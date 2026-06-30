---
document-id: BUILD-010
title: PDF DOCX and HTML Export Guide
version: 0.1.0
status: Draft
type: Guide
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
  - "[[Governance Vault Generator Architecture]]"
  - "[[Build Script Procedure]]"
  - "[[Export Package Configuration]]"
  - "[[Board Legal and Theological Review Package Procedure]]"
  - "[[Public Document Export Policy]]"
supersedes:
dependencies:
  - "[[Governance Vault Generator Architecture]]"
  - "[[Build Script Procedure]]"
tags:
  - build-system
  - exports
  - pdf
  - docx
  - html
---

# PDF DOCX and HTML Export Guide

## 1. Purpose

This guide explains how the governance vault generator should create PDF, DOCX, and HTML outputs from Markdown source documents.

Exports are useful for board review, legal review, theological review, public release, printing, archiving, and sharing with people who do not use Obsidian.

---

# 2. Governing Principle

Exports are outputs, not the source of truth.

If an exported PDF, DOCX, or HTML file contains an error, correct the Markdown source file and rebuild the export.

---

# 3. Output Folders

Recommended output folders:

```text
dist/
├── obsidian-vault/
├── html/
├── pdf/
├── docx/
├── review-packages/
└── reports/
```

---

# 4. Export Types

| Export Type | Purpose |
|---|---|
| Obsidian Vault | Internal navigation, review, graph view, backlinks |
| HTML | Browser review and static internal site |
| PDF | Stable reading, board packets, archive snapshots |
| DOCX | Editable review by Word users |
| Markdown Bundle | Review package source copy |
| ZIP Release | Portable release archive |

---

# 5. Individual Document Exports

Each Markdown document may be exported to:

- one HTML file;
- one PDF file;
- one DOCX file.

The output should preserve:

- title;
- document ID;
- version;
- status;
- review date;
- authority level;
- body content.

---

# 6. Bundle Exports

Bundle exports combine multiple documents into one package.

Possible bundles:

- Board Review Package;
- Legal Review Package;
- Theological Review Package;
- Public Document Package;
- National Chapter Review Package;
- Housing Review Package;
- Foundation Review Package;
- Safeguarding Review Package.

---

# 7. Export Metadata

Each export should include:

- release name;
- generation date;
- source repository if known;
- document count;
- included categories;
- confidentiality note;
- review status;
- source-of-truth warning.

Example warning:

```text
This file is a generated output. The Markdown source file in source/ remains the source of truth.
```

---

# 8. Confidentiality

Before exporting documents, review confidentiality.

Do not include confidential, board confidential, legal privileged, safeguarding, personnel, resident, donor, or private records in broad review packages unless authorized.

Public exports require extra review.

---

# 9. Review Packages

Review packages should include:

- package index;
- selected documents;
- generated registry;
- known issues;
- review instructions;
- feedback form if needed.

---

# 10. Export Commands

Suggested commands:

```bash
python scripts/build_review_packages.py
python scripts/export_selected.py --package board-review
python scripts/export_selected.py --package legal-review
python scripts/export_selected.py --package theological-review
```

---

# 11. Export Failure

If export fails:

- confirm dependencies are installed;
- check Markdown syntax;
- check file names;
- check output permissions;
- review build report;
- correct source and rebuild.

---

# 12. Review

This guide should be reviewed whenever export formats, templates, or review package processes change.
