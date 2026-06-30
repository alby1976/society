---
document-id: BUILD-004
title: Jinja2 Template Standards
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
  - "[[Governance Vault Generator Architecture]]"
  - "[[Source Folder and Markdown Standards]]"
  - "[[Build Script Procedure]]"
supersedes:
dependencies:
  - "[[Governance Vault Generator Architecture]]"
tags:
  - jinja2
  - templates
  - build-system
  - standards
  - documentation
---

# Jinja2 Template Standards

## 1. Purpose

This standard explains how Jinja2 templates should be used in the governance vault generator.

Templates help generate consistent indexes, dashboards, registries, reports, PDF front pages, DOCX layouts, and HTML pages.

---

# 2. Governing Principle

Templates should reduce repetition without hiding meaning.

A template should make documents easier to generate and review, not harder to understand or maintain.

---

# 3. Recommended Template Folder

Store templates in:

```text
templates/
```

Possible templates:

```text
templates/
├── document.md.j2
├── index.md.j2
├── registry.md.j2
├── dashboard.md.j2
├── build-report.md.j2
├── pdf-cover.md.j2
├── docx-cover.md.j2
└── html-page.html.j2
```

---

# 4. Template Naming

Template names should describe output purpose.

Good:

```text
registry.md.j2
build-report.md.j2
html-page.html.j2
```

Avoid:

```text
thing.j2
new-template.j2
final.j2
```

---

# 5. Template Inputs

Templates may receive:

- document metadata;
- document body;
- list of documents;
- registry data;
- decision data;
- build warnings;
- folder structure;
- release version;
- generated date;
- review status.

---

# 6. Example Registry Template Logic

```jinja2
# Document Registry

| Document ID | Title | Status | Type | Category |
|---|---|---|---|---|
{% for doc in documents %}
| {{ doc.document_id }} | [[{{ doc.title }}]] | {{ doc.status }} | {{ doc.type }} | {{ doc.category }} |
{% endfor %}
```

---

# 7. Missing Data

Templates should handle missing data gracefully.

Instead of failing silently, the generator should record warnings when required metadata is missing.

Template output may show:

```text
MISSING
```

for required fields during audit builds.

---

# 8. Escaping and Markdown

Templates generating Markdown should avoid breaking table syntax.

Be careful with:

- pipe characters;
- line breaks inside table cells;
- YAML indentation;
- list formatting;
- quotes;
- colons in YAML values.

---

# 9. Separation of Concerns

Templates should not contain complex business logic.

Complex validation should live in Python scripts, not inside templates.

Templates should focus on presentation.

---

# 10. Version Control

Templates should be committed to Git.

Changes to templates should be recorded in [[Master Changelog]] when they affect generated outputs.

---

# 11. Review

This standard should be reviewed whenever templates or generated output formats change.
