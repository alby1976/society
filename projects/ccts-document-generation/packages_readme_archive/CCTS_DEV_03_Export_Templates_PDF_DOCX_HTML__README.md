# CCTS DEV-03 — Export Templates for PDF, DOCX, HTML, and Review Packages

This package adds export documentation, review package configuration, Jinja2 templates, and scripts for generating focused review packages.

## Contents

### Source documentation

- `source/94 Build System/PDF DOCX and HTML Export Guide.md`
- `source/94 Build System/Export Package Configuration.md`
- `source/94 Build System/Board Legal and Theological Review Package Procedure.md`
- `source/94 Build System/Public Document Export Policy.md`
- `source/90 Institutional Memory/Registry Updates/Document Registry Update - DEV-03.md`

### Templates

- `templates/html-page.html.j2`
- `templates/document-bundle.md.j2`
- `templates/review-package-index.md.j2`
- `templates/pdf-cover.md.j2`
- `templates/docx-cover.md.j2`

### Scripts and config

- `export_packages.yml`
- `scripts/build_review_packages.py`
- `scripts/export_selected.py`

## Use

Copy these files into the root of your governance generator repository.

Then run:

```bash
python scripts/build_review_packages.py
```

To export a custom package:

```bash
python scripts/export_selected.py --package custom-review --document "Mission Statement" --document "Statement of Faith"
```

## Metadata note

Following the updated YAML rule, `scriptural-foundation` and `confessional-foundation` fields are left blank in these export documents because they do not directly depend on a specific Scripture passage or confessional article as their document foundation.
