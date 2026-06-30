---
document-id: REGISTRY-005
title: Master Release Plan
version: 0.1.0
status: Draft
type: Plan
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
  - "[[Registry Maintenance Procedure]]"
supersedes:
dependencies:
  - "[[Master Document Registry]]"
  - "[[Master Changelog]]"
tags:
  - release-plan
  - governance
  - registry
  - build
  - obsidian
---

# Master Release Plan

## 1. Purpose

This release plan provides a simple process for preparing a governance vault release from the source Markdown documents.

It is intended to support Obsidian, Git repositories, PDF/DOCX generation, and long-term governance review.

---

# 2. Release Principle

Source files are the authority. Generated files are outputs.

A release should package what future leaders need to review, rebuild, and understand the governance system.

---

# 3. Release Stages

| Stage | Description | Complete |
|---|---|---|
| Stage 1 | Merge all source folders into one repository | [ ] |
| Stage 2 | Confirm folder structure | [ ] |
| Stage 3 | Confirm YAML frontmatter | [ ] |
| Stage 4 | Confirm document IDs | [ ] |
| Stage 5 | Confirm wiki-links | [ ] |
| Stage 6 | Update master registry | [ ] |
| Stage 7 | Update decision register | [ ] |
| Stage 8 | Update changelog | [ ] |
| Stage 9 | Run generator | [ ] |
| Stage 10 | Review generated Obsidian vault | [ ] |
| Stage 11 | Review PDF/DOCX outputs | [ ] |
| Stage 12 | Tag release in Git | [ ] |
| Stage 13 | Archive release package | [ ] |

---

# 4. Recommended Release Names

| Release | Description |
|---|---|
| v0.1-governance-draft | First complete governance draft vault |
| v0.2-review-cleanup | Link cleanup, registry cleanup, and review updates |
| v0.3-legal-review | Legal readiness and jurisdiction review version |
| v0.4-board-review | Board-ready governance package |
| v1.0-adopted | First formally approved release |

---

# 5. Release Checklist

## Source

- [ ] All package `source/` folders merged.
- [ ] No documents edited only in generated `dist/`.
- [ ] Folder structure reviewed.
- [ ] Duplicate names checked.
- [ ] Missing documents identified.

## YAML

- [ ] Required fields exist.
- [ ] `document-id` stable.
- [ ] `status` accurate.
- [ ] `type` accurate.
- [ ] `document-category` accurate.
- [ ] `review-cycle` accurate.
- [ ] `scriptural-foundation` used only where directly foundational.
- [ ] `confessional-foundation` used only where directly foundational.

## Links

- [ ] Obsidian wiki-links resolve.
- [ ] Major dashboards link correctly.
- [ ] Related documents exist.
- [ ] Dependencies exist.
- [ ] Superseded documents recorded if applicable.

## Registries

- [ ] [[Master Document Registry]] updated.
- [ ] [[Master Decision Register]] updated.
- [ ] [[Master Changelog]] updated.
- [ ] Registry update documents archived.

## Build

- [ ] Generator runs without error.
- [ ] Obsidian vault generated.
- [ ] PDF generated if configured.
- [ ] DOCX generated if configured.
- [ ] HTML generated if configured.
- [ ] Output reviewed.

## Governance Review

- [ ] Theological review needed documents identified.
- [ ] Legal review needed documents identified.
- [ ] Board review needed documents identified.
- [ ] Public-release documents identified.
- [ ] Confidential documents protected.

---

# 6. Release Notes Template

```markdown
# Release Notes - v0.1-governance-draft

## Summary

## Added

## Changed

## Known Issues

## Documents Requiring Legal Review

## Documents Requiring Theological Review

## Documents Requiring Board Review

## Next Steps
```

---

# 7. Git Tag Recommendation

Suggested tag format:

```bash
git tag -a v0.1-governance-draft -m "CCTS governance vault v0.1 draft"
git push origin v0.1-governance-draft
```

Suggested commit summary:

```text
Add CCTS governance vault source documents and registry system
```

---

# 8. Review

This release plan should be reviewed before every major release.
