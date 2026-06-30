---
document-id: RELEASE-004
title: Repository README Draft
version: 0.1.0
status: Draft
type: Template
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
  - "[[Governance Vault v0.1 Release Notes]]"
  - "[[Governance Vault Implementation Checklist]]"
  - "[[Package Inventory and Merge Order]]"
supersedes:
dependencies:
  - "[[Governance Vault v0.1 Release Notes]]"
tags:
  - release
  - readme
  - repository
  - template
  - governance-vault
---

# Repository README Draft

## Christian Community Transformation Society Governance Vault

This repository contains the source documents and generator workflow for the Christian Community Transformation Society governance vault.

The vault is designed for:

- Obsidian review;
- Git-based version control;
- Markdown source editing;
- generated PDF/DOCX/HTML outputs;
- governance review;
- institutional memory;
- theological, legal, board, and operational review.

## Source of Truth

Edit documents in:

```text
source/
```

Generated output folders are not the source of truth.

## Build

Run:

```bash
python build.py
```

or the build command defined by this repository.

## Main Entry Points

- `source/00 Home/Master Governance Dashboard.md`
- `source/90 Institutional Memory/Master Document Registry.md`
- `source/90 Institutional Memory/Master Decision Register.md`
- `source/90 Institutional Memory/Master Changelog.md`
- `source/90 Institutional Memory/Master Release Plan.md`

## Metadata Rule

Use `scriptural-foundation` and `confessional-foundation` only when the references directly provide the foundation for that specific document.

Leave these fields blank for documents where they are not directly foundational.

## Release Status

Current draft release:

```text
v0.1-governance-draft
```

This release is a draft governance vault. It is not final legal advice, final charity documentation, or formally adopted governance unless approved by the proper authority.

## Suggested Workflow

1. Edit Markdown files in `source/`.
2. Update registries.
3. Update decision register when decisions are made.
4. Update changelog.
5. Run generator.
6. Review Obsidian vault.
7. Audit YAML and links.
8. Commit changes.
9. Tag release.

## Suggested Commit

```bash
git add source README.md
git commit -m "Add CCTS governance vault v0.1 draft source documents"
```

## Suggested Release Tag

```bash
git tag -a v0.1-governance-draft -m "CCTS governance vault v0.1 draft"
git push origin v0.1-governance-draft
```

## Review Needed

Before formal use, documents should receive appropriate review:

- theological review;
- legal review;
- board review;
- church advisory review;
- finance review;
- safeguarding review;
- national chapter review;
- technical build review.

## License

Add license terms here after board and legal review.
