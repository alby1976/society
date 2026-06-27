# Python Content Generator

This is a small, complete generator stack:

- Python generator and CLI
- Jinja2 templates
- Markdown source files
- Automated build scripts
- Obsidian vault generation
- Governance dashboards, registries, dependency maps, and validation reports
- PDF and DOCX generation

Beginner Jinja2 guide: `docs/dummies-guide-to-jinja2.md`

`source/site.yml` examples: `docs/site-yml-examples.md`

Generator config reference: `docs/generator-yml.md`

## Quick Start

Windows PowerShell:

```powershell
.\scripts\build.ps1
```

Linux or macOS terminal:

```bash
chmod +x ./scripts/build.sh
./scripts/build.sh
```

Run directly with Python:

```powershell
python .\build.py
```

```bash
python3 ./build.py
```

Generated files are written to `dist/`:

- `dist/vault/` - Obsidian-ready Markdown vault
- `dist/guide.pdf` - PDF export
- `dist/guide.docx` - Word export
- optional `dist/site/` - static HTML website when enabled in `generator.yml`

Build paths and output filenames are configured in `generator.yml`.

## Edit Content

Add Markdown files anywhere under `source/`. The generator discovers them
recursively, reads YAML frontmatter from each file, and preserves the folder
structure in `dist/vault/`.

Use `source/site.yml` for project-level metadata and optional page overrides.
You no longer need to list every Markdown file in `site.yml`; a `pages:` entry
is only needed when you want to override metadata or force a specific order.
Change files in `templates/` to control how normal vault pages are rendered.

Use `generator.yml` for build behavior such as source paths, output filenames,
generated note locations, and frontmatter field groups.

## `site.yml` Or Source File?

Put changes in the Markdown source file when the change belongs to that
document itself:

- document body text
- headings, lists, tables, and references
- normal document metadata such as `document-id`, `title`, `version`, `status`, `type`, `tags`, and review dates
- governance metadata such as `owner`, `decision-id`, `dependencies`, and `changes`
- the generated filename `slug`, when it should travel with the document

Use `source/site.yml` when the change is about the project as a whole or about
build-time control:

- project title, subtitle, and author
- forcing a specific page order for PDF, DOCX, or the main vault index
- temporarily overriding one document's metadata without editing the Markdown file
- keeping all document metadata in one central file by choice
- migrating older projects that already list pages in `site.yml`

As a rule of thumb, put durable document facts in the Markdown file. Use
`source/site.yml` for project-level metadata, ordering, and intentional
exceptions.

## Project Layout

The generator expects this layout:

```text
your-project/
  generator.yml
  source/
    site.yml
    policies/
      publishing.md
    procedures/
      build-workflow.md
  templates/
    index.md.j2
    page.md.j2
```

Markdown files carry document metadata in YAML frontmatter:

```markdown
---
document-id: "DOC-REC-0001"
title: "Publishing Outputs Policy"
version: "1.0.0"
status: "approved"
type: "policy"
document-category: "records-management"
effective-date: "2026-06-25"
last-reviewed: "2026-06-25"
tags: ["publishing", "records", "pdf", "docx", "obsidian"]
author: "Codex"
next-review-date: "2027-06-25"
approved-by: "Executive Director"
authority-level: "executive"
slug: "03 Publishing Outputs Policy"
---

# Publishing Outputs Policy

Write the document body here.
```

`document-id` is the permanent identifier for the document. Keep it stable even
if the title, filename, folder, or `slug` changes. Use `decision-id` separately
for governance decisions that should appear in the decision register.

`source/site.yml` controls the project and can optionally override individual
documents:

```yaml
title: "Generator Starter Kit"
subtitle: "A reusable Python pipeline for Markdown, Obsidian, PDF, and DOCX."
author: "Codex"
pages:
  - title: "Governance Document Standard"
    version: "1.0.0"
    status: "approved"
    type: "standard"
    document-category: "governance"
    effective-date: "2026-06-25"
    last-reviewed: "2026-06-25"
    tags: ["governance", "markdown", "obsidian"]
    author: "Codex"
    next-review-date: "2027-06-25"
    review-cycle: "annual"
    approved-by: "Board of Directors"
    authority-level: "board"
    related-documents: ["[[Board Governance Policy]]"]
    document-id: "DOC-GOV-0001"
    file: "overview.md"
    slug: "01 Governance Document Standard"
```

In this context, **override** means that a value in `source/site.yml` replaces
the same value from a Markdown file's YAML frontmatter for that one listed
document. The source Markdown file is matched by `pages[].file`.

For example, if `source/pages/overview.md` contains:

```yaml
---
document-id: "DOC-GOV-0001"
title: "Old Title"
status: "draft"
version: "1.0.0"
---
```

and `source/site.yml` contains:

```yaml
pages:
  - file: "overview.md"
    title: "Governance Document Standard"
    status: "approved"
```

then the build uses `title: "Governance Document Standard"` and
`status: "approved"` for that document. It still uses `version: "1.0.0"` from
the Markdown frontmatter because `version` was not overridden in `site.yml`.
It also keeps `document-id: "DOC-GOV-0001"` because permanent IDs normally live
with the document.

`pages[].file` means "the `file` field inside each item in the `pages:` list."
In the example above, the page item has `file: "overview.md"`, so that value is
that item's `pages[].file`.

