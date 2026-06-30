---
document-id: BUILD-005
title: Obsidian Import and Review Guide
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
  - "[[Master Governance Dashboard]]"
  - "[[Governance Vault Implementation Checklist]]"
  - "[[Missing Link and Dependency Review Checklist]]"
  - "[[YAML Metadata Audit Checklist]]"
  - "[[Final Governance Readiness Report]]"
supersedes:
dependencies:
  - "[[Master Governance Dashboard]]"
tags:
  - obsidian
  - import
  - review
  - guide
  - governance-vault
---

# Obsidian Import and Review Guide

## 1. Purpose

This guide explains how to open and review the generated governance vault in Obsidian.

It is written to reduce mental load and provide one simple review path.

---

# 2. Before Import

Confirm that you have:

- generated vault output;
- Obsidian installed;
- folder access to the generated vault;
- source repository preserved separately;
- latest build completed.

Recommended output folder:

```text
dist/obsidian-vault/
```

---

# 3. Open Vault in Obsidian

1. Open Obsidian.
2. Choose `Open folder as vault`.
3. Select the generated vault folder.
4. Open the vault.
5. Start with [[Master Governance Dashboard]].

---

# 4. First Review Path

Open these documents first:

1. [[Master Governance Dashboard]]
2. [[Master Document Registry]]
3. [[Master Decision Register]]
4. [[Master Changelog]]
5. [[Master Release Plan]]
6. [[Final Governance Readiness Report]]

This gives the overview before reading individual policies.

---

# 5. Recommended Obsidian Settings

Helpful settings:

- turn on backlinks;
- turn on outgoing links;
- use graph view for broken or isolated areas;
- use search for `status: Draft`;
- use search for `scriptural-foundation:` to audit populated foundation fields;
- use search for `TODO` or blank fields if used.

---

# 6. Review by Area

Use the dashboard to review:

- theology;
- mission;
- governance;
- reporting;
- ministries;
- national chapters;
- operations;
- risk;
- finance;
- HR;
- safeguarding;
- communications;
- legal readiness;
- templates;
- audit;
- release.

Do not try to review everything randomly.

---

# 7. Link Review

In Obsidian, check:

- unresolved links;
- duplicate note names;
- isolated notes;
- backlinks to core documents;
- dashboard navigation;
- registry links.

Use [[Missing Link and Dependency Review Checklist]].

---

# 8. Metadata Review

Use Obsidian search to find:

```text
document-id:
status: Draft
scriptural-foundation:
confessional-foundation:
next-review-date:
```

Use [[YAML Metadata Audit Checklist]].

---

# 9. Editing Rule

If you find an error, edit the source file in `source/`, not the generated vault, unless the generated vault is being used directly as the source.

Preferred workflow:

1. note the issue;
2. locate source file;
3. edit source file;
4. rebuild;
5. reopen or refresh vault.

---

# 10. Review Notes

Use a review note or audit report for findings.

Suggested note:

```text
source/92 Audit/Final Governance Readiness Report.md
```

Record:

- broken links;
- missing documents;
- duplicate titles;
- legal review needs;
- theological review needs;
- board review needs;
- documents needing merge or rewrite.

---

# 11. Public vs Internal Review

Do not assume the whole vault is public.

Some documents may be internal, restricted, confidential, board confidential, or legal privileged.

Public release should be limited to documents approved for public communication.

---

# 12. Review

This guide should be reviewed whenever the Obsidian workflow or generator output changes.
