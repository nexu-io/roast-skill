#!/bin/bash
# roast-skill setup — installs Python dependencies for Twitter data fetching
# Run once after installing the skill

set -e

SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV_DIR="$SKILL_DIR/.venv"

echo "🔧 Setting up roast-skill dependencies..."

# Find Python 3
PYTHON=""
for cmd in python3.12 python3.11 python3.10 python3; do
  if command -v "$cmd" &>/dev/null; then
    PYTHON="$cmd"
    break
  fi
done

if [ -z "$PYTHON" ]; then
  echo "❌ Python 3 not found. Please install Python 3.10+"
  exit 1
fi

echo "Using $PYTHON ($(${PYTHON} --version))"

# Create venv if needed
if [ ! -d "$VENV_DIR" ]; then
  echo "Creating virtual environment..."
  "$PYTHON" -m venv "$VENV_DIR"
fi

# Install twitter-cli
echo "Installing twitter-cli..."
"$VENV_DIR/bin/pip" install -q twitter-cli

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next: configure Twitter authentication"
echo "Run: $VENV_DIR/bin/twitter auth"
echo "This will open a browser for Twitter cookie-based login."
echo ""
echo "Or manually place cookies at: ~/.agent-reach/twitter-cookies.txt"
