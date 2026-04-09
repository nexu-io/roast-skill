#!/usr/bin/env python3
"""
Fetch Feishu messages for a target user across groups.
Designed for roast-skill — collects message data for AI roast generation.

Supports two modes:
  1. User token mode (preferred): Uses user_access_token via OAuth to read ALL
     groups the authorizing user is in. No need to add bot to every group.
  2. Bot token mode (fallback): Uses tenant_access_token, can only read groups
     the bot has been added to.

Usage:
  # User token mode (preferred — reads all user's groups)
  python feishu_fetch.py --app-id <id> --app-secret <secret> --target-user <open_id> --user-token <token> [--output /tmp/result.json]

  # Bot token mode (fallback — only reads bot's groups)
  python feishu_fetch.py --app-id <id> --app-secret <secret> --target-user <open_id> [--output /tmp/result.json]

  # OAuth helper: generate authorization URL for user to click
  python feishu_fetch.py --app-id <id> --oauth-url [--redirect-uri <uri>]

  # OAuth helper: exchange auth code for user token
  python feishu_fetch.py --app-id <id> --app-secret <secret> --auth-code <code>

Environment variables (alternative to flags):
  FEISHU_APP_ID, FEISHU_APP_SECRET, FEISHU_USER_TOKEN

Output JSON:
  { "target_user": "...", "mode": "user_token|bot_token", "total_messages": N, "groups": [...], "messages": [...] }
"""

import argparse
import json
import os
import sys
import time
import urllib.parse

try:
    import requests
except ImportError:
    print("Error: requests library not found. Run: pip install requests", file=sys.stderr)
    sys.exit(1)

# --- Config & Token Management ---

TOKEN_CACHE_FILE = os.path.expanduser("~/.nexu/feishu-user-token.json")

# Config paths: desktop app path first, then traditional runtime path
CONFIG_PATHS = [
    os.path.expanduser("~/Library/Application Support/@nexu/desktop/.nexu/config.json"),
    os.path.expanduser("~/.nexu/config.json"),
]


def load_feishu_credentials_from_config():
    """Auto-detect Feishu app_id and app_secret from OpenClaw config files.
    Tries desktop app path first, then falls back to ~/.nexu/config.json.
    Returns (app_id, app_secret) or (None, None) if not found.
    """
    for config_path in CONFIG_PATHS:
        if not os.path.exists(config_path):
            continue
        try:
            with open(config_path) as f:
                config = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue

        channels = config.get("channels", [])
        secrets = config.get("secrets", {})

        for ch in channels:
            if ch.get("channelType") != "feishu":
                continue
            app_id = ch.get("appId")
            if not app_id:
                continue
            # Find app_secret in secrets: channel:{uuid}:appSecret
            ch_uuid = ch.get("uuid", "")
            app_secret = secrets.get(f"channel:{ch_uuid}:appSecret")
            if app_id and app_secret:
                print(f"✅ Loaded Feishu credentials from {config_path}", file=sys.stderr)
                return app_id, app_secret
    return None, None


def get_tenant_token(app_id, app_secret):
    """Get tenant access token (bot identity)."""
    r = requests.post(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": app_id, "app_secret": app_secret},
    )
    data = r.json()
    if data.get("code") != 0:
        print(f"Tenant token error: {data}", file=sys.stderr)
        sys.exit(1)
    return data["tenant_access_token"]


def get_app_access_token(app_id, app_secret):
    """Get app access token (needed for user token exchange)."""
    r = requests.post(
        "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal",
        json={"app_id": app_id, "app_secret": app_secret},
    )
    data = r.json()
    if data.get("code") != 0:
        print(f"App token error: {data}", file=sys.stderr)
        sys.exit(1)
    return data["app_access_token"]


