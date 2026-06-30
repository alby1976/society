---
document-id: BUILD-011
title: Export Package Configuration
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
  - "[[PDF DOCX and HTML Export Guide]]"
  - "[[Board Legal and Theological Review Package Procedure]]"
  - "[[Public Document Export Policy]]"
  - "[[Master Release Plan]]"
supersedes:
dependencies:
  - "[[PDF DOCX and HTML Export Guide]]"
tags:
  - build-system
  - exports
  - configuration
  - review-packages
  - standard
---

# Export Package Configuration

## 1. Purpose

This standard defines how export packages should be configured for board, legal, theological, public, and ministry review.

The goal is to avoid manually selecting documents every time.

---

# 2. Configuration Principle

A review package should be defined by purpose, not by memory.

If a package is needed more than once, it should have a configuration file.

---

# 3. Recommended Configuration File

Use:

```text
export_packages.yml
```

Example:

```yaml
packages:
  board-review:
    title: Board Review Package
    confidentiality: Internal
    include_categories:
      - Governance
      - Operations
      - Finance
      - Risk Management
    exclude_statuses:
      - Archived
    output_formats:
      - markdown
      - html
      - pdf
      - docx

  theological-review:
    title: Theological Review Package
    confidentiality: Internal
    include_categories:
      - Theology
      - Ministry
    include_tags:
      - chaplaincy
      - church-advisory
      - prayer
    output_formats:
      - markdown
      - pdf
      - docx
```

---

# 4. Package Fields

| Field | Meaning |
|---|---|
| `title` | Display name for package |
| `confidentiality` | Public, Internal, Restricted, Confidential, Board Confidential |
| `include_categories` | Document categories to include |
| `include_tags` | Tags to include |
| `include_documents` | Exact document IDs or titles to include |
| `exclude_documents` | Exact document IDs or titles to exclude |
| `exclude_statuses` | Draft, Archived, Superseded, etc. |
| `output_formats` | markdown, html, pdf, docx, zip |
| `review_instructions` | Short text for reviewers |

---

# 5. Standard Packages

Recommended initial packages:

| Package Key | Purpose |
|---|---|
| `board-review` | Board governance and policy review |
| `legal-review` | Legal readiness and high-risk legal documents |
| `theological-review` | Theology, church advisory, chaplaincy, prayer |
| `finance-review` | Finance, Foundation, restricted funds, grants |
| `safeguarding-review` | Safeguarding, privacy, vulnerable persons, incident response |
| `chapter-review` | National Chapter and expansion documents |
| `public-candidate` | Documents being considered for public release |

---

# 6. Public Candidate Package

Public candidate does not mean public approved.

A public candidate package should be reviewed before publication.

Possible public candidate documents:

- mission statement;
- vision statement;
- core values;
- statement of faith if approved;
- selected public overview documents;
- public annual report if approved;
- selected ministry descriptions.

---

# 7. Legal Review Package

Legal review may include:

- constitution;
- bylaws if created;
- national chapter framework;
- legal readiness framework;
- housing;
- Foundation grants;
- finance;
- privacy;
- safeguarding;
- HR;
- communications;
- public fundraising language.

---

# 8. Theological Review Package

Theological review may include:

- statement of faith;
- mission;
- vision;
- core values;
- theological oversight;
- church advisory;
- chaplaincy;
- prayer;
- annual day of prayer;
- church referral;
- seminary recognition.

---

# 9. Board Review Package

Board review may include:

- international constitution;
- governance framework;
- reserved powers;
- delegated authority;
- board charter;
- membership;
- mission alignment;
- reporting;
- finance;
- risk;
- HR;
- safeguarding;
- communications;
- roadmap.

---

# 10. Review

This configuration standard should be reviewed whenever export packages change.
