#!/bin/bash
# Wiki Validate - Validate documentation quality
# Usage: ./scripts/wiki-validate.sh /path/to/repo

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_PATH="${1:-.}"

# Convert to absolute path
if [[ "$REPO_PATH" != /* ]]; then
    REPO_PATH="$(cd "$REPO_PATH" 2>/dev/null && pwd)"
fi

echo "========================================="
echo "  Repo Wiki - Validate"
echo "========================================="
echo ""
echo "Repository: $REPO_PATH"
echo ""

# Check if docs exist
if [ ! -d "$REPO_PATH/docs" ]; then
    echo "❌ No docs/ directory found."
    echo "Run: ./scripts/wiki-init.sh $REPO_PATH"
    exit 1
fi

# Run CLI validate
uv run "$SCRIPT_DIR/repo_wiki_cli.py" validate "$REPO_PATH"

# Try mkdocs build if available
echo ""
if command -v mkdocs &> /dev/null && [ -f "$REPO_PATH/mkdocs.yml" ]; then
    echo "Testing MkDocs build..."
    cd "$REPO_PATH"
    if mkdocs build --strict --quiet 2>/dev/null; then
        echo "✅ MkDocs build successful"
    else
        echo "⚠️  MkDocs build has warnings/errors"
    fi
fi

echo ""
echo "========================================="
echo "Validation complete!"
echo "========================================="