def generate_oauth_url(app_id, redirect_uri="https://open.feishu.cn/document/home/index"):
    """Generate OAuth authorization URL for user to click.
    
    IMPORTANT: The 'scope' parameter is required! Without it, the token only gets
    auth:user.id:read and cannot read chats or messages. This was the root cause
    of persistent 99991679 errors during development.
    """
    params = {
        "app_id": app_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "state": "roast-skill",
        "scope": "im:chat:readonly im:message:readonly contact:contact.base:readonly",
    }
    url = "https://open.feishu.cn/open-apis/authen/v1/authorize?" + urllib.parse.urlencode(params)
    return url


def exchange_code_for_user_token(app_id, app_secret, auth_code):
    """Exchange OAuth authorization code for user_access_token."""
    app_token = get_app_access_token(app_id, app_secret)
    r = requests.post(
        "https://open.feishu.cn/open-apis/authen/v1/oidc/access_token",
        headers={"Authorization": f"Bearer {app_token}", "Content-Type": "application/json"},
        json={"grant_type": "authorization_code", "code": auth_code},
    )
    data = r.json()
    if data.get("code") != 0:
        print(f"Token exchange error: {data}", file=sys.stderr)
        sys.exit(1)
    token_data = data.get("data", {})
    # Save token for reuse
    cache = {
        "access_token": token_data.get("access_token"),
        "refresh_token": token_data.get("refresh_token"),
        "expires_at": int(time.time()) + token_data.get("expires_in", 7200) - 300,
        "app_id": app_id,
    }
    os.makedirs(os.path.dirname(TOKEN_CACHE_FILE), exist_ok=True)
    with open(TOKEN_CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)
    print(f"✅ User token saved to {TOKEN_CACHE_FILE}", file=sys.stderr)
    print(f"   Expires in {token_data.get('expires_in', 0)} seconds", file=sys.stderr)
    print(f"   User: {token_data.get('name', 'unknown')}", file=sys.stderr)
    return token_data.get("access_token")


def refresh_user_token(app_id, app_secret, refresh_token):
    """Refresh an expired user_access_token."""
    app_token = get_app_access_token(app_id, app_secret)
    r = requests.post(
        "https://open.feishu.cn/open-apis/authen/v1/oidc/refresh_access_token",
        headers={"Authorization": f"Bearer {app_token}", "Content-Type": "application/json"},
        json={"grant_type": "refresh_token", "refresh_token": refresh_token},
    )
    data = r.json()
    if data.get("code") != 0:
        print(f"Token refresh error: {data}", file=sys.stderr)
        return None
    token_data = data.get("data", {})
    cache = {
        "access_token": token_data.get("access_token"),
        "refresh_token": token_data.get("refresh_token"),
        "expires_at": int(time.time()) + token_data.get("expires_in", 7200) - 300,
        "app_id": app_id,
    }
    with open(TOKEN_CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)
    print("✅ User token refreshed", file=sys.stderr)
    return token_data.get("access_token")


def load_cached_user_token(app_id, app_secret):
    """Try to load and auto-refresh cached user token."""
    if not os.path.exists(TOKEN_CACHE_FILE):
        return None
    try:
        with open(TOKEN_CACHE_FILE) as f:
            cache = json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

    if cache.get("app_id") != app_id:
        return None

    # Check if token is still valid
    if cache.get("expires_at", 0) > int(time.time()):
        return cache.get("access_token")

    # Try refresh
    refresh_tok = cache.get("refresh_token")
    if refresh_tok:
        print("User token expired, refreshing...", file=sys.stderr)
        return refresh_user_token(app_id, app_secret, refresh_tok)

    return None


# --- Data Fetching ---


def get_user_chats(headers):
    """Get all chats the user is in (user_access_token mode)."""
    chats = []
    page_token = ""
    while True:
        url = "https://open.feishu.cn/open-apis/im/v1/chats?page_size=100&user_id_type=open_id"
        if page_token:
            url += f"&page_token={page_token}"
        r = requests.get(url, headers=headers)
        data = r.json()
        if data.get("code") != 0:
            print(f"Chat list error: {data.get('msg')} (code: {data.get('code')})", file=sys.stderr)
            break
        items = data.get("data", {}).get("items", [])
        chats.extend(items)
        if not data.get("data", {}).get("has_more"):
            break
        page_token = data["data"].get("page_token", "")
        time.sleep(0.1)
    return chats


