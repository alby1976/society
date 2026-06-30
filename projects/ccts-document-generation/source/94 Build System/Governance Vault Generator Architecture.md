---
document-id: BUILD-001
title: Governance Vault Generator Architecture
version: 0.1.0
status: Draft
type: Manual
document-category: Operations
jurisdiction: International
chapter: Global
governance-level: Administrative
effective-date:
last-reviewed: 2026-06-29
next-review-date: 2027-06-29
review-cycle: Annual
approved-by:
authority-level: Administrative
scriptural-foundation:
confessional-foundation:
related-documents:
  - "[[Repository README Draft]]"
  - "[[Source Folder and Markdown Standards]]"
  - "[[Build Script Procedure]]"
  - "[[Jinja2 Template Standards]]"
  - "[[Obsidian Import and Review Guide]]"
  - "[[Master Release Plan]]"
supersedes:
dependencies:
  - "[[Repository README Draft]]"
  - "[[Master Release Plan]]"
tags:
  - build-system
  - generator
  - obsidian
  - documentation
  - operations
---

# Governance Vault Generator Architecture

## 1. Purpose

This document describes the intended architecture for the Christian Community Transformation Society governance vault generator.

The generator exists to reduce mental load by allowing the Society to maintain one set of Markdown source documents and produce usable outputs for Obsidian, PDF, DOCX, HTML, registries, and release packages.

---

# 2. Governing Principle

The source Markdown files are the source of truth.

Generated outputs are useful, but they are not the master documents. If a correction is needed, edit `source/`, then rebuild.

---

# 3. Recommended Repository Structure

```text
ccts-governance-vault/
├── README.md
├── pyproject.toml
├── build.py
├── Makefile
├── source/
│   ├── 00 Home/
│   ├── 01 International Governance/
│   ├── 02 Theology/
│   ├── 03 Board Governance/
│   ├── 04 Membership/
│   ├── 05 Theological Oversight/
│   ├── 06 Church Advisory/
│   ├── 07 Stewardship Advisors/
│   ├── 08 Mission Alignment/
│   ├── 09 Reporting/
│   ├── 10 Chaplaincy/
│   ├── 11 Housing/
│   ├── 12 Operations/
│   ├── 13 Strategy/
│   ├── 14 National Chapters/
│   ├── 15 Risk Management/
│   ├── 16 Finance/
│   ├── 17 Human Resources/
│   ├── 18 Safeguarding/
│   ├── 19 Communications/
│   ├── 20 Legal Readiness/
│   ├── 90 Institutional Memory/
│   ├── 91 Templates/
│   ├── 92 Audit/
│   └── 93 Release/
├── templates/
│   ├── document.md.j2
│   ├── index.md.j2
│   ├── registry.md.j2
│   └── report.md.j2
├── dist/
│   ├── obsidian-vault/
│   ├── pdf/
│   ├── docx/
│   └── html/
└── scripts/
    ├── validate_yaml.py
    ├── check_links.py
    ├── build_pdf.py
    └── build_docx.py
```

---

# 4. Build Flow

The generator should follow this sequence:

1. discover all Markdown files recursively under `source/`;
2. read YAML frontmatter;
3. validate required metadata;
4. collect document IDs, titles, tags, related documents, dependencies, and review dates;
5. copy or render files into an Obsidian vault structure;
6. generate dashboards and registries where configured;
7. generate PDF, DOCX, and HTML outputs where configured;
8. write build reports and warnings;
9. preserve source file paths and document IDs.

---

# 5. Document Discovery

The generator should discover:

```text
source/**/*.md
```

It should ignore:

- generated output folders;
- temporary files;
- `.DS_Store`;
- editor backup files;
- files outside `source/` unless explicitly configured.

---

# 6. Metadata Extraction

The generator should parse YAML frontmatter from each Markdown document.

Key metadata includes:

- `document-id`;
- `title`;
- `version`;
- `status`;
- `type`;
- `document-category`;
- `jurisdiction`;
- `chapter`;
- `governance-level`;
- `review-cycle`;
- `authority-level`;
- `related-documents`;
- `dependencies`;
- `tags`.

---

# 7. Validation Responsibilities

The generator should warn about:

- missing YAML;
- invalid YAML;
- duplicate document IDs;
- duplicate titles;
- missing required fields;
- broken wiki-links;
- missing dependencies;
- invalid statuses;
- invalid document types;
- invalid categories;
- review dates in the past;
- scriptural or confessional foundation fields filled where manual review is needed.

The generator should not silently hide errors.

---

# 8. Obsidian Output

The Obsidian output should preserve folder structure and Markdown links.

Recommended output:

```text
dist/obsidian-vault/
```

The generated vault should include:

- all source documents;
- dashboards;
- registries;
- templates;
- audit reports where generated;
- build report.

---

# 9. PDF and DOCX Output

PDF and DOCX outputs may be generated for:

- individual documents;
- document groups;
- full governance manual;
- board review package;
- legal review package;
- theological review package;
- public release package.

PDF/DOCX outputs should include title, metadata, body, and footer/version information where possible.

---

# 10. HTML Output

HTML output may be used for:

- internal review site;
- static governance reference;
- link checking;
- public selected documents.

Confidential or internal-only documents should not be published publicly without review.

---

# 11. Build Reports

The generator should create build reports such as:

- `build-report.md`;
- `missing-links.md`;
- `metadata-warnings.md`;
- `duplicate-documents.md`;
- `release-summary.md`.

These reports should help the Society correct source documents.

---

# 12. Recommended Commands

```bash
python build.py
python scripts/validate_yaml.py
python scripts/check_links.py
make build
make audit
make release
```

Use whichever commands exist in the repository.

---

# 13. Review

This architecture should be reviewed whenever the generator workflow changes.
