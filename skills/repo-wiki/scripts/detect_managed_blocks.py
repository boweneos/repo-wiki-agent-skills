#!/usr/bin/env uv run python
"""Find and parse managed block markers in documentation."""
import re
import sys
from pathlib import Path

def detect_managed_blocks():
    """Find all managed blocks in docs."""
    
    docs_path = Path("docs")
    results = []
    
    for md_file in docs_path.glob("**/*.md"):
        with open(md_file, errors='ignore') as f:
            content = f.read()
        
        pattern = r'<!-- BEGIN:REPO_WIKI_MANAGED -->(.*?)<!-- END:REPO_WIKI_MANAGED -->'
        blocks = re.findall(pattern, content, re.DOTALL)
        
        if blocks:
            results.append({
                "file": str(md_file),
                "block_count": len(blocks),
                "total_lines": len(content.splitlines())
            })
    
    print(f"Found managed blocks in {len(results)} files:\n")
    
    for result in results:
        print(f"  {result['file']}: {result['block_count']} blocks")
    
    return 0

if __name__ == "__main__":
    sys.exit(detect_managed_blocks())
