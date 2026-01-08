# RPD: Repo Wiki Agent Skills for Incremental, Citation-Backed Knowledge Base (Markdown + MkDocs)  
  
## 1. Summary  
  
Build a set of agent “skills” that can generate and maintain a repository wiki as a structured collection of Markdown `.md`) files (MkDocs-compatible). The agent must:  
  
- Create a brand-new wiki from an existing codebase.  
- Detect code changes and incrementally update only the affected wiki pages.  
- Add missing pages for new modules/features.  
- Include **codebase citations with file paths and exact line ranges** for every non-trivial technical claim.  
  
Primary output: a `/docs` directory containing a navigable, consistent documentation set plus a `mkdocs.yml` (or equivalent) configuration.  
  
---  
  
## 2. Problem Statement  
  
Engineering teams often lack up-to-date internal documentation because:  
- Manual docs drift quickly from the code.  
- “Big bang” doc generation is expensive to rerun.  
- Without citations, docs are hard to trust and harder to review.  
  
We need an agent that produces a **living wiki** tied directly to the code, with **auditable citations** and **incremental updates** after each change.  
  
---  
  
## 3. Goals and Non-Goals  
  
### 3.1 Goals  
1. **One-command wiki creation**  
   - Generate a complete baseline wiki from a repository.  
2. **Incremental updates**  
   - Use diffs to update only impacted pages.  
3. **Strong traceability**  
   - Every generated page includes citations pointing to specific files and line ranges.  
4. **Stable information architecture**  
   - Predictable folder structure; consistent page templates.  
5. **Review-friendly output**  
   - Small PRs when possible; deterministic formatting; link-checkable.  
6. **Safe around secrets**  
   - Avoid copying secrets, tokens, `.env`, private keys; minimize large code excerpts.  
  
### 3.2 Non-Goals  
- Replacing API reference generators (e.g., Javadoc/Sphinx) entirely.  
- Perfect semantic understanding of every codebase edge case.  
- Automatic architectural correctness beyond what can be grounded in citations.  
- Real-time background syncing (runs are explicit).  
  
---  
  
## 4. Target Users  
  
- **Engineers**: need trustworthy docs with source links.  
- **Tech leads/architects**: need architectural overview and dependency mapping.  
- **New joiners**: need onboarding and “how it works” explanations.  
- **Reviewers**: want citation-backed claims to verify quickly.  
  
---  
  
## 5. Key Requirements  
  
### 5.1 Functional Requirements  
**FR1 — Baseline wiki generation**  
- Input: repository path (local) and optionally remote URL.  
- Output: `/docs` markdown tree + `mkdocs.yml` (or `docs/.pages` for other systems).  
- Must generate:  
  - Overview pages (what it is, how to run, architecture).  
  - Module/component pages.  
  - Key workflows (build/test/deploy if present).  
  - Glossary (optional but recommended).  
  
**FR2 — Change detection**  
- Detect changes via:  
  - Git diff between a stored baseline commit and current HEAD; or  
  - filesystem timestamp/hash when git isn’t available.  
- Determine impacted documentation pages.  
  
**FR3 — Incremental update**  
- Update only impacted pages and navigation.  
- Add pages for new modules; deprecate/archive removed ones (configurable).  
  
**FR4 — Citations with line numbers**  
- Every generated technical statement (behavior, contract, config, defaults) must be supported by citations.  
- Citations must include:  
  - Relative file path  
  - Start and end line numbers  
  - (Preferable) commit SHA for stability  
  
**FR5 — Linkable citations**  
- If remote is known (GitHub/GitLab), emit clickable permalinks:  
  - `https://host/org/repo/blob/<sha>/<path>#Lx-Ly`  
- Otherwise, emit a local citation format (still with line numbers).  
  
**FR6 — Preservation of human edits**  
- Do not overwrite manual edits unintentionally.  
- Support “managed blocks” that the agent owns and can safely rewrite.  
  
### 5.2 Non-Functional Requirements  
- **NFR1 Determinism**: same input commit ⇒ same output (modulo timestamps).  
- **NFR2 Bounded changes**: incremental run should minimize diffs (stable formatting/order).  
- **NFR3 Performance**: incremental run scales with diff size (not full repo scan unless needed).  
- **NFR4 Safety**: exclude secrets and sensitive files; configurable denylist patterns.  
- **NFR5 Verifiability**: a validator checks that every citation points to valid lines.  
  