def get_bot_chats(headers):
    """Get all chats the bot is in (tenant_access_token mode)."""
    chats = []
    page_token = ""
    while True:
        url = "https://open.feishu.cn/open-apis/im/v1/chats?page_size=100"
        if page_token:
            url += f"&page_token={page_token}"
        r = requests.get(url, headers=headers)
        data = r.json()
        if data.get("code") != 0:
            print(f"Chat list error: {data.get('msg')}", file=sys.stderr)
            break
        items = data.get("data", {}).get("items", [])
        chats.extend(items)
        if not data.get("data", {}).get("has_more"):
            break
        page_token = data["data"].get("page_token", "")
    return chats


def get_chat_members(headers, chat_id):
    """Get members of a chat. Silently skips unsupported group types."""
    members = []
    page_token = ""
    while True:
        url = f"https://open.feishu.cn/open-apis/im/v1/chats/{chat_id}/members?page_size=100"
        if page_token:
            url += f"&page_token={page_token}"
        r = requests.get(url, headers=headers)
        data = r.json()
        if data.get("code") != 0:
            # Silently skip — could be external group, permission issue, etc.
            break
        items = data.get("data", {}).get("items", [])
        members.extend(items)
        if not data.get("data", {}).get("has_more"):
            break
        page_token = data["data"].get("page_token", "")
    return members


def get_messages(headers, chat_id, target_user, max_pages=40):
    """Fetch messages from target user in a chat."""
    msgs = []
    page_token = ""
    for page in range(1, max_pages + 1):
        url = f"https://open.feishu.cn/open-apis/im/v1/messages?container_id_type=chat&container_id={chat_id}&page_size=50"
        if page_token:
            url += f"&page_token={page_token}"
        r = requests.get(url, headers=headers)
        data = r.json()
        if data.get("code") != 0:
            msg = data.get("msg", "")
            # Silently skip unsupported chat types (b2c/b2b external groups)
            if "app type is not supported" in msg or "b2c" in msg or "b2b" in msg:
                print(f"    ⏭️ Skipped (external/unsupported group)", file=sys.stderr)
            else:
                print(f"  Messages error (page {page}): {msg}", file=sys.stderr)
            break
        items = data.get("data", {}).get("items", [])
        for msg in items:
            if msg.get("sender", {}).get("id") == target_user:
                body_content = msg.get("body", {}).get("content", "")
                msgs.append(
                    {
                        "chat_id": chat_id,
                        "msg_type": msg.get("msg_type"),
                        "create_time": msg.get("create_time"),
                        "body": body_content,
                        "message_id": msg.get("message_id", ""),
                    }
                )
        if not data.get("data", {}).get("has_more"):
            break
        page_token = data["data"].get("page_token", "")
        time.sleep(0.15)
    return msgs


# --- Main Flows ---


def fetch_with_user_token(user_token, target_user, output_path):
    """Fetch messages using user_access_token — can read ALL user's groups."""
    headers = {"Authorization": f"Bearer {user_token}", "Content-Type": "application/json"}

    print("🔑 Mode: user_access_token (can read all user's groups)", file=sys.stderr)
    print("Finding groups with target user...", file=sys.stderr)

    chats = get_user_chats(headers)
    print(f"  User is in {len(chats)} chats", file=sys.stderr)

    shared_groups = []
    for chat in chats:
        chat_id = chat.get("chat_id")
        if not chat_id:
            continue
        # Skip p2p chats — only group chats have rich multi-party data
        if chat.get("chat_mode") == "p2p":
            continue
        members = get_chat_members(headers, chat_id)
        member_ids = [m.get("member_id") for m in members]
        if target_user in member_ids:
            shared_groups.append(
                {"chat_id": chat_id, "name": chat.get("name", ""), "member_count": len(members)}
            )
            print(f"  ✓ Shared group: {chat.get('name', chat_id)}", file=sys.stderr)
        time.sleep(0.1)

    print(f"\nFound {len(shared_groups)} shared groups, fetching messages...", file=sys.stderr)

    all_msgs = []
    for group in shared_groups:
        print(f"  Reading {group['name'] or group['chat_id']}...", file=sys.stderr)
        msgs = get_messages(headers, group["chat_id"], target_user)
        all_msgs.extend(msgs)
        print(f"    → {len(msgs)} messages", file=sys.stderr)

    result = {
        "target_user": target_user,
        "mode": "user_token",
        "total_messages": len(all_msgs),
        "shared_groups": shared_groups,
        "messages": all_msgs,
    }

    output = json.dumps(result, ensure_ascii=False, indent=2)
    if output_path:
        with open(output_path, "w") as f:
            f.write(output)
        print(f"\n✅ Saved {len(all_msgs)} messages from {len(shared_groups)} groups to {output_path}", file=sys.stderr)
    else:
        print(output)


