---
document-id: BUILD-014
title: Testing and Quality Assurance Guide
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
  - "[[YAML Metadata Audit Checklist]]"
  - "[[Missing Link and Dependency Review Checklist]]"
  - "[[Metadata Schema Reference]]"
  - "[[Pytest Validation Suite Guide]]"
supersedes:
dependencies:
  - "[[Governance Vault Generator Architecture]]"
  - "[[Build Script Procedure]]"
tags:
  - testing
  - qa
  - build-system
  - validation
  - guide
---

# Testing and Quality Assurance Guide

## 1. Purpose

This guide explains how the governance vault generator and source documents should be tested before release.

Testing protects the Society from broken builds, missing metadata, duplicate document IDs, broken Obsidian links, invalid registries, and inconsistent exports.

---

# 2. Governing Principle

Testing should make mistakes visible early.

A governance vault should not depend on memory, guesswork, or manual checking alone. Automated checks should support careful human review.

---

# 3. What Should Be Tested

Testing should cover:

- Markdown discovery;
- YAML parsing;
- required metadata fields;
- duplicate document IDs;
- duplicate titles;
- valid statuses;
- valid document types;
- valid categories;
- Obsidian wiki-links;
- missing dependencies;
- registry generation;
- build report generation;
- export package selection;
- source folder structure;
- review package output;
- release ZIP creation.

---

# 4. Test Types

| Test Type | Purpose |
|---|---|
| Unit tests | Test parser, validators, and link checker functions |
| Integration tests | Test full build from sample source folder |
| Metadata tests | Test YAML required fields and allowed values |
| Link tests | Test missing and resolved Obsidian links |
| Export tests | Test review package creation |
| Smoke tests | Confirm build command runs without crashing |
| Regression tests | Confirm fixed bugs stay fixed |

---

# 5. Recommended Commands

Run:

```bash
pytest
```

Run with coverage if installed:

```bash
pytest --cov=ccts_generator --cov-report=term-missing
```

Run generator checks:

```bash
python scripts/build_all.py
python scripts/audit_all.py
```

---

# 6. Test Folder Structure

Recommended structure:

```text
tests/
├── fixtures/
│   ├── valid_source/
│   └── invalid_source/
├── test_parser.py
├── test_validators.py
├── test_links.py
├── test_build_smoke.py
└── test_export_packages.py
```

---

# 7. CI Integration

GitHub Actions should run tests before build:

```bash
pytest
python build.py
python scripts/validate_yaml.py
python scripts/check_links.py
python scripts/audit_all.py
```

---

# 8. Passing Tests Do Not Equal Approval

Automated tests cannot approve doctrine, law, governance, finances, safeguarding, or public release.

Tests only confirm that the vault structure and generator behavior are working.

Human review remains required.

---

# 9. Review

This guide should be reviewed whenever the generator, metadata schema, or release process changes.
