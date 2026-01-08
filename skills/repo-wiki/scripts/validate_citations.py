#!/usr/bin/env uv run python
"""Validate that all citations in the wiki point to valid files and line ranges."""
import json
import os
import sys

def validate_citations():
    """Validate all citations in manifest."""
    errors = []
    
    manifest_path = ".repo_wiki/manifest.json"
    if not os.path.exists(manifest_path):
        print("❌ manifest.json not found")
        return 1
    
    with open(manifest_path) as f:
        manifest = json.load(f)
    
    pages = manifest.get("pages", {})
    
    for page_path, page_data in pages.items():
        citations = page_data.get("citations", [])
        
        for citation in citations:
            filepath = citation.get("filepath", "")
            start_line = citation.get("start_line", 0)
            end_line = citation.get("end_line", 0)
            
            if not os.path.exists(filepath):
                errors.append(f"{page_path}: File not found: {filepath}")
                continue
            
            with open(filepath, errors='ignore') as f:
                line_count = sum(1 for _ in f)
            
            if start_line < 1 or start_line > line_count:
                errors.append(f"{page_path}: Invalid start line {start_line} in {filepath}")
            
            if end_line < start_line or end_line > line_count:
                errors.append(f"{page_path}: Invalid end line {end_line} in {filepath}")
    
    if errors:
        print(f"❌ Found {len(errors)} citation errors:")
        for error in errors:
            print(f"  - {error}")
        return 1
    else:
        print("✓ All citations valid")
        return 0

if __name__ == "__main__":
    sys.exit(validate_citations())
