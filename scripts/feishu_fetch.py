#!/usr/bin/env python3
"""
Fetch Feishu messages for a target user across all shared groups.
Designed for roast-skill — collects message data for AI roast generation.

Usage:
  python feishu_fetch.py --app-id <id> --app-secret <secret> --target-user <open_id> [--output /tmp/result.json]

Environment variables (alternative to flags):
  FEISHU_APP_ID, FEISHU_APP_SECRET

Output JSON:
  { "target_user": "...", "total_messages": N, "groups": [...], "messages": [...] }
"""

import argparse
import json
import os
import sys
import time

try:
    import requests
except ImportError:
    print("Error: requests library not found. Run: pip install requests", file=sys.stderr)
    sys.exit(1)

def get_token(app_id, app_secret):
    """Get tenant access token."""
    r = requests.post(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        json={"app_id": app_id, "app_secret": app_secret}
    )
    data = r.json()
    if data.get("code") != 0:
        print(f"Token error: {data}", file=sys.stderr)
        sys.exit(1)
    return data["tenant_access_token"]

def get_bot_chats(headers):
    """Get all chats the bot is in."""
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
    """Get members of a chat."""
    members = []
    page_token = ""
    while True:
        url = f"https://open.feishu.cn/open-apis/im/v1/chats/{chat_id}/members?page_size=100"
        if page_token:
            url += f"&page_token={page_token}"
        r = requests.get(url, headers=headers)
        data = r.json()
        if data.get("code") != 0:
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
            print(f"  Messages error (page {page}): {data.get('msg')}", file=sys.stderr)
            break
        items = data.get("data", {}).get("items", [])
        for msg in items:
            if msg.get("sender", {}).get("id") == target_user:
                body_content = msg.get("body", {}).get("content", "")
                msgs.append({
                    "chat_id": chat_id,
                    "msg_type": msg.get("msg_type"),
                    "create_time": msg.get("create_time"),
                    "body": body_content,
                    "message_id": msg.get("message_id", "")
                })
        if not data.get("data", {}).get("has_more"):
            break
        page_token = data["data"].get("page_token", "")
        time.sleep(0.15)  # Rate limit
    return msgs

def main():
    parser = argparse.ArgumentParser(description="Fetch Feishu messages for roast-skill")
    parser.add_argument("--app-id", default=os.environ.get("FEISHU_APP_ID"), help="Feishu App ID")
    parser.add_argument("--app-secret", default=os.environ.get("FEISHU_APP_SECRET"), help="Feishu App Secret")
    parser.add_argument("--target-user", required=True, help="Target user open_id")
    parser.add_argument("--output", "-o", help="Output JSON file path")
    args = parser.parse_args()

    if not args.app_id or not args.app_secret:
        print("Error: Feishu app credentials required (--app-id/--app-secret or env vars)", file=sys.stderr)
        sys.exit(1)

    print("Getting token...", file=sys.stderr)
    token = get_token(args.app_id, args.app_secret)
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    print("Finding shared groups...", file=sys.stderr)
    chats = get_bot_chats(headers)
    print(f"  Bot is in {len(chats)} chats", file=sys.stderr)

    # Find groups where target user is also a member
    shared_groups = []
    for chat in chats:
        chat_id = chat.get("chat_id")
        if not chat_id:
            continue
        members = get_chat_members(headers, chat_id)
        member_ids = [m.get("member_id") for m in members]
        if args.target_user in member_ids:
            shared_groups.append({
                "chat_id": chat_id,
                "name": chat.get("name", ""),
                "member_count": len(members)
            })
            print(f"  ✓ Shared group: {chat.get('name', chat_id)}", file=sys.stderr)
        time.sleep(0.1)

    print(f"\nFound {len(shared_groups)} shared groups, fetching messages...", file=sys.stderr)

    all_msgs = []
    for group in shared_groups:
        print(f"  Reading {group['name'] or group['chat_id']}...", file=sys.stderr)
        msgs = get_messages(headers, group["chat_id"], args.target_user)
        all_msgs.extend(msgs)
        print(f"    → {len(msgs)} messages", file=sys.stderr)

    result = {
        "target_user": args.target_user,
        "total_messages": len(all_msgs),
        "shared_groups": shared_groups,
        "messages": all_msgs
    }

    output = json.dumps(result, ensure_ascii=False, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"\n✅ Saved {len(all_msgs)} messages to {args.output}", file=sys.stderr)
    else:
        print(output)

if __name__ == "__main__":
    main()
