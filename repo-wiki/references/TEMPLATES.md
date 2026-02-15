# Page Template Specifications

## Template Variables

- `{{REPO_NAME}}` - Repository name
- `{{BASELINE_COMMIT}}` - Git commit SHA
- `{{TODAY}}` - Current date (YYYY-MM-DD)
- `{{REMOTE_URL}}` - Git remote URL
- `{{COMPONENT_NAME}}` - Component name
- `{{COMPONENT_PATH}}` - Path to component

## Available Templates

1. `mkdocs.yml.template` - MkDocs configuration
2. `component-page.md.template` - Component documentation
3. `overview-page.md.template` - Main index page
4. `architecture-page.md.template` - Architecture documentation

## Managed Block Markers

```markdown
<!-- BEGIN:REPO_WIKI_MANAGED -->
Agent content...
<!-- END:REPO_WIKI_MANAGED -->
```

## Frontmatter Standard

```yaml
---
generated_by: repo-wiki-agent
baseline_commit: "abc1234..."
last_updated: "2024-01-01"
managed_sections:
  - "## Section Name"
---
```
