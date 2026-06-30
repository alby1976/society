---
document-id: BUILD-016
title: Metadata Schema Reference
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
  - "[[Source Folder and Markdown Standards]]"
  - "[[YAML Metadata Audit Checklist]]"
  - "[[Testing and Quality Assurance Guide]]"
supersedes:
dependencies:
  - "[[Source Folder and Markdown Standards]]"
tags:
  - metadata
  - schema
  - yaml
  - standard
  - build-system
---

# Metadata Schema Reference

## 1. Purpose

This reference defines the standard YAML metadata schema used in the governance vault.

---

# 2. Required Fields

| Field | Required? | Notes |
|---|---|---|
| `document-id` | Yes | Stable unique ID |
| `title` | Yes | Human-readable title |
| `version` | Yes | Semantic or release version |
| `status` | Yes | Draft, Proposed, Active, Archived, Superseded |
| `type` | Yes | Policy, Procedure, Framework, etc. |
| `document-category` | Yes | Governance, Theology, Operations, etc. |
| `jurisdiction` | Yes | International, Canada, Hong Kong, etc. |
| `chapter` | Yes | Global, Canada, Hong Kong, etc. |
| `governance-level` | Yes | International, National Chapter, Board, Administrative, etc. |
| `effective-date` | Optional | Blank until adopted |
| `last-reviewed` | Yes | Date last reviewed |
| `next-review-date` | Yes | Date next review is due |
| `review-cycle` | Yes | Annual, Quarterly, Monthly, Release, etc. |
| `approved-by` | Optional | Blank until approved |
| `authority-level` | Yes | Board, International Board, Administrative, etc. |
| `scriptural-foundation` | Optional | Use only when directly foundational |
| `confessional-foundation` | Optional | Use only when directly foundational |
| `related-documents` | Optional | Obsidian wiki-links |
| `supersedes` | Optional | Prior document replaced |
| `dependencies` | Optional | Documents required first |
| `tags` | Yes | Filtering and navigation |

---

# 3. Approved Status Values

- Draft
- Proposed
- Active
- Archived
- Superseded

---

# 4. Approved Type Values

- Policy
- Procedure
- Framework
- Charter
- Manual
- Bylaw
- Constitution
- Report
- Guideline
- Form
- Template
- Register
- Checklist
- Plan
- Standard
- Commentary
- Guide

---

# 5. Approved Category Values

- Governance
- Theology
- Ministry
- Operations
- Finance
- Housing
- Cooperative
- Human Resources
- Risk Management
- Communications
- Legal Readiness

---

# 6. Foundation Fields Rule

Use `scriptural-foundation` and `confessional-foundation` only when the references directly ground the specific document.

Do not fill these fields merely because a document is Christian, Reformed, or organizationally important.

---

# 7. Review

This schema should be reviewed whenever metadata standards change.
