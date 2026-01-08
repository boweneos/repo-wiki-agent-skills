---
name: repo-wiki-index
description: Build a searchable code map of the repository. Extracts modules, components, APIs, configs, dependencies, and key symbols for documentation and citation purposes.
license: MIT
compatibility: Requires filesystem read access, git, uv (Python package manager)
metadata:
  version: 1.0.0
  parent_skill: repo-wiki
  category: documentation-indexing
allowed-tools: cat ls find git uv grep
---

# Repo Wiki Index Skill

Build a comprehensive code map for documentation generation and citation.

## Purpose

This skill creates a searchable index of the codebase that includes:

1. File inventory (with ignore patterns applied)
2. Module and component boundaries
3. Public interfaces (classes, functions, APIs)
4. Configuration files and their locations
5. Dependencies and imports
6. Key entrypoints

## When to Use

Use this skill:

- After running `repo-wiki-initialize`
- Before generating page content
- When the codebase structure has changed significantly

## Step-by-Step Instructions

### Step 1: Load Configuration

```bash
STATE_FILE=".repo_wiki/state.json"
```

### Step 2: Enumerate Files

```bash
find . -type f ! -path "./.git/*" ! -path "*/node_modules/*" > .repo_wiki/file_list.txt
```

### Step 3: Detect Technology Stack

Scan for language markers (package.json, requirements.txt, go.mod, etc.)

### Step 4: Identify Components

Map directory structure to logical components in `src/`, `lib/`, `packages/`.

### Step 5: Extract Public Interfaces

Find exported functions, classes, and APIs for each language.

### Step 6: Build Code Index

Create `.repo_wiki/code_index.json` with all findings.

## Output Files

- `.repo_wiki/code_index.json` - Main structured index
- `.repo_wiki/file_list.txt` - All indexed files
- `.repo_wiki/components.txt` - Component detection results
- `.repo_wiki/tech_stack.txt` - Technology detection

## Success Criteria

- ✅ `code_index.json` created
- ✅ Technology stack detected
- ✅ Components mapped
- ✅ Entrypoints identified

## Next Steps

After indexing:
1. **Generate page content**: Read `repo-wiki-generate/SKILL.md`
