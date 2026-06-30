---
document-id: BUILD-018
title: Repository Bootstrap Guide
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
  - "[[Source Folder and Markdown Standards]]"
  - "[[Build Script Procedure]]"
  - "[[Local Development Environment Guide]]"
  - "[[Backup Restore and Portability Guide]]"
supersedes:
dependencies:
  - "[[Governance Vault Generator Architecture]]"
tags:
  - repository
  - bootstrap
  - build-system
  - setup
  - guide
---

# Repository Bootstrap Guide

## 1. Purpose

This guide explains how to create a clean local repository for the Christian Community Transformation Society governance vault.

The goal is to make the project reproducible, portable, and easy to rebuild from downloaded packages.

---

# 2. Governing Principle

The repository should be simple enough to restore and structured enough to preserve institutional memory.

The Society should be able to rebuild the vault from source without depending on a single computer, chat thread, or person's memory.

---

# 3. Recommended Repository Name

Suggested repository name:

```text
ccts-governance-vault
```

Suggested local folder:

```text
C:\Projects\ccts-governance-vault
```

or:

```text
~/Projects/ccts-governance-vault
```

---

# 4. Bootstrap Steps

1. Create repository folder.
2. Copy generator source code into the folder.
3. Copy automation scripts into the folder.
4. Copy export templates into the folder.
5. Copy QA files into the folder.
6. Put downloaded governance package ZIPs into `packages/`.
7. Run package merge script.
8. Run build.
9. Open generated Obsidian vault.
10. Commit source files to Git.

---

# 5. One-Command Bootstrap

After copying this package into the project root, run:

```bash
python scripts/bootstrap_repo.py
```

On Windows, use:

```powershell
python scripts\bootstrap_repo.py
```

The script creates standard folders, placeholder files, and a setup report.

---

# 6. Folder Structure Created

```text
.
├── source/
├── templates/
├── scripts/
├── packages/
├── dist/
├── docs/
├── config/
├── tests/
└── .github/
```

---

# 7. What Belongs in Each Folder

| Folder | Purpose |
|---|---|
| `source/` | Markdown source documents |
| `templates/` | Jinja2 export templates |
| `scripts/` | Build, merge, audit, release scripts |
| `packages/` | Downloaded package ZIPs before merge |
| `dist/` | Generated outputs |
| `docs/` | Repository notes and helper documentation |
| `config/` | Build and export configuration |
| `tests/` | Automated tests |
| `.github/` | GitHub Actions workflows |

---

# 8. Git Setup

Run:

```bash
git init
git add .
git commit -m "Initialize CCTS governance vault repository"
```

After merging all source packages:

```bash
git add source templates scripts config tests README.md
git commit -m "Add CCTS governance vault source and generator workflow"
```

---

# 9. First Build

Run:

```bash
python build.py
```

or:

```bash
python scripts/build_all.py
```

Then open:

```text
dist/obsidian-vault/
```

in Obsidian.

---

# 10. Review

This guide should be reviewed whenever the repository setup process changes.
