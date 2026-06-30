---
document-id: BUILD-015
title: Pytest Validation Suite Guide
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
  - "[[Testing and Quality Assurance Guide]]"
  - "[[Metadata Schema Reference]]"
  - "[[Build Script Procedure]]"
  - "[[GitHub Actions Build and Audit Workflow]]"
supersedes:
dependencies:
  - "[[Testing and Quality Assurance Guide]]"
tags:
  - pytest
  - validation
  - testing
  - build-system
  - guide
---

# Pytest Validation Suite Guide

## 1. Purpose

This guide explains how the pytest suite should be used to test the CCTS governance vault generator.

---

# 2. Install Test Dependencies

Install pytest:

```bash
pip install pytest pytest-cov
```

Or add to `requirements-dev.txt`:

```text
pytest>=8.0.0
pytest-cov>=5.0.0
```

---

# 3. Run Tests

Run all tests:

```bash
pytest
```

Run verbose:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_parser.py
```

Run coverage:

```bash
pytest --cov=ccts_generator --cov-report=term-missing
```

---

# 4. Test Categories

Parser tests confirm that Markdown and YAML are parsed properly.

Validator tests confirm that required fields, duplicate IDs, and allowed values are checked.

Link tests confirm that Obsidian links are identified and missing links are reported.

Build smoke tests confirm that a small sample vault builds successfully.

Export tests confirm review package selection and output generation.

---

# 5. Fixture Design

Fixtures should be small and readable.

Use fixtures for valid YAML, missing YAML, duplicate IDs, duplicate titles, valid links, missing links, and sample registry output.

---

# 6. Test Failure Response

When tests fail:

1. read the error;
2. identify whether source, script, or test is wrong;
3. fix the smallest cause;
4. rerun tests;
5. commit the fix.

Do not change tests merely to silence real problems.

---

# 7. CI Use

The GitHub Actions workflow should run:

```bash
pytest
```

before build and audit steps.

---

# 8. Review

This guide should be reviewed whenever the test suite changes.
