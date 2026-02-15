# State File Format

## .repo_wiki/state.json

```json
{
  "schema_version": "1.0",
  "last_run_commit": "abc1234...",
  "baseline_commit": "abc1234...",
  "repo_remote_url": "https://github.com/org/repo",
  "repo_name": "my-repo",
  "created_at": "2024-01-01T00:00:00Z",
  "last_updated_at": "2024-01-02T12:00:00Z",
  "ignore_patterns": [".git/**", "node_modules/**"],
  "pages": {}
}
```

## .repo_wiki/manifest.json

```json
{
  "schema_version": "1.0",
  "generated_at": "2024-01-01T12:00:00Z",
  "baseline_commit": "abc1234...",
  "pages": {
    "docs/components/auth.md": {
      "citations": [
        {"filepath": "src/auth/service.ts", "start_line": 10, "end_line": 50}
      ]
    }
  }
}
```

## .repo_wiki/change_set.json

```json
{
  "last_commit": "abc1234...",
  "current_commit": "def5678...",
  "added": [],
  "modified": [],
  "deleted": [],
  "renamed": [],
  "affected_components": [],
  "impacted_pages": []
}
```
