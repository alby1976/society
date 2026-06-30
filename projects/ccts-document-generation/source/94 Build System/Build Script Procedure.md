---
document-id: BUILD-003
title: Build Script Procedure
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
  - "[[Governance Vault Generator Architecture]]"
  - "[[Source Folder and Markdown Standards]]"
  - "[[Master Release Plan]]"
  - "[[Governance Vault Implementation Checklist]]"
  - "[[Final Governance Vault Audit Framework]]"
supersedes:
dependencies:
  - "[[Governance Vault Generator Architecture]]"
tags:
  - build-system
  - build-script
  - procedure
  - python
  - release
---

# Build Script Procedure

## 1. Purpose

This procedure explains how to run and review the governance vault build process.

The build process turns `source/` Markdown documents into reviewable outputs such as an Obsidian vault, PDF, DOCX, HTML, registries, and build reports.

---

# 2. Build Principle

Builds should be repeatable.

A future leader should be able to clone the repository, install dependencies, run the build, and reproduce the governance vault.

---

# 3. Before Running Build

Confirm:

- [ ] all desired package `source/` folders have been merged;
- [ ] repository is saved or committed;
- [ ] Python environment is active;
- [ ] dependencies are installed;
- [ ] `source/` exists;
- [ ] build scripts exist;
- [ ] templates exist if required;
- [ ] no one is editing generated output as source.

---

# 4. Install Dependencies

Suggested commands:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

On macOS or Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If using `pyproject.toml`:

```bash
pip install -e .
```

---

# 5. Run Build

Typical command:

```bash
python build.py
```

Optional commands if supported:

```bash
make build
make audit
make release
```

---

# 6. Expected Outputs

A successful build may create:

```text
dist/
├── obsidian-vault/
├── pdf/
├── docx/
├── html/
└── reports/
```

Exact output depends on the generator.

---

# 7. Review Build Report

After build, review:

- missing YAML;
- invalid YAML;
- duplicate IDs;
- duplicate titles;
- broken links;
- missing dependencies;
- invalid metadata values;
- failed PDF/DOCX exports;
- skipped documents;
- warnings about review dates.

Do not ignore build warnings just because files were produced.

---

# 8. Common Build Problems

| Problem | Likely Cause | Action |
|---|---|---|
| Missing document | Source folder not merged | Merge source package |
| Broken link | Document title changed or missing | Fix link in source |
| Duplicate ID | Two documents use same ID | Assign unique ID |
| Invalid YAML | YAML syntax error | Fix frontmatter |
| PDF failed | Converter or dependency missing | Check PDF tool setup |
| DOCX failed | Converter or template missing | Check DOCX tool setup |
| Empty registry | Metadata not parsed | Check YAML frontmatter |

---

# 9. After Build

After a successful build:

- [ ] open generated Obsidian vault;
- [ ] review dashboard;
- [ ] check master registry;
- [ ] review build warnings;
- [ ] run audit checklists;
- [ ] commit source changes;
- [ ] tag release if ready.

---

# 10. Do Not Edit Generated Output

If an output document has an error:

1. find the source file under `source/`;
2. edit the source file;
3. rebuild;
4. verify output.

---

# 11. Build Log

Use this table to record builds.

| Build Date | Version / Branch | Command Used | Result | Notes |
|---|---|---|---|---|
|  |  |  | Success / Failed / Warnings |  |

---

# 12. Review

This procedure should be reviewed whenever build scripts, dependencies, templates, or output formats change.
