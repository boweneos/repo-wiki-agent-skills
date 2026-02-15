#!/usr/bin/env uv run python
"""Convert local citations to remote permalinks using git remote URL."""
import json
import re
import sys
from pathlib import Path

def generate_permalinks():
    """Convert citations to permalinks."""
    
    with open(".repo_wiki/state.json") as f:
        state = json.load(f)
    
    remote_url = state.get("repo_remote_url", "")
    baseline_commit = state.get("baseline_commit", "")
    
    if not remote_url:
        print("⚠️  No remote URL configured")
        return 1
    
    if remote_url.startswith("git@github.com:"):
        remote_url = remote_url.replace("git@github.com:", "https://github.com/")
    if remote_url.endswith(".git"):
        remote_url = remote_url[:-4]
    
    print(f"Remote: {remote_url}")
    print(f"Commit: {baseline_commit}")
    
    docs_path = Path("docs")
    updated_count = 0
    
    for md_file in docs_path.glob("**/*.md"):
        with open(md_file) as f:
            content = f.read()
        
        pattern = r'`([^`]+)`\s+L(\d+)[-–]L(\d+)'
        
        def replace_with_permalink(match):
            filepath = match.group(1)
            start_line = match.group(2)
            end_line = match.group(3)
            permalink = f"{remote_url}/blob/{baseline_commit}/{filepath}#L{start_line}-L{end_line}"
            return f"[{filepath}#L{start_line}-L{end_line}]({permalink})"
        
        new_content = re.sub(pattern, replace_with_permalink, content)
        
        if new_content != content:
            with open(md_file, 'w') as f:
                f.write(new_content)
            updated_count += 1
            print(f"✓ Updated {md_file}")
    
    print(f"\n✓ Generated permalinks in {updated_count} files")
    return 0

if __name__ == "__main__":
    sys.exit(generate_permalinks())
