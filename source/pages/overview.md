---
# Required document controls used by registries, indexes, and exports.
document-id: "DOC-GOV-0001"
title: "Governance Document Standard"
version: "1.0.0"
status: "approved"
type: "standard"
document-category: "governance"
effective-date: "2026-06-25"
last-reviewed: "2026-06-25"
tags: ["governance", "markdown", "obsidian"]

# Recommended governance metadata. Omit keys that are not meaningful.
author: "Codex"
owner: "Governance Committee"
next-review-date: "2027-06-25"
review-cycle: "annual"
approved-by: "Board of Directors"
authority-level: "board"
related-documents: ["[[Board Governance Policy]]", "[[Document Control Procedure]]"]
decision-id: "GOV-0001"
changes:
  - date: "2026-06-25"
    version: "1.0.0"
    summary: "Established the governance document metadata standard."

# Optional output filename stem. The source folder path is preserved.
slug: "01 Governance Document Standard"
---

<!--
This sample document demonstrates a governance standard. Keep body headings
semantic because PDF, DOCX, and Obsidian outputs all reuse this Markdown body.
-->

## Executive Summary

This standard defines how organizational governance documents are generated as Markdown files suitable for Obsidian, Git repositories, and long-term records management.

## Purpose

The purpose of this standard is to ensure that every generated document has consistent YAML frontmatter, clear headings, durable versioning, and a structure that can be reviewed over time.

## Scope

This standard applies to policies, procedures, standards, governance records, and operational documents generated through this repository.

## Definitions

| Term | Definition |
| --- | --- |
| Frontmatter | YAML metadata placed at the beginning of a Markdown document. |
| Governance Document | A policy, procedure, standard, or record that defines authority, accountability, or organizational practice. |
| Obsidian Wiki-Link | A Markdown-style internal reference such as `[[Board Governance Policy]]`. |

## Required Document Controls

<!-- These controls explain why the generator validates required frontmatter. -->

- Each document must include ordered YAML frontmatter.
- Each document must use semantic versioning.
- Each document must include an effective date and last reviewed date.
- Optional properties must be omitted when they are not meaningful.

## Roles and Responsibilities

| Role | Responsibility |
| --- | --- |
| Board | Approves board-level governance documents and amendments. |
| Executive | Maintains operational alignment with approved governance documents. |
| Staff | Follows the current approved version and proposes improvements when needed. |
| Committees | Review assigned documents and recommend updates within their authority. |

## Review and Amendment Procedures

1. Review the document according to its stated review cycle.
2. Confirm whether the authority level and related documents remain accurate.
3. Update the semantic version when substantive changes are approved.
4. Record the new last-reviewed date in the YAML frontmatter.

## References

- [[Board Governance Policy]]
- [[Document Control Procedure]]

## Appendices

### Appendix A: Frontmatter Order

The generator writes required properties first, then meaningful recommended properties, then meaningful optional properties.
