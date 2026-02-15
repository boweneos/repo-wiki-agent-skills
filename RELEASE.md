# Release Guide

This document describes how to create a new release of Repo Wiki Agent Skills.

## Prerequisites

- Push access to the repository
- Git configured with your credentials
- All tests passing on the main branch

## Release Process

### 1. Update Version

Update the version in `pyproject.toml`:

```toml
[project]
version = "1.1.0"  # Update this
```

### 2. Update CHANGELOG.md

Move items from `[Unreleased]` to a new version section:

```markdown
## [1.1.0] - 2026-01-15

### Added
- New feature description

### Changed
- Changed feature description

### Fixed
- Bug fix description
```

Add the new version link at the bottom:

```markdown
[1.1.0]: https://github.com/agent-skills/repo-wiki-agent-skills/releases/tag/v1.1.0
```

### 3. Commit Changes

```bash
git add pyproject.toml CHANGELOG.md
git commit -m "chore: bump version to 1.1.0"
git push origin main
```

### 4. Create and Push Tag

```bash
# Create annotated tag
git tag -a v1.1.0 -m "Release version 1.1.0"

# Push the tag
git push origin v1.1.0
```

### 5. Automated Release

Once the tag is pushed, GitHub Actions will automatically:

1. ✅ Build Python wheel and source distribution
2. ✅ Create `.tar.gz` and `.zip` archives of the source
3. ✅ Extract release notes from CHANGELOG.md
4. ✅ Create a GitHub Release with all assets
5. ✅ Upload to PyPI (if `PYPI_API_TOKEN` secret is configured)

### 6. Verify Release

1. Go to [Releases](https://github.com/agent-skills/repo-wiki-agent-skills/releases)
2. Verify the new release is published
3. Check that all assets are attached:
   - `repo_wiki_agent_skills-X.Y.Z-py3-none-any.whl`
   - `repo-wiki-agent-skills-X.Y.Z.tar.gz` (Python source)
   - `repo-wiki-agent-skills-vX.Y.Z.tar.gz` (Full source archive)
   - `repo-wiki-agent-skills-vX.Y.Z.zip` (Full source archive)

## Release Types

### Patch Release (1.0.X)

For bug fixes and minor improvements:

```bash
# Example: 1.0.0 -> 1.0.1
git tag -a v1.0.1 -m "Release version 1.0.1"
```

### Minor Release (1.X.0)

For new features (backwards compatible):

```bash
# Example: 1.0.0 -> 1.1.0
git tag -a v1.1.0 -m "Release version 1.1.0"
```

### Major Release (X.0.0)

For breaking changes:

```bash
# Example: 1.0.0 -> 2.0.0
git tag -a v2.0.0 -m "Release version 2.0.0"
```

## Pre-release Versions

For alpha, beta, or release candidates:

```bash
# Alpha
git tag -a v1.1.0-alpha.1 -m "Release version 1.1.0-alpha.1"

# Beta
git tag -a v1.1.0-beta.1 -m "Release version 1.1.0-beta.1"

# Release Candidate
git tag -a v1.1.0-rc.1 -m "Release version 1.1.0-rc.1"
```

Pre-releases are automatically marked as "pre-release" on GitHub.

## PyPI Configuration (Optional)

To enable automatic PyPI uploads:

1. Create a PyPI API token at https://pypi.org/manage/account/token/
2. Add it as a repository secret named `PYPI_API_TOKEN`
3. Future releases will automatically upload to PyPI

## Troubleshooting

### Release Failed

Check the [Actions](https://github.com/agent-skills/repo-wiki-agent-skills/actions) tab for error details.

Common issues:
- Build failures: Check Python dependencies
- Asset creation: Verify file paths in workflow
- PyPI upload: Check token permissions

### Delete a Release

```bash
# Delete remote tag
git push --delete origin v1.1.0

# Delete local tag
git tag -d v1.1.0

# Delete GitHub release via web interface
```

### Fix Release Notes

Edit the release on GitHub's web interface to update the description.

## Download Assets

Users can download release assets via:

### GitHub Releases

```bash
# Download specific version
wget https://github.com/agent-skills/repo-wiki-agent-skills/releases/download/v1.0.0/repo-wiki-agent-skills-v1.0.0.tar.gz
```

### PyPI (if configured)

```bash
pip install repo-wiki-agent-skills==1.0.0
```

### Direct Installation

```bash
# Install from wheel
pip install https://github.com/agent-skills/repo-wiki-agent-skills/releases/download/v1.0.0/repo_wiki_agent_skills-1.0.0-py3-none-any.whl
```

## Release Checklist

- [ ] All tests passing
- [ ] Version updated in `pyproject.toml`
- [ ] CHANGELOG.md updated with changes
- [ ] Changes committed and pushed
- [ ] Tag created and pushed
- [ ] GitHub Actions workflow completed successfully
- [ ] Release appears on GitHub with all assets
- [ ] Release notes are accurate
- [ ] (Optional) Package available on PyPI

## Versioning Strategy

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** version: Incompatible API changes
- **MINOR** version: Backwards-compatible functionality
- **PATCH** version: Backwards-compatible bug fixes

## Questions?

Open an issue or discussion on GitHub if you need help with releases.