`pages[].file` points to the source Markdown file that the override applies to.
It is not the generated vault filename. For example:

```yaml
pages:
  - file: "overview.md"
    slug: "01 Governance Document Standard"
  - file: "policies/publishing.md"
    slug: "03 Publishing Outputs Policy"
```

When `pages[].file` is just a filename such as `overview.md`, it is resolved
relative to `source/pages/` for backward compatibility. Nested paths such as
`policies/publishing.md` are resolved relative to `source/`. The `slug` value
becomes the generated Obsidian note filename while the folder path is preserved.

More examples are included in `docs/site-yml-examples.md`, including project
metadata only, forced ordering, single-document overrides, nested folders, and
full metadata in `site.yml`.

## Moving And Renaming Files

Safe to move or rename:

- Markdown documents under `source/`
- Subfolders under `source/`
- `source/pages/` itself, if you also move the Markdown files somewhere else under `source/`
- Markdown filenames, as long as any matching `pages[].file` value in `source/site.yml` is updated or removed
- Generated files under `dist/`, because each build recreates them
- Example files under `examples/`, unless you still use them directly
- Documentation under `docs/`

Safe to rename in frontmatter:

- `slug`, which controls the generated Obsidian note filename
- `title`, which controls display text in indexes, PDFs, and DOCX exports
- `tags`, `status`, `type`, `document-category`, and other metadata values used by generated registries and indexes

Do not casually rename `document-id`. It is intended to remain permanent across
title, filename, folder, and slug changes.

Keep these names and locations unless you also update the Python code:

- `content_generator/` - Python package imported by `build.py` and the CLI
- `build.py` - default direct build entry point
- `pyproject.toml` - package metadata, dependencies, and CLI registration

These paths are configurable in `generator.yml`:

- `source/` - `paths.source_dir`
- `source/site.yml` - `paths.site_file`
- `templates/` - `paths.template_dir`
- `dist/` - `paths.dist_dir`
- `dist/vault/` - `paths.vault_dir`
- `dist/vault/00 Index.md` - `outputs.index_note`
- `dist/guide.pdf` - `outputs.pdf_file`
- `dist/guide.docx` - `outputs.docx_file`
- generated registry/index note paths - `generated_notes`

Avoid manually editing files under `dist/` if you need persistent changes. Put
the change in `source/`, `templates/`, or `content_generator/` instead, then
run the build again.

## Generated Vault Notes

Every build recreates `dist/vault/` and writes:

- `00 Index.md` - top-level cross-linked page index
- `Home Dashboard.md` - status, category, recently reviewed, and Dataview summary
- `Governance Dashboard.md` - review queues, drafts, approved policies, and topical Dataview dashboards
- `Document Registry.md` - static registry plus Dataview registry query
- `Decision Register.md` - documents with `decision-id` or `type: decision`
- `Dependency Map.md` - dependency list plus Mermaid graph generated from `dependencies`
- `Link Validation Report.md` - missing links, broken dependency references, and orphan documents
- `Release Notes.md` - version/status notes ordered by effective date
- `Changelog.md` - automatic changelog generated from `changes` metadata, with version metadata as a fallback
- `Review Schedule.md` - owner and review-date inventory
- `International Dashboard.md` - jurisdiction, chapter, governance-level, and parent document dashboard
- `_indexes/By Category.md`
- `_indexes/By Status.md`
- `_indexes/By Type.md`
- `_indexes/By Tag.md`
- `_indexes/By Jurisdiction.md`
- `_indexes/By Chapter.md`
- `_indexes/Dataview Queries.md`

## Universal Markdown Governance Format

Generated page notes use the universal Markdown governance format. Required frontmatter properties are always emitted in this order:

```yaml
document-id:
title:
version:
status:
type:
document-category:
effective-date:
last-reviewed:
tags:
```

Recommended properties are emitted only when present in Markdown frontmatter or `source/site.yml`:

```yaml
author:
next-review-date:
review-cycle:
approved-by:
authority-level:
related-documents:
owner:
decision-id:
dependencies:
changes:
jurisdiction:
chapter:
governance-level:
parent-document:
applies-to:
reserved-power:
local-adaptation:
```

Optional properties are emitted only when present in Markdown frontmatter or `source/site.yml`:

```yaml
scriptural-foundation:
confessional-foundation:
supersedes:
```

The generator raises an error when a required property is missing or blank. Optional and recommended fields are omitted when they are not supplied, so generated Markdown does not contain placeholder values such as `TBD`, `null`, or empty lists.

## Sample Import

Use this pattern when calling the generator from your own Python file:

```python
from pathlib import Path

from content_generator import Generator

project_root = Path("C:/docs/my-generator-project")
Generator(project_root).build_all()
```

The selected `project_root` must contain `source/` and `templates/`. See `examples/import_and_build.py` for a runnable sample.

If the package has not been installed yet and you run a script from a nested folder, add the project root to `sys.path` before importing:

```python
from pathlib import Path
import sys

project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from content_generator import Generator

Generator(project_root).build_all()
```

## API Documentation

The code uses NumPy-style docstrings, so API documentation tools such as Sphinx can read the public classes and functions.

Example Sphinx setup:

```powershell
pip install sphinx napoleon
sphinx-apidoc -o docs/api content_generator
```

In `docs/conf.py`, enable NumPy-style parsing:

```python
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
napoleon_numpy_docstring = True
```
