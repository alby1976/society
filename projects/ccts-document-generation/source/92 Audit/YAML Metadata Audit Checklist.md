---
document-id: AUDIT-003
title: YAML Metadata Audit Checklist
version: 0.1.0
status: Draft
type: Checklist
document-category: Governance
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
  - "[[Final Governance Vault Audit Framework]]"
  - "[[Master Document Registry]]"
  - "[[Registry Maintenance Procedure]]"
  - "[[Master Release Plan]]"
supersedes:
dependencies:
  - "[[Final Governance Vault Audit Framework]]"
tags:
  - audit
  - yaml
  - metadata
  - checklist
  - governance
---

# YAML Metadata Audit Checklist

## 1. Purpose

This checklist helps audit YAML frontmatter across the governance vault.

Consistent YAML makes the vault easier to sort, filter, review, export, and rebuild.

---

# 2. Standard YAML Fields

Every official governance document should include:

```yaml
---
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
---
```

Some report templates may include additional reporting metadata.

---

# 3. Global Metadata Rules

- [ ] YAML opens and closes with `---`.
- [ ] YAML is valid.
- [ ] `document-id` is present.
- [ ] `title` matches document title.
- [ ] `version` uses a consistent version pattern.
- [ ] `status` is one of the approved statuses.
- [ ] `type` is one of the approved document types.
- [ ] `document-category` is accurate.
- [ ] `jurisdiction` is accurate.
- [ ] `chapter` is accurate.
- [ ] `governance-level` is accurate.
- [ ] `last-reviewed` is present.
- [ ] `next-review-date` is present.
- [ ] `review-cycle` is present.
- [ ] `authority-level` is present.
- [ ] `tags` are present.

---

# 4. Status Values

Approved status values:

- Draft;
- Proposed;
- Active;
- Archived;
- Superseded.

| Status Issue | Document | Action |
|---|---|---|
|  |  |  |

---

# 5. Type Values

Approved type values may include:

- Policy;
- Procedure;
- Framework;
- Charter;
- Manual;
- Bylaw;
- Constitution;
- Report;
- Guideline;
- Form;
- Template;
- Register;
- Checklist;
- Plan;
- Standard;
- Commentary.

| Type Issue | Document | Action |
|---|---|---|
|  |  |  |

---

# 6. Category Values

Approved category values may include:

- Governance;
- Theology;
- Ministry;
- Operations;
- Finance;
- Housing;
- Cooperative;
- Human Resources;
- Risk Management;
- Communications;
- Legal Readiness.

| Category Issue | Document | Action |
|---|---|---|
|  |  |  |

---

# 7. Scriptural and Confessional Foundation Rule

The following adopted rule must be audited:

`scriptural-foundation` and `confessional-foundation` should be populated only when those references directly provide the foundation for that specific document.

Do not fill these fields merely because the document is Christian, Reformed, or governance-related.

| Document | Field | Issue | Action |
|---|---|---|---|
|  | scriptural-foundation / confessional-foundation |  |  |

---

# 8. Link Fields

Check:

- [ ] `related-documents` uses Obsidian wiki-links.
- [ ] `dependencies` uses Obsidian wiki-links.
- [ ] `supersedes` is blank or accurate.
- [ ] Related documents exist or are intentionally planned.
- [ ] Dependencies exist or are intentionally planned.

---

# 9. Document ID Audit

| Check | Complete? | Notes |
|---|---|---|
| All document IDs present | Yes / No |  |
| No duplicate document IDs | Yes / No |  |
| IDs match registry | Yes / No |  |
| IDs use category prefix | Yes / No |  |
| Superseded IDs not reused | Yes / No |  |

---

# 10. Date Audit

| Check | Complete? | Notes |
|---|---|---|
| Last-reviewed dates present | Yes / No |  |
| Next-review dates present | Yes / No |  |
| Dates are valid ISO format where used | Yes / No |  |
| Review cycles are realistic | Yes / No |  |

---

# 11. Tag Audit

Tags should be:

- lowercase;
- consistent;
- useful for filtering;
- not too many;
- not random;
- hyphenated where helpful.

| Tag Issue | Document | Action |
|---|---|---|
|  |  |  |

---

# 12. Final YAML Rating

- [ ] Ready
- [ ] Ready with Notes
- [ ] Needs Cleanup
- [ ] Not Ready

Notes:

---

# 13. Review

This checklist should be completed before each major vault release.
