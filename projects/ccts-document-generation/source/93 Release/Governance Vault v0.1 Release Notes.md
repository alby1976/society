---
document-id: RELEASE-001
title: Governance Vault v0.1 Release Notes
version: 0.1.0
status: Draft
type: Report
document-category: Governance
jurisdiction: International
chapter: Global
governance-level: Administrative
effective-date:
last-reviewed: 2026-06-29
next-review-date: 2027-06-29
review-cycle: Release
approved-by:
authority-level: Administrative
scriptural-foundation:
confessional-foundation:
related-documents:
  - "[[Master Release Plan]]"
  - "[[Master Changelog]]"
  - "[[Master Document Registry]]"
  - "[[Final Governance Readiness Report]]"
  - "[[Governance Vault Implementation Checklist]]"
  - "[[Package Inventory and Merge Order]]"
supersedes:
dependencies:
  - "[[Master Release Plan]]"
  - "[[Master Changelog]]"
tags:
  - release
  - release-notes
  - governance-vault
  - v0-1
  - institutional-memory
---

# Governance Vault v0.1 Release Notes

## 1. Release Summary

This release establishes the first broad draft of the Christian Community Transformation Society governance vault.

The v0.1 release is a founding governance draft. It is intended for review, refinement, legal assessment, theological review, board consideration, and continued source-controlled development.

This release should not be treated as final legal bylaws, final charity documents, or formally adopted policy unless the proper approving authority later adopts specific documents.

---

# 2. Release Name

Suggested release name:

```text
v0.1-governance-draft
```

Suggested Git tag:

```bash
git tag -a v0.1-governance-draft -m "CCTS governance vault v0.1 draft"
git push origin v0.1-governance-draft
```

---

# 3. Release Purpose

This release exists to:

- preserve the founding governance architecture;
- reduce mental load through an Obsidian-compatible vault;
- maintain source Markdown files as the source of truth;
- support generated PDF, DOCX, HTML, and dashboard outputs;
- prepare for legal, theological, board, and operational review;
- make future changes traceable;
- protect institutional memory from being lost in chat history.

---

# 4. Major Additions

This release includes draft documents for:

- theology and mission;
- international constitution and governance;
- board governance;
- membership;
- Theological Oversight Council;
- Church Advisory Fellowship;
- Stewardship Advisors;
- Mission Alignment Review;
- 5-15 reporting system;
- chaplaincy;
- housing;
- worker cooperative;
- Church Support Foundation;
- national chapters;
- Canada starter documents;
- Hong Kong starter documents;
- founding roadmap;
- operations;
- risk management;
- finance;
- human resources;
- safeguarding and privacy;
- communications;
- legal readiness;
- templates;
- master registries;
- final audit tools.

---

# 5. Source of Truth

The source of truth is:

```text
source/
```

Generated output folders such as `dist/`, generated Obsidian vaults, PDFs, DOCX files, and HTML exports are outputs and should not be edited as master copies.

---

# 6. Important Metadata Rule

This release adopts the following metadata rule:

`scriptural-foundation` and `confessional-foundation` should be populated only when those references directly provide the foundation for that specific document.

These fields should remain blank in ordinary operational, registry, legal-readiness, and administrative documents unless a specific Scripture passage or confessional standard directly grounds that document.

---

# 7. Release Status

| Area | Status | Notes |
|---|---|---|
| Governance architecture | Draft | Broad structure generated |
| Theological identity | Draft | Requires theological review |
| Legal readiness | Draft | Requires qualified legal review |
| National chapters | Draft | Canada and Hong Kong starter sets included |
| Ministry frameworks | Draft | Chaplaincy, housing, cooperative, and Foundation included |
| Reporting | Draft | 5-15 system included |
| Registries | Draft | Master registries added |
| Audit tools | Draft | Final audit documents added |
| Build scripts | Existing / To Confirm | Confirm generator build process in repository |
| Formal adoption | Not adopted | Requires proper approving authority |

---

# 8. Known Issues

Known issues for v0.1:

- Some links may point to documents planned but not yet created.
- Some document IDs may need final normalization.
- Legal readiness documents are governance tools, not legal advice.
- Theological documents require formal theological review.
- Some policy names may need consolidation after link audit.
- Some registry rows may need reconciliation with actual merged source files.
- Some documents may overlap and should be merged after review.
- Local jurisdiction documents require qualified local review.
- Confidentiality labels may need strengthening before operational use.

---

# 9. Required Reviews

Before formal adoption, the following reviews are recommended:

| Review Type | Required For |
|---|---|
| Theological review | Statement of Faith, theological oversight, chaplaincy, church advisory, prayer documents |
| Legal review | Constitution, bylaws, charity, chapter, housing, grants, employment, privacy, safeguarding, cooperative, fundraising |
| Board review | Authority, reserved powers, finance, risk, HR, reporting, chapters |
| Church advisory review | Church relationships, chaplaincy, referrals, seminary recognition |
| Finance review | restricted funds, grants, budget, expense controls |
| Safeguarding review | vulnerable persons, reporting, privacy, incident response |
| Technical review | generator, links, YAML, registry, output files |

---

# 10. Recommended Next Release

Suggested next release:

```text
v0.2-review-cleanup
```

Purpose:

- merge all source packages;
- run link audit;
- resolve duplicate titles;
- normalize YAML;
- update master registry;
- complete final readiness report;
- prepare board/legal/theological review package.

---

# 11. Release Decision

| Field | Response |
|---|---|
| Release Recommendation | Release as draft with known issues |
| Formal Adoption? | No |
| Suitable for Obsidian Review? | Yes |
| Suitable for Legal Filing? | No |
| Suitable for Board Review? | Yes, after audit |
| Suitable for Public Release? | Limited, only selected public documents after review |

---

# 12. Release Approval Record

| Role | Name | Date |
|---|---|---|
| Prepared By |  |  |
| Reviewed By |  |  |
| Approved for Draft Release By |  |  |
| Release Date |  |  |