---  
  
## 6. Assumptions  
  
- Repository is readable on disk.  
- Git is available for best results (diff + stable commit SHAs).  
- Default output target is MkDocs:  
  - `mkdocs.yml`  
  - `docs/` content tree  
- “Structured mk files” interpreted as **structured Markdown** (MkDocs-ready). (If you meant a different “.mk” format, the same design applies but the renderer changes.)  
  
---  
  
## 7. Outputs and Repo Layout  
  
### 7.1 Generated Files  
```  
mkdocs.yml  
docs/  
  [index.md](http://index.md)  
  getting-started/  
    [local-dev.md](http://local-dev.md)  
    [configuration.md](http://configuration.md)  
  architecture/  
    [overview.md](http://overview.md)  
    [data-flow.md](http://data-flow.md)  
    [dependency-map.md](http://dependency-map.md)  
  components/  
    <component-a>.md  
    <component-b>.md  
  api/  
    [endpoints.md](http://endpoints.md)            # if applicable  
  operations/  
    [build-and-test.md](http://build-and-test.md)  
    [deploy.md](http://deploy.md)               # if applicable  
  adr/  
    adr-0001-...md          # optional  
  [glossary.md](http://glossary.md)  
  [changelog.md](http://changelog.md)              # auto-maintained doc changelog (optional)  
.repo_wiki/  
  state.json                # baseline commit, mappings, hashes  
  manifest.json             # page -> citations -> source fingerprints  
  logs/  
```  
  
### 7.2 Page Conventions  
- Frontmatter on each page (optional but recommended):  
```yaml  
---  
generated_by: repo-wiki-agent  
baseline_commit: "<sha>"  
last_updated: "YYYY-MM-DD"  
managed_sections:  
  - "## Generated Summary"  
  - "## Key Interfaces"  
---  
```  
  
---  
  
## 8. Citation Specification  
  
### 8.1 Markdown Citation Format (Recommended)  
Use footnotes or inline “Source:” blocks.  
  
**Inline example:**  
```md  
The service starts an HTTP server on the configured port.    
Source: `src/server.ts` L12–L48  
```  
  
**Footnote example (preferred for cleanliness):**  
```md  
The service starts an HTTP server on the configured port.[^server_start]  
  
[^server_start]: `src/server.ts` L12–L48 (commit `abc1234`)  
```  
  
### 8.2 Remote Permalink Format (If Remote Known)  
```md  
[^server_start]: [https://github.com/org/repo/blob/abc1234/src/server.ts#L12-L48](https://github.com/org/repo/blob/abc1234/src/server.ts#L12-L48)  
```  
  
### 8.3 Citation Coverage Rule  
A page must not contain “assertive” statements without citations, including:  
- default values  
- error behaviors  
- performance characteristics inferred from code  
- control flow descriptions  
- configuration keys and meaning  
  
Allow uncited content only for:  
- navigation text  
- high-level “intent” phrasing explicitly labeled as interpretation  
  
---  
  
## 9. Incremental Update Strategy  
  
### 9.1 State Tracking  
Maintain `.repo_wiki/state.json` containing:  
- `baseline_commit`  
- `last_run_commit`  
- `repo_remote_url` (optional)  
- `doc_version`  
- ignore patterns used  
- index of generated pages and their source dependencies  
  
Example structure:  
```json  
{  
  "last_run_commit": "abc1234",  
  "repo_remote_url": "[https://github.com/org/repo](https://github.com/org/repo)",  
  "pages": {  
    "docs/components/[auth.md](http://auth.md)": {  
      "sources": [  
        {"path": "src/auth/auth_service.ts", "ranges": [[10,88],[120,170]]}  
      ],  
      "fingerprints": {  
        "src/auth/auth_service.ts": "sha256:..."  
      }  
    }  
  }  
}  
```  
  
### 9.2 Impact Analysis (How we decide what to update)  
On incremental run:  
1. Compute changed files `git diff --name-only <last_run_commit>..HEAD`).  
2. Map changed files to impacted pages:  
   - Direct mapping via stored `pages[].sources[].path`  
   - Plus heuristic mapping:  
     - folder-to-component ownership (e.g., `src/auth/**` ⇒ `components/auth.md`)  
     - symbol-level mapping if available (optional)  
3. Update:  
   - impacted component pages  
   - architecture diagrams/pages if dependency graph changed  
   - index/nav if new pages are added  
  
