#!/usr/bin/env uv run python
"""Determine which pages are impacted by code changes."""
import json
import sys
from pathlib import Path

def compute_page_impact():
    """Map changed files to impacted documentation pages."""
    
    with open(".repo_wiki/change_set.json") as f:
        changes = json.load(f)
    
    with open(".repo_wiki/manifest.json") as f:
        manifest = json.load(f)
    
    impacted_pages = set()
    
    changed_files = (
        changes.get("added", []) +
        changes.get("modified", []) +
        changes.get("deleted", [])
    )
    
    for page_path, page_data in manifest.get("pages", {}).items():
        citations = page_data.get("citations", [])
        
        for citation in citations:
            if citation.get("filepath") in changed_files:
                impacted_pages.add(page_path)
                break
    
    print(f"Impacted pages: {len(impacted_pages)}\n")
    
    for page in sorted(impacted_pages):
        print(f"  - {page}")
    
    return 0

if __name__ == "__main__":
    sys.exit(compute_page_impact())
