---
document-id: BUILD-021
title: Backup Restore and Portability Guide
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
  - "[[Repository Bootstrap Guide]]"
  - "[[Records Management Policy]]"
  - "[[Master Release Plan]]"
  - "[[Governance Vault Implementation Checklist]]"
supersedes:
dependencies:
  - "[[Records Management Policy]]"
tags:
  - backup
  - restore
  - portability
  - records
  - guide
---

# Backup Restore and Portability Guide

## 1. Purpose

This guide explains how to back up, restore, and move the governance vault repository.

It protects the Society from losing institutional memory because of device failure, accidental deletion, or a single-person workflow.

---

# 2. Governing Principle

The Society should be able to rebuild the governance vault from source.

Backups should protect source files, generator code, templates, registry records, release notes, and package history.

---

# 3. What Must Be Backed Up

Back up:

- `source/`;
- `templates/`;
- `scripts/`;
- `ccts_generator/`;
- `config/`;
- `tests/`;
- `README.md`;
- `pyproject.toml`;
- `requirements.txt`;
- `requirements-dev.txt`;
- release ZIPs;
- audit reports;
- package ZIP archive where practical.

Generated `dist/` can be rebuilt, but release snapshots may still be archived.

---

# 4. Recommended Backup Methods

Use at least two of:

- Git repository;
- external drive;
- encrypted cloud storage approved by the Society;
- ZIP release archive;
- Obsidian Sync for working vault if approved;
- periodic exported release package.

---

# 5. Restore Steps

To restore on a new computer:

1. copy or clone repository;
2. install Python;
3. create virtual environment;
4. install dependencies;
5. run `python build.py`;
6. open `dist/obsidian-vault/` in Obsidian;
7. check build reports;
8. confirm latest release tag or changelog.

---

# 6. Portable ZIP Restore

If restoring from ZIP:

1. unzip repository package;
2. confirm `source/` exists;
3. confirm generator files exist;
4. run setup script;
5. run build;
6. review reports.

---

# 7. What Not to Rely On

Do not rely only on:

- chat history;
- one laptop;
- generated PDF only;
- generated DOCX only;
- Obsidian vault without source;
- memory of which packages were merged;
- uncommitted local edits.

---

# 8. Backup Review Schedule

Recommended:

| Backup Type | Frequency |
|---|---|
| Git commit | After each logical change |
| Release ZIP | Each release |
| External backup | Monthly during active build |
| Restore test | Quarterly or before major review |
| Package archive review | Each release |

---

# 9. Review

This guide should be reviewed annually and after any restore, migration, or data-loss concern.
