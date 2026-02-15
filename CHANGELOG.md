# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub Actions workflows for CI/CD
- Automated release process with downloadable assets

## [1.0.0] - 2026-01-09

### Added
- Complete Agent Skills implementation for repository wiki generation
- Seven modular skills: initialize, index, generate, detect, update, validate, and main orchestrator
- Citation-backed documentation with file paths and line ranges
- Incremental update system based on git diff
- Managed blocks for preserving human edits
- MkDocs-compatible output format
- Clickable permalinks to source code
- Quality validation gates
- Helper scripts for common operations:
  - `validate_citations.py` - Verify citation integrity
  - `generate_permalinks.py` - Convert citations to URLs
  - `detect_managed_blocks.py` - Find managed sections
  - `compute_page_impact.py` - Map changes to pages
- Documentation templates:
  - Component page template
  - Architecture page template
  - Overview page template
  - MkDocs configuration template
- Reference documentation:
  - Citation specification
  - Architecture overview
  - State format specification
  - Template documentation
- Shell scripts for workflows:
  - `wiki-init.sh` - First-time setup
  - `wiki-update.sh` - Incremental updates
  - `wiki-validate.sh` - Quality validation
- Cursor IDE commands:
  - `/wiki-init` - Initialize wiki
  - `/wiki-update` - Update documentation
  - `/wiki-validate` - Validate quality
- CLI interface via `repo-wiki` command
- Python package configuration with pyproject.toml
- Comprehensive README with usage examples
- Implementation summary documentation
- Quick start guide

### Features
- **Citation System**: Every technical claim backed by source code references
- **Incremental Updates**: Only regenerate pages affected by code changes
- **Managed Blocks**: Preserve human edits while allowing agent updates
- **Quality Gates**: Enforce citation validity, link integrity, and markdown syntax
- **MkDocs Integration**: Generate standard documentation sites
- **Performance**: Scales with change size, not repository size
- **Safety**: Excludes secrets and sensitive information
- **Traceability**: Commit SHA tracking for stable references

### Requirements Implemented
- ✅ FR1: Baseline wiki generation
- ✅ FR2: Change detection via git diff
- ✅ FR3: Incremental updates
- ✅ FR4: Citations with line numbers
- ✅ FR5: Linkable citations (permalinks)
- ✅ FR6: Preservation of human edits
- ✅ NFR1: Deterministic output
- ✅ NFR2: Bounded changes (incremental)
- ✅ NFR3: Performance scaling with diff size
- ✅ NFR4: Safety (secrets excluded)
- ✅ NFR5: Verifiable citations

### Compliance
- Agent Skills specification compliant
- MkDocs compatible
- Python 3.10+ support
- Cross-platform (Linux, macOS, Windows)

[Unreleased]: https://github.com/agent-skills/repo-wiki-agent-skills/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/agent-skills/repo-wiki-agent-skills/releases/tag/v1.0.0
