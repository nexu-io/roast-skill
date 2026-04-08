#!/usr/bin/env python3
"""
Fetch Twitter/X profile and recent tweets for roast-skill.
Uses twitter-cli under the hood.

Usage:
  python twitter_fetch.py <username> [--count 30] [--output /tmp/result.json]

Output JSON:
  { "profile": {...}, "tweets": [...] }
"""

import argparse
import json
import os
import subprocess
import sys

def find_twitter_cli():
    """Find twitter CLI binary in common locations."""
    candidates = [
        # roast-skill's own venv
        os.path.join(os.path.dirname(__file__), "..", ".venv", "bin", "twitter"),
        # agent-reach venv
        os.path.expanduser("~/.agent-reach-venv/bin/twitter"),
        # global
        "twitter",
    ]
    for c in candidates:
        full = os.path.expanduser(c)
        if os.path.isfile(full) and os.access(full, os.X_OK):
            return full
        # Check PATH
        if c == "twitter":
            import shutil
            found = shutil.which("twitter")
            if found:
                return found
    return None

def run_twitter(cli, args):
    """Run twitter CLI and return stdout."""
    cmd = [cli] + args
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            print(f"Warning: twitter CLI returned {result.returncode}", file=sys.stderr)
            if result.stderr:
                print(result.stderr[:500], file=sys.stderr)
        return result.stdout
    except FileNotFoundError:
        print(f"Error: twitter CLI not found at {cli}", file=sys.stderr)
        return ""
    except subprocess.TimeoutExpired:
        print("Error: twitter CLI timed out", file=sys.stderr)
        return ""

def fetch_profile(cli, username):
    """Fetch user profile as JSON."""
    output = run_twitter(cli, ["user", username, "--json"])
    if not output.strip():
        return None
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        # Try parsing key-value output
        return {"raw": output}

def fetch_tweets(cli, username, count=30):
    """Fetch recent tweets as JSON."""
    output = run_twitter(cli, ["tweets", username, "--count", str(count), "--json"])
    if not output.strip():
        return []
    try:
        data = json.loads(output)
        if isinstance(data, list):
            return data
        return [data]
    except json.JSONDecodeError:
        return [{"raw": output}]

def main():
    parser = argparse.ArgumentParser(description="Fetch Twitter data for roast-skill")
    parser.add_argument("username", help="Twitter username (without @)")
    parser.add_argument("--count", type=int, default=30, help="Number of tweets to fetch")
    parser.add_argument("--output", "-o", help="Output JSON file path")
    args = parser.parse_args()

    username = args.username.lstrip("@")

    cli = find_twitter_cli()
    if not cli:
        print(json.dumps({
            "error": "twitter-cli not found",
            "setup": "Run: bash scripts/setup.sh (in roast-skill directory)"
        }))
        sys.exit(1)

    print(f"Using twitter CLI: {cli}", file=sys.stderr)
    print(f"Fetching @{username}...", file=sys.stderr)

    profile = fetch_profile(cli, username)
    tweets = fetch_tweets(cli, username, args.count)

    result = {
        "username": username,
        "profile": profile,
        "tweets": tweets,
        "tweet_count": len(tweets)
    }

    output = json.dumps(result, ensure_ascii=False, indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Saved to {args.output}", file=sys.stderr)
    else:
        print(output)

if __name__ == "__main__":
    main()
