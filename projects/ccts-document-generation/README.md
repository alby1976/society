# CCTS COMPLETE-01 — All-in-One Merged Governance Vault

This package consolidates the generated Christian Community Transformation Society governance vault materials into one repository-ready folder.

## Contents

- `source/` — merged Markdown source documents
- `ccts_generator/` — Python generator source code, if available from DEV packages
- `scripts/` — build, audit, merge, export, and test scripts
- `templates/` — Jinja2 templates
- `tests/` — pytest starter tests
- `.github/workflows/` — GitHub Actions workflows
- `config/` — build configuration
- `packages_readme_archive/` — README files from the individual generated packages
- `MERGE_REPORT.md` — what was merged and any conflicts

## Source of Truth

Edit documents in:

```text
source/
```

Generated output in `dist/` should not be edited as the master copy.

## Quick Start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python build.py
```

On macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python build.py
```

Then open:

```text
dist/obsidian-vault/
```

in Obsidian.

## Recommended First Review

Open these notes first in Obsidian:

1. `Master Governance Dashboard`
2. `Master Document Registry`
3. `Master Decision Register`
4. `Master Changelog`
5. `Master Release Plan`
6. `Final Governance Readiness Report`

## Metadata Rule

`scriptural-foundation` and `confessional-foundation` should be populated only when those references directly provide the foundation for that specific document.

Leave these fields blank for ordinary administrative, registry, operational, legal-readiness, audit, release, template, and build-system documents unless directly foundational.

## Release Status

This is a merged draft package, not formal adoption.

Before official use, complete:

- theological review;
- legal review;
- board review;
- church advisory review where needed;
- finance review;
- safeguarding and privacy review;
- link and YAML audit;
- final readiness report.

## Generated

Generated on: 2026-06-29
Packages scanned: 67
