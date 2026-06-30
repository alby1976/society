# CCTS BUILD-01 — Generator and Build System Documentation

This generator-ready source package adds documentation for the governance vault generator, source folder standards, build process, Jinja2 templates, and Obsidian import/review workflow.

## Contents

- `source/94 Build System/Governance Vault Generator Architecture.md`
- `source/94 Build System/Source Folder and Markdown Standards.md`
- `source/94 Build System/Build Script Procedure.md`
- `source/94 Build System/Jinja2 Template Standards.md`
- `source/94 Build System/Obsidian Import and Review Guide.md`
- `source/90 Institutional Memory/Registry Updates/Document Registry Update - BUILD-01.md`

## Metadata note

Following the updated YAML rule, `scriptural-foundation` and `confessional-foundation` fields are left blank in these build-system documents because they do not directly depend on a specific Scripture passage or confessional article as their document foundation.

## Use

Copy the included `source/` folder into your Python content generator project, merging it with existing source files.

Then run:

```bash
python build.py
```

Edit source files only in `source/`, not in generated `dist/` output.
