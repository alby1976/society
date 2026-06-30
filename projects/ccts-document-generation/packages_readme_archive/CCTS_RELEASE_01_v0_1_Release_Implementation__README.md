# CCTS RELEASE-01 — v0.1 Release and Implementation

This generator-ready source package adds release notes, implementation checklist, package inventory, and README draft for the Christian Community Transformation Society governance vault.

## Contents

- `source/93 Release/Governance Vault v0.1 Release Notes.md`
- `source/93 Release/Governance Vault Implementation Checklist.md`
- `source/93 Release/Package Inventory and Merge Order.md`
- `source/93 Release/Repository README Draft.md`
- `source/90 Institutional Memory/Registry Updates/Document Registry Update - RELEASE-01.md`

## Metadata note

Following the updated YAML rule, `scriptural-foundation` and `confessional-foundation` fields are left blank in these release documents because they do not directly depend on a specific Scripture passage or confessional article as their document foundation.

## Use

Copy the included `source/` folder into your Python content generator project, merging it with existing source files.

Then run:

```bash
python build.py
```

Edit source files only in `source/`, not in generated `dist/` output.
