# CCTS TEMPLATE-01 — Governance Forms and Templates

This generator-ready source package adds core reusable governance forms and templates for the Christian Community Transformation Society.

## Contents

- `source/91 Templates/Board Meeting Minutes Template.md`
- `source/91 Templates/Decision Record Template.md`
- `source/91 Templates/Policy Review Form.md`
- `source/91 Templates/Mission Alignment Review Form.md`
- `source/91 Templates/Confidentiality Agreement Template.md`
- `source/90 Institutional Memory/Registry Updates/Document Registry Update - TEMPLATE-01.md`

## Metadata note

Following the updated YAML rule, `scriptural-foundation` and `confessional-foundation` fields are left blank in these template documents because they do not directly depend on a specific Scripture passage or confessional article as their document foundation.

## Use

Copy the included `source/` folder into your Python content generator project, merging it with existing source files.

Then run:

```bash
python build.py
```

Edit source files only in `source/`, not in generated `dist/` output.
