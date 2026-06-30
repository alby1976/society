---
document-id: BUILD-020
title: Dependency and Tooling Reference
version: 0.1.0
status: Draft
type: Standard
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
  - "[[Local Development Environment Guide]]"
  - "[[Build Script Procedure]]"
  - "[[Testing and Quality Assurance Guide]]"
  - "[[PDF DOCX and HTML Export Guide]]"
supersedes:
dependencies:
  - "[[Local Development Environment Guide]]"
tags:
  - dependencies
  - tooling
  - python
  - build-system
  - standard
---

# Dependency and Tooling Reference

## 1. Purpose

This reference lists recommended tools and Python dependencies for the governance vault generator.

The goal is to make the build environment understandable and reproducible.

---

# 2. Core Python Dependencies

| Package | Purpose |
|---|---|
| PyYAML | Parse YAML frontmatter |
| Jinja2 | Render templates |
| markdown | Convert Markdown to HTML |
| python-docx | Generate DOCX files |
| reportlab | Generate PDF files |
| pytest | Run tests |
| pytest-cov | Test coverage |
| ruff | Optional linting |

---

# 3. Optional Tools

| Tool | Purpose |
|---|---|
| Obsidian | Vault review and navigation |
| Git | Version control |
| GitHub Actions | Automated build and QA |
| VS Code | Editing and Python workflow |
| PyCharm | Python development |
| 7-Zip | ZIP extraction if needed |
| Make | Shortcut commands on supported systems |

---

# 4. Minimum Build

Minimum build requires:

```text
PyYAML
Jinja2
```

Recommended full build requires:

```text
PyYAML
Jinja2
markdown
python-docx
reportlab
pytest
pytest-cov
```

---

# 5. Dependency Files

Recommended dependency files:

```text
requirements.txt
requirements-dev.txt
pyproject.toml
```

---

# 6. Upgrade Caution

Do not upgrade dependencies during a governance release unless needed.

If dependencies are upgraded:

- run tests;
- run build;
- run link check;
- run export checks;
- update changelog if outputs change.

---

# 7. Review

This reference should be reviewed annually or whenever dependencies change.
