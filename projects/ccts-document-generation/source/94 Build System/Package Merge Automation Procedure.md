---
document-id: BUILD-007
title: Package Merge Automation Procedure
version: 0.1.0
status: Draft
type: Procedure
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
  - "[[Automated Build Scripts Guide]]"
  - "[[Package Inventory and Merge Order]]"
  - "[[Governance Vault Implementation Checklist]]"
  - "[[Registry Maintenance Procedure]]"
supersedes:
dependencies:
  - "[[Package Inventory and Merge Order]]"
tags:
  - build-system
  - package-merge
  - automation
  - procedure
  - source
---

# Package Merge Automation Procedure

## 1. Purpose

This procedure explains how to merge downloaded governance packages into the main repository using automation.

The goal is to avoid manually opening dozens of ZIP files and copying files one by one.

---

# 2. Folder Setup

Create a folder named:

```text
packages/
```

Put downloaded package ZIP files into that folder.

Example:

```text
packages/
├── CCTS_Package_1A_Definitions_Dashboard_Registry.zip
├── CCTS_GOV_01_International_Constitution.zip
├── CCTS_RELEASE_01_v0_1_Release_Implementation.zip
└── ...
```

---

# 3. Merge Command

Run:

```bash
python scripts/merge_packages.py packages/
```

The script should:

- open each ZIP;
- find files under each package's `source/` folder;
- copy those files into repository `source/`;
- preserve folder structure;
- avoid overwriting files unless `--overwrite` is provided;
- write a merge report.

---

# 4. Safe Merge Rules

Default behavior should be cautious.

- Do not overwrite existing files by default.
- Record skipped files.
- Record copied files.
- Preserve registry update documents.
- Preserve package order where possible.
- Use `--overwrite` only when intentionally replacing old files.

---

# 5. Merge Report

The merge report should be written to:

```text
dist/reports/package-merge-report.md
```

The report should include:

- packages found;
- files copied;
- files skipped;
- conflicts;
- errors;
- next steps.

---

# 6. After Merge

After merge:

```bash
python scripts/build_all.py
```

Then review:

- `dist/reports/build-report.md`;
- `dist/reports/missing-links.md`;
- generated Obsidian vault;
- master registry;
- changelog.

---

# 7. Review

This procedure should be reviewed whenever package structure or merge scripts change.
