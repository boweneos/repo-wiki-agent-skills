#!/bin/bash
# Wiki Update - Detect changes and update documentation
# Usage: ./scripts/wiki-update.sh /path/to/repo

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_PATH="${1:-.}"

# Convert to absolute path
if [[ "$REPO_PATH" != /* ]]; then
    REPO_PATH="$(cd "$REPO_PATH" 2>/dev/null && pwd)"
fi

echo "========================================="
echo "  Repo Wiki - Update"
echo "========================================="
echo ""
echo "Repository: $REPO_PATH"
echo ""

# Check if wiki exists
if [ ! -d "$REPO_PATH/.repo_wiki" ]; then
    echo "❌ Wiki not initialized."
    echo "Run: ./scripts/wiki-init.sh $REPO_PATH"
    exit 1
fi

# Run CLI detect
echo "Step 1: Detecting changes..."
uv run "$SCRIPT_DIR/repo_wiki_cli.py" detect "$REPO_PATH"

echo ""
echo "========================================="
echo "✅ Change detection complete!"
echo "========================================="
echo ""
echo "Next steps:"
echo ""
echo "  Option A: Use Cursor AI to update content"
echo "    1. Open the repository in Cursor"
echo "    2. Type /wiki-update in chat"
echo "    3. Provide the repo path: $REPO_PATH"
echo ""
echo "  Option B: Review changes manually"
echo "    cat $REPO_PATH/.repo_wiki/change_set.json"
echo ""
echo "  Then validate:"
echo "    ./scripts/wiki-validate.sh $REPO_PATH"
echo ""