### 9.3 Regeneration Rules  
- If a page’s cited lines shift due to edits, the agent must:  
  - re-locate the referenced symbol/block (AST-based if possible; fallback: fuzzy match)  
  - refresh line ranges  
- If source is deleted:  
  - mark doc section as “Removed/Unknown” and cite last known commit if available, or remove section.  
  
---  
  
## 10. Skills Design  
  
This section defines the agent skills as composable, testable units.  
  
### Skill A — `InitializeWiki`  
**Purpose:** Create the wiki skeleton and baseline state.  
  
- **Inputs**  
  - `repo_path`  
  - `output_docs_path` (default `docs/`)  
  - `wiki_engine` (default `mkdocs`)  
  - `remote_url` (optional)  
- **Actions**  
  - Detect languages/frameworks (by file patterns + config files)  
  - Generate IA (information architecture)  
  - Write `mkdocs.yml`  
  - Create initial pages with placeholders and managed blocks  
  - Create `.repo_wiki/state.json`  
- **Outputs**  
  - Structured markdown tree + nav config  
- **Success Criteria**  
  - MkDocs builds successfully  
  - All pages have consistent headers and managed sections  
  
### Skill B — `IndexCodebase`  
**Purpose:** Build a code map for documentation and citations.  
  
- **Inputs**  
  - `repo_path`  
  - ignore patterns  
- **Actions**  
  - Enumerate files  
  - Extract:  
    - public entrypoints  
    - modules/components  
    - key configs (Dockerfile, CI, build scripts)  
    - exported APIs (heuristic)  
  - Build dependency hints (imports, package references)  
- **Outputs**  
  - `code_index.json` (internal artifact)  
- **Success Criteria**  
  - Index covers ≥95% of non-vendor source files (configurable)  
  
### Skill C — `GeneratePages`  
**Purpose:** Produce citation-backed markdown pages.  
  
- **Inputs**  
  - `code_index`  
  - page templates  
  - citation mode (local vs permalink)  
- **Actions**  
  - For each component/module:  
    - Summarize responsibility  
    - Document key interfaces/classes/functions  
    - Add configuration and error behavior  
    - Add examples (only if grounded)  
  - Attach citations for each assertion  
- **Outputs**  
  - `docs/**.md`  
  - Update `.repo_wiki/manifest.json`  
- **Success Criteria**  
  - Validator passes: all citations resolve to real file+line ranges  
  
### Skill D — `DetectChanges`  
**Purpose:** Determine what changed since last run.  
  
- **Inputs**  
  - git repo + `.repo_wiki/state.json`  
- **Actions**  
  - Compute diff (files changed, renamed, deleted)  
  - Capture commit SHA  
- **Outputs**  
  - `change_set` object (added/modified/deleted/renamed)  
- **Success Criteria**  
  - Correctly identifies file movement/renames when possible  
  
### Skill E — `PlanIncrementalUpdate`  
**Purpose:** Decide which pages to update/add/remove.  
  
- **Inputs**  
  - `change_set`  
  - `.repo_wiki/manifest.json`  
  - heuristics (path-to-component rules)  
- **Actions**  
  - Impact analysis  
  - Produce a plan: list of pages to regenerate, pages to create, nav updates  
- **Outputs**  
  - `update_plan.json`  
- **Success Criteria**  
  - Plan touches minimal pages necessary  
  - Includes nav consistency steps  
  
### Skill F — `ApplyIncrementalUpdate`  
**Purpose:** Execute the update plan and refresh citations.  
  
- **Inputs**  
  - `update_plan`  
  - current repo state  
- **Actions**  
  - Regenerate impacted pages/sections  
  - Refresh citation line numbers  
  - Update state/manifest to new commit  
- **Outputs**  
  - Updated `docs/` + updated `.repo_wiki/*`  
- **Success Criteria**  
  - MkDocs builds  
  - Citation validator passes  
  
### Skill G — `ValidateWiki`  
**Purpose:** Enforce quality gates before merging.  
  
- **Inputs**  
  - `docs/`  
  - `.repo_wiki/manifest.json`  
- **Checks**  
  - Citation targets exist and line ranges valid  
  - No uncited assertive statements (best-effort lint)  
  - Links valid (internal)  
  - Nav consistent  
- **Outputs**  
  - `validation_report.md`  
