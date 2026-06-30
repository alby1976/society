---
document-id: GOV-REV-003
title: Document Review Policy
version: 0.1.0
status: Draft
type: Policy
document-category: Governance
jurisdiction: International
chapter: Global
governance-level: Administrative
effective-date:
last-reviewed: 2026-06-28
next-review-date: 2027-06-28
review-cycle: Annual
approved-by:
authority-level: International Board
scriptural-foundation:
  - 1 Corinthians 14:40
  - Proverbs 11:14
  - Luke 1:1-4
confessional-foundation:
  - Westminster Confession of Faith
  - Heidelberg Catechism
  - Belgic Confession
  - Canons of Dort
related-documents:
  - "[[Document Registry]]"
  - "[[Decision Register]]"
  - "[[Governance Review Process]]"
  - "[[Mission Alignment Review]]"
  - "[[Changelog]]"
  - "[[Release Plan]]"
supersedes:
dependencies:
  - "[[Document Registry]]"
  - "[[Decision Register]]"
tags:
  - documents
  - review
  - policy
  - governance
  - registry
---

# Document Review Policy

## 1. Purpose

This policy establishes how official governance documents of the Christian Community Transformation Society are reviewed, revised, approved, superseded, archived, and maintained.

The Society uses generator-ready Markdown as its source of truth for governance documents. This policy protects that source from drift, confusion, duplication, and accidental contradiction.

## 2. Governing Principle

If a document governs people, money, doctrine, mission, property, reports, chapters, or authority, it must be reviewed.

Documents are not sacred because they are old. They are not useless because they are drafts. They are tools, and tools need sharpening.

## 3. Scope

This policy applies to constitutions, bylaws, policies, frameworks, charters, manuals, procedures, standards, templates, registers, dashboards, governance maps, reporting forms, and institutional memory documents.

## 4. Document Metadata

Every official document should include YAML metadata with document-id, title, version, status, type, document-category, jurisdiction, chapter, governance-level, effective-date, last-reviewed, next-review-date, review-cycle, approved-by, authority-level, related-documents, dependencies, and tags.

Missing metadata should be corrected before a document is treated as official.

## 5. Status Values

| Status | Meaning |
|---|---|
| Draft | Under development |
| Proposed | Ready for formal review |
| Active | Approved and governing |
| Superseded | Replaced by another document |
| Archived | Retained for memory |
| Retired | No longer used and not replaced |

A draft should not be treated as binding unless an authority expressly adopts it for interim use.

## 6. Review Frequency

| Document Type | Typical Review Cycle |
|---|---|
| Constitution | Annual during founding, then every 3 years |
| Statement of Faith | Annual during founding, then every 3-5 years |
| Board Charter | Annual |
| Financial Policies | Annual |
| Risk and Safeguarding Policies | Annual |
| Membership Policies | Annual or every 2 years |
| Ministry Frameworks | Annual during launch, then every 1-3 years |
| Templates | Annual or as used |
| Registers | Ongoing |
| Dashboards | Ongoing or quarterly |
| Archive Documents | As needed |

## 7. Review Authority

Review authority depends on document type.

Examples include International Board review for constitutional documents, Theological Oversight Council review for theological documents, Church Advisory Fellowship consultation for church relationship documents, Finance Committee review for financial policies, Governance Committee review for governance documents, National Board review for local chapter documents, and ministry leader review for operational procedures under delegated authority.

Approval authority must follow the [[Authority Matrix]].

## 8. Review Questions

A document review should ask:

1. Is the document still needed?
2. Is it consistent with Scripture and the Statement of Faith?
3. Is it consistent with mission, vision, and values?
4. Is it consistent with higher documents?
5. Is the authority level correct?
6. Are responsibilities clear?
7. Are procedures usable?
8. Are links and dependencies accurate?
9. Are definitions consistent?
10. Is the review date current?
11. Does it reflect accepted decisions?
12. Has law or context changed?
13. Does it need theological, legal, financial, or risk review?
14. Should it remain active, be revised, be superseded, or be archived?

## 9. Review Outcomes

A review may result in no change, minor editorial update, metadata update, substantive revision, theological review, legal review, board approval, supersession, archival, retirement, creation of related documents, or mission alignment review.

## 10. Versioning

Documents should use semantic versioning where practical.

Examples:

- 0.1.0 — early draft;
- 0.2.0 — substantial draft revision;
- 1.0.0 — first approved active version;
- 1.1.0 — minor substantive update;
- 2.0.0 — major revision.

Version changes should be reflected in the [[Changelog]] when material.

## 11. Superseded Documents

Superseded documents should not be deleted.

They should be moved or marked as superseded and linked to the new governing document.

The superseding document should identify what it replaces.

This protects institutional memory and prevents old documents from wandering around like governance ghosts.

## 12. Legal and Theological Review

Documents requiring legal review may include bylaws, incorporation documents, employment policies, housing policies, leases, privacy policies, financial policies, grant agreements, and national chapter documents.

Documents requiring theological review may include statement of faith, chaplaincy, church partnerships, teaching materials, prayer policies, mission alignment documents, and theological oversight policies.

## 13. Document Registry

Every official document should appear in the [[Document Registry]].

The registry should record document title, ID, status, version, type, category, authority, review date, owner, related documents, and dependencies.

Registry updates may be generated automatically from frontmatter where the generator supports it.

## 14. Decision Register

Major document approvals, amendments, supersessions, or retirements should be recorded in the [[Decision Register]].

A decision entry should include decision, date, authority, reason, alternatives considered, affected documents, and implementation steps.

## 15. Source of Truth

The Society's generator-ready Markdown source files are the source of truth for governance documents.

Generated outputs such as Obsidian vault files, PDFs, DOCX manuals, and HTML pages should be treated as publications, not the primary editable source.

Edit `source/`. Do not edit `dist/`. Future-you will send thank-you notes.

## 16. Link and Dependency Review

Document review should include checking broken wiki-links, missing dependencies, outdated related documents, duplicate titles, duplicate document IDs, orphaned documents, circular dependencies where problematic, and inconsistent naming.

The generator should eventually automate this.

## 17. Review Record

Each review should be recorded in one or more of document frontmatter, [[Document Registry]], [[Changelog]], [[Decision Register]], board minutes, review schedule, or release notes.

## 18. Review

This policy should be reviewed annually with [[Governance Review Process]], [[Document Registry]], and [[Decision Register]].
