---
document-id: BUILD-002
title: Source Folder and Markdown Standards
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
  - "[[YAML Metadata Audit Checklist]]"
  - "[[Missing Link and Dependency Review Checklist]]"
  - "[[Registry Maintenance Procedure]]"
supersedes:
dependencies:
  - "[[Governance Vault Generator Architecture]]"
tags:
  - markdown
  - source-folder
  - standards
  - build-system
  - obsidian
---

# Source Folder and Markdown Standards

## 1. Purpose

This standard defines how Markdown source files should be written, named, organized, and maintained in the governance vault.

The goal is to keep the vault readable by humans and usable by the generator.

---

# 2. Source of Truth

All editable governance content belongs in:

```text
source/
```

Do not edit generated output as the master copy.

---

# 3. Folder Naming

Folders should be numbered and named clearly.

Recommended pattern:

```text
00 Home
01 International Governance
02 Theology
03 Board Governance
...
90 Institutional Memory
91 Templates
92 Audit
93 Release
```

Numbered folders help preserve order in file browsers and Obsidian.

---

# 4. File Naming

File names should:

- match the document title where practical;
- avoid cryptic abbreviations;
- avoid `final`, `final-final`, or `new`;
- use `.md`;
- avoid dates unless the document is a dated report;
- avoid duplicate note titles.

Good:

```text
Mission Alignment Review.md
Leadership Health and Workload Policy.md
```

Avoid:

```text
policy-final-new.md
misc governance stuff.md
```

---

# 5. Markdown Structure

Documents should normally use:

- YAML frontmatter;
- H1 title;
- numbered sections;
- tables where helpful;
- Obsidian wiki-links;
- clear review section;
- short paragraphs.

Example:

```markdown
---
document-id: EXAMPLE-001
title: Example Policy
...
---

# Example Policy

## 1. Purpose

## 2. Governing Principle

## 3. Scope

## 4. Policy

## 5. Review
```

---

# 6. YAML Required Fields

Every official source document should include:

```yaml
document-id:
title:
version:
status:
type:
document-category:
jurisdiction:
chapter:
governance-level:
effective-date:
last-reviewed:
next-review-date:
review-cycle:
approved-by:
authority-level:
scriptural-foundation:
confessional-foundation:
related-documents:
supersedes:
dependencies:
tags:
```

---

# 7. Scriptural and Confessional Foundation Rule

Use these fields only when directly foundational:

```yaml
scriptural-foundation:
confessional-foundation:
```

Leave them blank for ordinary operational, registry, legal-readiness, administrative, template, audit, release, or process documents unless specific references directly ground that document.

---

# 8. Wiki-Link Standards

Use Obsidian wiki-links for internal links:

```markdown
[[Mission Alignment Review]]
[[National Chapter Framework]]
```

Avoid raw relative links for internal governance documents unless the generator requires them.

---

# 9. Tables

Use Markdown tables for:

- checklists;
- registers;
- decision records;
- roles;
- review ratings;
- approval records.

Keep tables readable and avoid overly wide tables where possible.

---

# 10. Tags

Tags should be:

- lowercase;
- hyphenated;
- useful;
- limited;
- consistent.

Example:

```yaml
tags:
  - governance
  - mission-alignment
  - review
```

---

# 11. Document Status

Use consistent statuses:

- Draft;
- Proposed;
- Active;
- Superseded;
- Archived.

Do not mark a document Active unless formally adopted.

---

# 12. Review Dates

Use dates consistently, preferably:

```text
YYYY-MM-DD
```

Blank dates may be used only when unknown or intentionally pending.

---

# 13. Templates

Templates should be stored in:

```text
source/91 Templates/
```

Templates should be clearly marked as `type: Template` or `type: Form`.

---

# 14. Registry Updates

Registry update documents should be stored in:

```text
source/90 Institutional Memory/Registry Updates/
```

Registry update documents preserve package history and should not be deleted casually.

---

# 15. Review

This standard should be reviewed whenever folder structure, metadata, or generator behavior changes.
