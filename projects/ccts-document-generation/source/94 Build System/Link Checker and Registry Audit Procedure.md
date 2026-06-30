---
document-id: BUILD-017
title: Link Checker and Registry Audit Procedure
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
  - "[[Testing and Quality Assurance Guide]]"
  - "[[Missing Link and Dependency Review Checklist]]"
  - "[[Master Document Registry]]"
  - "[[Registry Maintenance Procedure]]"
supersedes:
dependencies:
  - "[[Missing Link and Dependency Review Checklist]]"
tags:
  - link-checker
  - registry-audit
  - testing
  - procedure
  - obsidian
---

# Link Checker and Registry Audit Procedure

## 1. Purpose

This procedure explains how to check Obsidian links and registry consistency using automated scripts and human review.

---

# 2. Link Check Command

Run:

```bash
python scripts/check_links.py
```

The script should produce:

```text
dist/reports/missing-links.md
```

---

# 3. Registry Audit Command

Run:

```bash
python scripts/audit_all.py
```

The script should produce:

```text
dist/reports/audit-summary.md
```

---

# 4. What the Link Checker Should Detect

The link checker should identify links to missing documents, documents with no inbound links, duplicate titles, links to renamed documents, links in YAML fields, and links in document body.

---

# 5. What the Registry Audit Should Detect

The registry audit should identify documents missing from registry, registry entries without source files, duplicate document IDs, duplicate titles, missing review dates, missing status, documents marked Active without approval, and populated foundation fields requiring confirmation.

---

# 6. Manual Review Still Required

The script cannot always know whether a missing link is a document that should be created, a renamed document, a typo, a planned future document, or an obsolete reference.

Use [[Missing Link and Dependency Review Checklist]] to decide.

---

# 7. Cleanup Process

For each issue:

1. identify source file;
2. decide whether to create, rename, remove, or defer;
3. edit source file;
4. rerun link checker;
5. update registry if needed;
6. update changelog if significant.

---

# 8. Review

This procedure should be reviewed whenever link checker or registry scripts change.