def fetch_with_bot_token(app_id, app_secret, target_user, output_path):
    """Fetch messages using tenant_access_token — only bot's groups."""
    token = get_tenant_token(app_id, app_secret)
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    print("🤖 Mode: tenant_access_token (only bot's groups)", file=sys.stderr)
    print("Finding shared groups...", file=sys.stderr)

    chats = get_bot_chats(headers)
    print(f"  Bot is in {len(chats)} chats", file=sys.stderr)

    shared_groups = []
    for chat in chats:
        chat_id = chat.get("chat_id")
        if not chat_id:
            continue
        members = get_chat_members(headers, chat_id)
        member_ids = [m.get("member_id") for m in members]
        if target_user in member_ids:
            shared_groups.append(
                {"chat_id": chat_id, "name": chat.get("name", ""), "member_count": len(members)}
            )
            print(f"  ✓ Shared group: {chat.get('name', chat_id)}", file=sys.stderr)
        time.sleep(0.1)

    print(f"\nFound {len(shared_groups)} shared groups, fetching messages...", file=sys.stderr)

    all_msgs = []
    for group in shared_groups:
        print(f"  Reading {group['name'] or group['chat_id']}...", file=sys.stderr)
        msgs = get_messages(headers, group["chat_id"], target_user)
        all_msgs.extend(msgs)
        print(f"    → {len(msgs)} messages", file=sys.stderr)

    result = {
        "target_user": target_user,
        "mode": "bot_token",
        "total_messages": len(all_msgs),
        "shared_groups": shared_groups,
        "messages": all_msgs,
    }

    output = json.dumps(result, ensure_ascii=False, indent=2)
    if output_path:
        with open(output_path, "w") as f:
            f.write(output)
        print(f"\n✅ Saved {len(all_msgs)} messages from {len(shared_groups)} groups to {output_path}", file=sys.stderr)
    else:
        print(output)


