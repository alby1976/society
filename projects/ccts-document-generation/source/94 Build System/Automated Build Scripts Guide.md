---
document-id: BUILD-006
title: Automated Build Scripts Guide
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
  - "[[Source Folder and Markdown Standards]]"
  - "[[GitHub Actions Build and Audit Workflow]]"
  - "[[Package Merge Automation Procedure]]"
supersedes:
dependencies:
  - "[[Governance Vault Generator Architecture]]"
  - "[[Build Script Procedure]]"
tags:
  - build-system
  - automation
  - scripts
  - guide
  - ci
---

# Automated Build Scripts Guide

## 1. Purpose

This guide explains the automation scripts used to merge packages, build the governance vault, audit metadata, check links, generate outputs, and prepare release ZIP files.

The scripts exist to reduce repetitive manual work and make the vault reproducible.

---

# 2. Governing Principle

Automation should reduce mental load without hiding what changed.

A script should make repeated steps easier, but the repository should still preserve source files, registry updates, build reports, and release records.

---

# 3. Recommended Automation Commands

| Task | Command |
|---|---|
| Build vault | `python build.py` |
| Validate YAML | `python scripts/validate_yaml.py` |
| Check links | `python scripts/check_links.py` |
| Merge packages | `python scripts/merge_packages.py packages/` |
| Run all checks | `python scripts/build_all.py` |
| Audit all | `python scripts/audit_all.py` |
| Package release | `python scripts/package_release.py` |
| Create new document | `python scripts/new_document.py` |

---

# 4. Windows Commands

PowerShell:

```powershell
.\build.ps1
```

Command Prompt:

```cmd
build.cmd
```

---

# 5. Make Commands

If `make` is available:

```bash
make build
make audit
make release
make clean
```

---

# 6. Package Merge Workflow

1. Put downloaded package ZIP files into `packages/`.
2. Run:

```bash
python scripts/merge_packages.py packages/
```

3. Review copied files.
4. Run:

```bash
python scripts/build_all.py
```

5. Open generated vault in Obsidian.

---

# 7. Build-All Workflow

The build-all script should:

1. validate source folder exists;
2. run the generator;
3. validate YAML;
4. check links;
5. create release ZIP if requested;
6. report warnings clearly.

---

# 8. Audit-All Workflow

The audit-all script should:

1. validate YAML;
2. check links;
3. compare registry references where possible;
4. check duplicate document IDs;
5. check duplicate titles;
6. write audit summary to `dist/reports/audit-summary.md`.

---

# 9. CI Workflow

The GitHub Actions workflow should run on:

- pull requests;
- pushes to main;
- manual dispatch.

It should:

- install Python;
- install dependencies;
- run build;
- run YAML validation;
- run link check;
- upload generated reports as artifacts.

---

# 10. Review

This guide should be reviewed whenever scripts or CI workflows change.
