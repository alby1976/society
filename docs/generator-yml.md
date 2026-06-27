# `generator.yml` Configuration

`generator.yml` controls the generator runtime settings: where files are read
from, where outputs are written, what generated notes are named, and which
frontmatter fields are required or optional.

Use `generator.yml` for build behavior. Use `source/site.yml` for project
metadata and optional page overrides.

## Minimal Example

```yaml
paths:
  source_dir: "source"
  site_file: "source/site.yml"
  template_dir: "templates"
  dist_dir: "dist"
  vault_dir: "dist/vault"
  legacy_pages_dir: "pages"

outputs:
  index_note: "00 Index.md"
  pdf_file: "guide.pdf"
  docx_file: "guide.docx"
```

Missing settings fall back to the built-in defaults, so you can include only the
values you want to change.

## Paths

```yaml
paths:
  source_dir: "source"
  site_file: "source/site.yml"
  template_dir: "templates"
  dist_dir: "dist"
  vault_dir: "dist/vault"
  legacy_pages_dir: "pages"
```

- `source_dir` is scanned recursively for Markdown files.
- `site_file` stores project metadata and optional page overrides.
- `template_dir` stores Jinja templates.
- `dist_dir` receives PDF, DOCX, and other generated outputs.
- `vault_dir` is recreated every time the vault is built.
- `legacy_pages_dir` resolves bare `pages[].file` entries from `source/site.yml`.

## Output Names

```yaml
outputs:
  index_note: "00 Index.md"
  pdf_file: "guide.pdf"
  docx_file: "guide.docx"
```

- `index_note` is relative to `vault_dir`.
- `pdf_file` and `docx_file` are relative to `dist_dir`.

## Optional HTML

```yaml
html:
  enabled: false
  html_dir: "dist/site"
```

When `enabled` is `true`, `python build.py` also writes a small static HTML
website to `html_dir`. You can also build it directly with:

```bash
contentgen --target html
```

## Generated Notes

```yaml
generated_notes:
  home_dashboard: "Home Dashboard.md"
  governance_dashboard: "Governance Dashboard.md"
  document_registry: "Document Registry.md"
  decision_register: "Decision Register.md"
  dependency_map: "Dependency Map.md"
  link_validation_report: "Link Validation Report.md"
  release_notes: "Release Notes.md"
  changelog: "Changelog.md"
  review_schedule: "Review Schedule.md"
  international_dashboard: "International Dashboard.md"
  index_by_category: "_indexes/By Category.md"
  index_by_status: "_indexes/By Status.md"
  index_by_type: "_indexes/By Type.md"
  index_by_tag: "_indexes/By Tag.md"
  index_by_jurisdiction: "_indexes/By Jurisdiction.md"
  index_by_chapter: "_indexes/By Chapter.md"
  dataview_queries: "_indexes/Dataview Queries.md"
```

These values are vault-relative paths. You can rename generated notes or move
them into folders without editing Python code.

## Frontmatter Field Groups

```yaml
frontmatter:
  required:
    - "document-id"
    - "title"
    - "version"
    - "status"
    - "type"
    - "document-category"
    - "effective-date"
    - "last-reviewed"
    - "tags"
  recommended:
    - "author"
    - "next-review-date"
    - "review-cycle"
    - "approved-by"
    - "authority-level"
    - "related-documents"
    - "owner"
    - "decision-id"
    - "dependencies"
    - "changes"
    - "jurisdiction"
    - "chapter"
    - "governance-level"
    - "parent-document"
    - "applies-to"
    - "reserved-power"
    - "local-adaptation"
  optional:
    - "scriptural-foundation"
    - "confessional-foundation"
    - "supersedes"
```

- `required` fields must exist in Markdown frontmatter or `source/site.yml`.
- `recommended` fields are emitted when present.
- `optional` fields are emitted when present.

Fields are emitted in the order listed here.

`document-id` is required by default because it is the permanent identifier used
to track a document across title, filename, folder, and slug changes.

## Example: Rename Outputs

```yaml
outputs:
  index_note: "Home.md"
  pdf_file: "manual.pdf"
  docx_file: "manual.docx"

generated_notes:
  home_dashboard: "Dashboards/Home Dashboard.md"
  governance_dashboard: "Dashboards/Governance Dashboard.md"
  document_registry: "Registers/Document Registry.md"
  decision_register: "Registers/Decision Register.md"
  dependency_map: "Maps/Dependency Map.md"
  link_validation_report: "Reports/Link Validation Report.md"
  release_notes: "Release Notes.md"
  changelog: "Changelog.md"
  review_schedule: "Review Schedule.md"
  index_by_category: "Indexes/By Category.md"
  index_by_status: "Indexes/By Status.md"
  index_by_type: "Indexes/By Type.md"
  index_by_tag: "Indexes/By Tag.md"
  dataview_queries: "Indexes/Dataview Queries.md"
```

## Example: Move Source And Output Folders

```yaml
paths:
  source_dir: "docs-source"
  site_file: "docs-source/site.yml"
  template_dir: "jinja"
  dist_dir: "build"
  vault_dir: "build/obsidian"
  legacy_pages_dir: "pages"
```

After changing these paths, move the matching folders/files to the new
locations.

## Common Mistakes

- Do not set `vault_dir` outside `dist_dir` unless you understand that the vault
  folder is deleted and recreated during vault builds.
- Keep `site_file` inside or near the configured source tree so page paths stay
  easy to reason about.
- If you rename `template_dir`, move `index.md.j2` and `page.md.j2` there too.
- If you remove a required frontmatter field from `generator.yml`, generated
  documents will no longer validate that field.
