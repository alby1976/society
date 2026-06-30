---
document-id: REGISTRY-006
title: Registry Maintenance Procedure
version: 0.1.0
status: Draft
type: Procedure
document-category: Governance
jurisdiction: International
chapter: Global
governance-level: Administrative
effective-date:
last-reviewed: 2026-06-29
next-review-date: 2027-06-29
review-cycle: Monthly
approved-by:
authority-level: Administrative
scriptural-foundation:
confessional-foundation:
related-documents:
  - "[[Master Governance Dashboard]]"
  - "[[Master Document Registry]]"
  - "[[Master Decision Register]]"
  - "[[Master Changelog]]"
  - "[[Master Release Plan]]"
supersedes:
dependencies:
  - "[[Master Document Registry]]"
  - "[[Master Decision Register]]"
tags:
  - registry
  - maintenance
  - procedure
  - institutional-memory
  - governance
---

# Registry Maintenance Procedure

## 1. Purpose

This procedure explains how to maintain the governance vault registries.

The purpose is to keep the governance system searchable, reviewable, rebuildable, and useful over time.

---

# 2. Governing Principle

Registries are not optional indexes. They are institutional memory controls.

A document that is not registered can be forgotten. A decision that is not recorded can be repeated. A change that is not logged can become confusion.

---

# 3. When to Update the Document Registry

Update [[Master Document Registry]] when:

- a new document is added;
- a document title changes;
- a document ID changes;
- a document status changes;
- a document is superseded;
- a document is archived;
- a document category changes;
- a document's authority level changes;
- a document becomes active.

---

# 4. When to Update the Decision Register

Update [[Master Decision Register]] when a decision affects:

- doctrine;
- mission;
- governance;
- reserved powers;
- national chapters;
- ministry launch order;
- finance;
- housing;
- cooperative;
- Foundation grants;
- chaplaincy;
- church relationships;
- HR and leadership qualifications;
- risk and safeguarding;
- public communications;
- release process.

---

# 5. When to Update the Changelog

Update [[Master Changelog]] when:

- a package is added;
- a major group of documents is added;
- a document is changed materially;
- a document is superseded;
- metadata standards change;
- registry structure changes;
- a release is created.

---

# 6. Document ID Rules

Document IDs should be:

- stable;
- unique;
- short enough to read;
- grouped by category;
- not reused after deletion;
- preserved when titles change.

Examples:

| Prefix | Area |
|---|---|
| THEO | Theology |
| INT-GOV | International Governance |
| BOARD | Board |
| REP | Reporting |
| CHAP | Chaplaincy |
| HOUSE | Housing |
| COOP | Worker Cooperative |
| FOUND | Church Support Foundation |
| CHAPTER | National Chapters |
| ROADMAP | Roadmap |
| OPS | Operations |
| RISK | Risk Management |
| FIN | Finance |
| HR | Human Resources |
| SAFE | Safeguarding |
| COMMS | Communications |
| REGISTRY | Master registry documents |

---

# 7. YAML Maintenance

Every official document should include YAML frontmatter.

Use blank fields where the information is not yet known.

Do not fill `scriptural-foundation` or `confessional-foundation` just to make the metadata look complete. Use those fields only where the referenced Scripture or confession directly grounds that specific document.

---

# 8. Link Maintenance

When adding or renaming a document:

- update wiki-links;
- update related documents;
- update dependencies;
- update dashboards;
- update registry rows;
- update changelog;
- check for duplicate titles;
- check for broken links in Obsidian.

---

# 9. Superseding Documents

When a document is superseded:

1. mark old document status as `Superseded`;
2. add the new document to `supersedes`;
3. update registry;
4. update changelog;
5. preserve old document unless retention policy permits archive removal;
6. update links where appropriate.

---

# 10. Monthly Registry Review

Monthly review checklist:

- [ ] New documents added to registry.
- [ ] New decisions added to register.
- [ ] Changelog updated.
- [ ] Duplicate IDs checked.
- [ ] Duplicate titles checked.
- [ ] Broken links checked.
- [ ] Draft statuses reviewed.
- [ ] Review dates checked.
- [ ] Scriptural and confessional foundation fields checked.
- [ ] Release plan updated if release is near.

---

# 11. Annual Registry Review

Annual review checklist:

- [ ] All active documents reviewed or scheduled.
- [ ] Archived documents reviewed.
- [ ] Superseded documents checked.
- [ ] Decision register reviewed.
- [ ] Changelog reviewed.
- [ ] Document categories reviewed.
- [ ] Authority levels reviewed.
- [ ] National chapter documents reviewed.
- [ ] Public-release documents reviewed.
- [ ] Confidential documents checked.

---

# 12. Review

This procedure should be reviewed annually and whenever registry structure changes.
