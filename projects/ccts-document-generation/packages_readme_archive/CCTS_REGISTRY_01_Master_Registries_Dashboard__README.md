# CCTS REGISTRY-01 — Master Registries and Governance Dashboard

This generator-ready source package creates the master registry and dashboard layer for the Christian Community Transformation Society governance vault.

## Contents

- `source/00 Home/Master Governance Dashboard.md`
- `source/90 Institutional Memory/Master Document Registry.md`
- `source/90 Institutional Memory/Master Decision Register.md`
- `source/90 Institutional Memory/Master Changelog.md`
- `source/90 Institutional Memory/Master Release Plan.md`
- `source/90 Institutional Memory/Registry Maintenance Procedure.md`
- `source/90 Institutional Memory/Registry Updates/Document Registry Update - REGISTRY-01.md`

## Metadata note

Following the updated YAML rule, `scriptural-foundation` and `confessional-foundation` fields are left blank in these registry documents because they do not directly depend on a specific Scripture passage or confessional article as their document foundation.

## Use

Copy the included `source/` folder into your Python content generator project, merging it with existing source files.

Then run:

```bash
python build.py
```

Edit source files only in `source/`, not in generated `dist/` output.