- **Success Criteria**  
  - All checks pass or are explicitly waived with reasons  
  
---  
  
## 11. Managed Blocks and Human Edits  
  
### 11.1 Managed Block Markers  
Use explicit markers so the agent only rewrites safe regions:  
  
```md  
## Generated Summary  
<!-- BEGIN:REPO_WIKI_MANAGED -->  
... agent content ...  
<!-- END:REPO_WIKI_MANAGED -->  
  
## Team Notes  
... humans edit freely ...  
```  
  
### 11.2 Merge Policy  
- Rewrite only managed blocks.  
- If a managed block was edited manually, either:  
  - keep manual edits and append “Agent suggestions” section, or  
  - fail validation and request review (configurable behavior).  
  
---  
  
## 12. Heuristics for Structure and Coverage  
  
### 12.1 Component Detection Heuristics  
- Folder-based:  
  - `src/<domain>/...` ⇒ component `<domain>`  
- Config-based:  
  - presence of `routes/`, `controllers/`, `services/` implies web service  
- Entrypoints:  
  - `main.*`, `index.*`, `app.*`, `server.*`  
- Infra:  
  - `Dockerfile`, `docker-compose.*`, `.github/workflows/*`, `helm/`, `terraform/`  
  
### 12.2 Page Templates (Minimum)  
Each component page should include:  
- Responsibility  
- Public interfaces (exported functions/classes)  
- Key data structures  
- Error handling  
- Configuration  
- Observability hooks (logs/metrics) if present  
- Citations throughout  
  
---  
  
## 13. Quality Gates and Metrics  
  
### 13.1 Required Quality Gates  
- **Build Gate:** `mkdocs build` (or markdown lint) succeeds.  
- **Citation Gate:** 100% of citations resolve; no dangling line ranges.  
- **Drift Gate:** If a page references removed code, it must be updated or flagged.  
  
### 13.2 Metrics  
- Citation coverage ratio (assertions with citations / total assertions)  
- Incremental scope ratio (pages changed / pages total)  
- Validation pass rate  
- Runtime per diff size (internal measurement)  
  
---  
  
## 14. Security and Safety Considerations  
  
- Default ignore patterns:  
  - `.env`, `*.pem`, `id_rsa`, `secrets.*`, `credentials.*`  
  - `node_modules/`, `dist/`, `build/`, vendor directories  
- Avoid copying large code blocks; prefer short snippets and citations.  
- Do not summarize secrets even if detected; redact.  
  
---  
  
## 15. Failure Modes and Recovery  
  
- **Line number drift:** relocate code blocks using fuzzy match / AST nodes; otherwise fall back to nearest match and flag.  
- **Renamed/moved files:** use git rename detection; update citations accordingly.  
- **Mass refactors:** allow a “full rebuild” mode that regenerates the entire wiki.  
- **Ambiguous ownership:** create a “Needs Review” section with conservative statements and citations.  
  
---  
  
## 16. Acceptance Criteria  
  
A solution is accepted if it can:  
  
1. **Initial run**  
   - Generate `docs/` and `mkdocs.yml`  
   - Build successfully  
   - Include citations with file paths + line ranges on all technical claims  
  
2. **Incremental run**  
   - After modifying a small set of files, only impacted pages change  
   - Citations remain valid and line-accurate  
   - New modules produce new pages and nav entries  
  
3. **Validation**  
   - Automated validator produces a clean report (or explicit waivers)  
  
---  
  
## 17. Implementation Notes  
  
### 17.1 Suggested Tech Choices (Implementation-Agnostic)  
- Git diff for change detection  
- A parser layer:  
  - AST parsing where feasible (language-specific)  
  - fallback: regex + structural heuristics  
- A citation resolver that can:  
  - compute line numbers  
  - generate permalinks using commit SHA  
  
### 17.2 Minimal CLI Interface  
- `repo-wiki init --repo .`  
- `repo-wiki build --repo .`  
- `repo-wiki update --repo .`  
- `repo-wiki validate --repo .`  
  
---  
  
## 18. notes 
- Target: MkDocs (repo-local), with optional exporters later.
- Citations: SHA permalinks as the canonical citation; optional branch link for convenience.
- Lint: strict on agent-managed blocks, warn-only elsewhere, with explicit override annotations.
- ADRs: generate draft ADRs from PRs/issues/commits only when confidence is high; always require human approval to mark “Accepted.”
  
---  
