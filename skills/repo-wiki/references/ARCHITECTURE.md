# Repo Wiki Skill Architecture

## Overview

The repo-wiki skill is composed of 6 sub-skills that work together.

## Sub-Skills

1. **repo-wiki-initialize** - Bootstrap wiki structure
2. **repo-wiki-index** - Build code map
3. **repo-wiki-generate** - Generate documentation with citations
4. **repo-wiki-detect** - Detect code changes
5. **repo-wiki-update** - Incrementally update documentation
6. **repo-wiki-validate** - Enforce quality gates

## Data Flow

```
[Initialize] -> [Index] -> [Generate] -> [Validate]
                                            |
                                            v
[Code Changes] -> [Detect] -> [Update] -> [Validate]
```

## State Files

- `.repo_wiki/state.json` - Run history and mappings
- `.repo_wiki/manifest.json` - Citation metadata
- `.repo_wiki/code_index.json` - Code map
- `.repo_wiki/change_set.json` - Change analysis

## Managed Block Strategy

```markdown
<!-- BEGIN:REPO_WIKI_MANAGED -->
Agent content...
<!-- END:REPO_WIKI_MANAGED -->
```
