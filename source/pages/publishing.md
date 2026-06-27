---
# Required document controls used by registries, indexes, and exports.
document-id: "DOC-REC-0001"
title: "Publishing Outputs Policy"
version: "1.0.0"
status: "approved"
type: "policy"
document-category: "records-management"
effective-date: "2026-06-25"
last-reviewed: "2026-06-25"
tags: ["publishing", "records", "pdf", "docx", "obsidian"]

# Recommended governance metadata. Omit keys that are not meaningful.
author: "Codex"
owner: "Records Custodian"
next-review-date: "2027-06-25"
review-cycle: "annual"
approved-by: "Executive Director"
authority-level: "executive"
related-documents: ["[[Governance Document Standard]]", "[[Documentation Build Workflow]]"]
decision-id: "GOV-0002"
dependencies: ["[[Governance Document Standard]]", "[[Documentation Build Workflow]]"]
changes:
  - date: "2026-06-25"
    version: "1.0.0"
    summary: "Established publishing rules for generated Markdown, PDF, and DOCX outputs."

# Optional governance foundations and output filename stem.
scriptural-foundation: ["1 Corinthians 14:40", "Colossians 3:23"]
slug: "03 Publishing Outputs Policy"
---

<!--
This sample document demonstrates a publishing policy. Metadata drives the
generated registries; this body provides the policy text shown in exports.
-->

## Executive Summary

This policy defines how generated Markdown, PDF, and DOCX outputs are treated as organizational publishing artifacts.

## Purpose

The purpose of this policy is to preserve reliable records while allowing documents to be used in Obsidian, Git repositories, and standard office formats.

## Scope

This policy applies to all files generated into the `dist/` folder by the documentation generator.

## Main Content

<!-- Generated output types are listed here because they are user-facing artifacts. -->

Generated outputs include:

- Obsidian Markdown notes with YAML frontmatter and wiki-links.
- PDF files for fixed-format distribution.
- DOCX files for review, editing, and office workflows.

## Christian Organization Considerations

When documents are intended for a Christian organization, governance should support faithful stewardship, prayerful accountability, and the ministry of the local church rather than replacing it.

Scripture references should be included only when they directly support the document purpose.

## Roles and Responsibilities

| Role | Responsibility |
| --- | --- |
| Executive Director | Authorizes publication of executive-level records. |
| Ministry Lead | Confirms ministry documents align with doctrine and practice. |
| Records Custodian | Preserves approved outputs and maintains institutional memory. |

## Reporting Requirements

Published governance documents should be recorded in the organization's document register with version, status, authority level, and review date.

## Review and Amendment Procedures

1. Review published outputs before distribution.
2. Confirm that PDF and DOCX exports correspond to the current Markdown source.
3. Archive superseded versions according to the records retention policy.
4. Update related document links when policies are amended.

## References

- [[Governance Document Standard]]
- [[Documentation Build Workflow]]
- 1 Corinthians 14:40
- Colossians 3:23

## Appendices

### Appendix A: Output Folder

The `dist/` folder is the publishing boundary for generated files.
