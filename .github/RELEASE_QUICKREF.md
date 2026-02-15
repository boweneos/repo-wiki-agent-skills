# Release Quick Reference

## 🚀 Create a Release (5 Steps)

```bash
# 1. Update version in pyproject.toml
vim pyproject.toml  # Change version = "X.Y.Z"

# 2. Update CHANGELOG.md
vim CHANGELOG.md    # Move items from [Unreleased] to [X.Y.Z]

# 3. Commit
git add pyproject.toml CHANGELOG.md
git commit -m "chore: bump version to X.Y.Z"
git push

# 4. Tag
git tag -a vX.Y.Z -m "Release version X.Y.Z"

# 5. Push tag (triggers automation)
git push origin vX.Y.Z
```

## 📦 What Gets Created

| Asset | Description | Use Case |
|-------|-------------|----------|
| `.whl` | Python wheel | `pip install file.whl` |
| `.tar.gz` (dist) | Python source | `pip install file.tar.gz` |
| `.tar.gz` (full) | Complete source | Extract and use |
| `.zip` | Complete source | Windows users |

## 🏷️ Version Types

| Type | Format | Example | PyPI Upload |
|------|--------|---------|-------------|
| Patch | X.Y.Z | v1.0.1 | ✅ Yes |
| Minor | X.Y.0 | v1.1.0 | ✅ Yes |
| Major | X.0.0 | v2.0.0 | ✅ Yes |
| Alpha | X.Y.Z-alpha.N | v1.1.0-alpha.1 | ❌ No |
| Beta | X.Y.Z-beta.N | v1.1.0-beta.1 | ❌ No |
| RC | X.Y.Z-rc.N | v1.1.0-rc.1 | ❌ No |

## ⚡ Common Commands

```bash
# List all tags
git tag -l

# Delete local tag
git tag -d vX.Y.Z

# Delete remote tag
git push --delete origin vX.Y.Z

# View tag details
git show vX.Y.Z

# Create annotated tag
git tag -a vX.Y.Z -m "Message"

# Create lightweight tag
git tag vX.Y.Z

# Push all tags
git push --tags

# Push specific tag
git push origin vX.Y.Z
```

## 🔍 Check Release Status

```bash
# View GitHub Actions
# https://github.com/YOUR-ORG/repo-wiki-agent-skills/actions

# View Releases
# https://github.com/YOUR-ORG/repo-wiki-agent-skills/releases

# Download asset
wget https://github.com/YOUR-ORG/repo-wiki-agent-skills/releases/download/vX.Y.Z/file.tar.gz
```

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Release failed | Check Actions tab for logs |
| Wrong version | Delete tag, fix, re-tag |
| Missing asset | Check workflow file paths |
| PyPI failed | Verify PYPI_API_TOKEN secret |

## 📋 Pre-Release Checklist

- [ ] All tests passing
- [ ] Version updated in `pyproject.toml`
- [ ] CHANGELOG.md updated
- [ ] Changes committed
- [ ] On correct branch (main)

## 🎯 Post-Release Checklist

- [ ] Release appears on GitHub
- [ ] All 4 assets attached
- [ ] Release notes correct
- [ ] PyPI package available (if configured)
- [ ] Badges updated

## 🔐 PyPI Setup (One-Time)

```bash
# 1. Create token at https://pypi.org/manage/account/token/
# 2. Add as GitHub secret: PYPI_API_TOKEN
# 3. Future releases auto-upload to PyPI
```

## 📊 Semantic Versioning

```
MAJOR.MINOR.PATCH

MAJOR: Breaking changes (v1.0.0 → v2.0.0)
MINOR: New features (v1.0.0 → v1.1.0)
PATCH: Bug fixes (v1.0.0 → v1.0.1)
```

## 🔄 Rollback Release

```bash
# 1. Delete release on GitHub (web UI)
# 2. Delete tag
git push --delete origin vX.Y.Z
git tag -d vX.Y.Z

# 3. Fix issue and re-release
```

## 💡 Tips

- ✅ Always use annotated tags (`-a` flag)
- ✅ Follow semantic versioning
- ✅ Update CHANGELOG before tagging
- ✅ Test in pre-release first
- ✅ Keep release notes concise
- ❌ Don't edit releases manually (use CHANGELOG)
- ❌ Don't skip version numbers
- ❌ Don't reuse deleted tags

## 📞 Help

- Issues: https://github.com/YOUR-ORG/repo-wiki-agent-skills/issues
- Docs: See [RELEASE.md](../RELEASE.md) for detailed guide
