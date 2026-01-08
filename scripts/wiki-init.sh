#!/bin/bash
# Wiki Init - Initialize wiki structure
# Usage: ./scripts/wiki-init.sh /path/to/repo

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_PATH="${1:-.}"

# Convert to absolute path
if [[ "$REPO_PATH" != /* ]]; then
    REPO_PATH="$(cd "$REPO_PATH" 2>/dev/null && pwd)"
fi

echo "========================================="
echo "  Repo Wiki - Initialize"
echo "========================================="
echo ""
echo "Repository: $REPO_PATH"
echo ""

# Run CLI init
echo "Step 1: Creating wiki structure..."
uv run "$SCRIPT_DIR/repo_wiki_cli.py" init "$REPO_PATH"

echo ""
echo "Step 2: Indexing codebase..."
uv run "$SCRIPT_DIR/repo_wiki_cli.py" index "$REPO_PATH"

echo ""
echo "========================================="
echo "✅ Wiki structure initialized!"
echo "========================================="
echo ""
echo "Next steps:"
echo ""
echo "  Option A: Use Cursor AI to generate content"
echo "    1. Open the repository in Cursor"
echo "    2. Type /wiki-init in chat"
echo "    3. Provide the repo path: $REPO_PATH"
echo ""
echo "  Option B: Use Claude API directly"
echo "    export ANTHROPIC_API_KEY=your-key"
echo "    uv run $SCRIPT_DIR/repo_wiki_llm.py generate $REPO_PATH"
echo ""
echo "  Option C: Generate manually"
echo "    Edit the placeholder files in $REPO_PATH/docs/"
echo ""