def main():
    parser = argparse.ArgumentParser(description="Fetch Feishu messages for roast-skill")
    parser.add_argument("--app-id", default=os.environ.get("FEISHU_APP_ID"), help="Feishu App ID")
    parser.add_argument("--app-secret", default=os.environ.get("FEISHU_APP_SECRET"), help="Feishu App Secret")
    parser.add_argument("--target-user", help="Target user open_id")
    parser.add_argument("--user-token", default=os.environ.get("FEISHU_USER_TOKEN"), help="User access token (preferred)")
    parser.add_argument("--output", "-o", help="Output JSON file path")

    # OAuth helpers
    parser.add_argument("--oauth-url", action="store_true", help="Generate OAuth authorization URL")
    parser.add_argument("--redirect-uri", default="https://open.feishu.cn/document/home/index", help="OAuth redirect URI")
    parser.add_argument("--auth-code", help="Exchange OAuth auth code for user token")

    # Verification
    parser.add_argument("--verify", action="store_true", help="Verify that messages can actually be read (quick test)")

    args = parser.parse_args()

    # --- Auto-detect credentials from config for all modes ---
    if not args.app_id or not args.app_secret:
        config_id, config_secret = load_feishu_credentials_from_config()
        if not args.app_id and config_id:
            args.app_id = config_id
        if not args.app_secret and config_secret:
            args.app_secret = config_secret

    # --- OAuth URL generation ---
    if args.oauth_url:
        if not args.app_id:
            print("Error: --app-id required for OAuth URL generation", file=sys.stderr)
            sys.exit(1)
        url = generate_oauth_url(args.app_id, args.redirect_uri)
        print(f"OAuth URL:\n{url}")
        print(f"\nUser clicks this link → authorizes → gets redirected with ?code=xxx", file=sys.stderr)
        print(f"Then run: python {sys.argv[0]} --app-id {args.app_id} --app-secret <secret> --auth-code <code>", file=sys.stderr)
        return

    # --- OAuth code exchange ---
    if args.auth_code:
        if not args.app_id or not args.app_secret:
            print("Error: --app-id and --app-secret required for code exchange", file=sys.stderr)
            sys.exit(1)
        token = exchange_code_for_user_token(args.app_id, args.app_secret, args.auth_code)
        print(f"\nuser_access_token: {token}")
        return

    # --- Main fetch flow ---
    # --- Verify mode: quick test if messages can actually be read ---
    if args.verify:
        if not args.app_id or not args.app_secret:
            print('{"canRead": false, "error": "no_credentials"}')
            sys.exit(1)
        token = get_tenant_token(args.app_id, args.app_secret)
        if not token:
            print('{"canRead": false, "error": "token_failed"}')
            sys.exit(1)
        headers = {"Authorization": f"Bearer {token}"}
        # Get first chat bot is in
        r = requests.get("https://open.feishu.cn/open-apis/im/v1/chats?page_size=1", headers=headers)
        data = r.json()
        chats = data.get("data", {}).get("items", [])
        if not chats:
            print('{"canRead": false, "error": "no_chats", "reason": "Bot is not in any group chat"}')
            sys.exit(0)
        chat_id = chats[0]["chat_id"]
        chat_name = chats[0].get("name", "unknown")
        # Try to read 1 message
        msg_r = requests.get(
            f"https://open.feishu.cn/open-apis/im/v1/messages?container_id_type=chat&container_id={chat_id}&page_size=1",
            headers=headers,
        )
        msg_data = msg_r.json()
        if msg_data.get("code") == 0:
            msg_count = len(msg_data.get("data", {}).get("items", []))
            print(json.dumps({"canRead": True, "testChat": chat_name, "messagesFound": msg_count}))
        else:
            err_msg = msg_data.get("msg", "unknown error")
            print(json.dumps({"canRead": False, "error": "read_failed", "testChat": chat_name, "detail": err_msg}))
        sys.exit(0)

    if not args.target_user:
        print("Error: --target-user required", file=sys.stderr)
        sys.exit(1)

    if not args.app_id or not args.app_secret:
        print("Error: Feishu app credentials required. Checked:", file=sys.stderr)
        print(f"  --app-id/--app-secret flags: not provided", file=sys.stderr)
        print(f"  FEISHU_APP_ID/FEISHU_APP_SECRET env vars: not set", file=sys.stderr)
        for p in CONFIG_PATHS:
            print(f"  {p}: {'exists' if os.path.exists(p) else 'not found'}", file=sys.stderr)
        sys.exit(1)

    # Try user token first (preferred)
    user_token = args.user_token or load_cached_user_token(args.app_id, args.app_secret)

    if user_token:
        # Verify token is valid
        test_r = requests.get(
            "https://open.feishu.cn/open-apis/authen/v1/user_info",
            headers={"Authorization": f"Bearer {user_token}"},
        )
        if test_r.json().get("code") == 0:
            fetch_with_user_token(user_token, args.target_user, args.output)
            return
        else:
            print("User token invalid, falling back to bot token mode", file=sys.stderr)

    # Fallback to bot token
    fetch_with_bot_token(args.app_id, args.app_secret, args.target_user, args.output)


if __name__ == "__main__":
    main()
