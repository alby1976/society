---
# Required document controls used by registries, indexes, and exports.
document-id: "DOC-OPS-0001"
title: "Documentation Build Workflow"
version: "1.0.0"
status: "approved"
type: "procedure"
document-category: "operations"
effective-date: "2026-06-25"
last-reviewed: "2026-06-25"
tags: ["documentation", "automation", "procedure"]

# Recommended governance metadata. Omit keys that are not meaningful.
author: "Codex"
owner: "Documentation Maintainer"
next-review-date: "2027-06-25"
review-cycle: "annual"
approved-by: "Operations Lead"
authority-level: "staff"
related-documents: ["[[Governance Document Standard]]"]
dependencies: ["[[Governance Document Standard]]"]
changes:
  - date: "2026-06-25"
    version: "1.0.0"
    summary: "Documented the repeatable documentation build workflow."

# Optional output filename stem. The source folder path is preserved.
slug: "02 Documentation Build Workflow"
---

<!--
This sample document demonstrates an operational procedure. The body intentionally
uses common Markdown constructs so the starter PDF and DOCX exporters stay easy
to inspect.
-->

## Executive Summary

This procedure explains how documentation source files are converted into an Obsidian vault, generated governance notes, PDF export, DOCX export, and optional HTML site.

## Purpose

The purpose of this procedure is to make documentation generation repeatable, reviewable, and suitable for version control.

## Scope

This procedure applies to maintainers who edit `source/site.yml`, Markdown files under `source/`, or templates in `templates/`.

## Procedure

<!-- Update this checklist when the generator workflow changes. -->

1. Update `source/site.yml` with project metadata when needed.
2. Add or revise Markdown content anywhere under `source/`.
3. Confirm each page has the required frontmatter fields.
4. Run the automated build script.
5. Review the generated files in `dist/vault/`, `dist/guide.pdf`, `dist/guide.docx`, and optional `dist/site/`.

## Action Checklist

- [ ] Confirm required metadata is complete.
- [ ] Confirm optional metadata is meaningful before including it.
- [ ] Confirm Obsidian wiki-links resolve to intended documents.
- [ ] Confirm generated exports are committed or archived according to policy.

## Roles and Responsibilities

| Role | Responsibility |
| --- | --- |
| Documentation Maintainer | Updates source files and runs the build. |
| Reviewer | Checks generated documents for clarity, accuracy, and policy alignment. |
| Approver | Confirms final approval according to the document authority level. |

## Reporting Requirements

Build failures, missing required metadata, or publication errors should be recorded in the relevant issue tracker or review log.

## Review and Amendment Procedures

This procedure should be reviewed annually or whenever the generator changes in a way that affects document output.

## References

- [[Governance Document Standard]]

## Appendices

### Appendix A: Build Commands

```powershell
.\scripts\build.ps1
```

```bash
./scripts/build.sh
```
