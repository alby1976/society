# CCTS DEV-02 — Automated Build Scripts and CI

This package adds automation scripts and CI files for the CCTS governance vault generator.

## Contents

### Source documentation

- `source/94 Build System/Automated Build Scripts Guide.md`
- `source/94 Build System/Package Merge Automation Procedure.md`
- `source/94 Build System/GitHub Actions Build and Audit Workflow.md`
- `source/94 Build System/Windows Build Workflow.md`
- `source/90 Institutional Memory/Registry Updates/Document Registry Update - DEV-02.md`

### Scripts

- `scripts/merge_packages.py`
- `scripts/build_all.py`
- `scripts/audit_all.py`
- `scripts/new_document.py`

### Windows helpers

- `build.ps1`
- `build.cmd`

### GitHub Actions

- `.github/workflows/build.yml`
- `.github/workflows/audit.yml`

### Makefile addition

- `Makefile.addon`

## Use

Copy these files into the root of your governance generator repository.

Then run:

```bash
python scripts/build_all.py
```

To merge downloaded package ZIPs, put ZIP files into `packages/` and run:

```bash
python scripts/merge_packages.py packages/
```

## Metadata note

Following the updated YAML rule, `scriptural-foundation` and `confessional-foundation` fields are left blank in these build-system documents because they do not directly depend on a specific Scripture passage or confessional article as their document foundation.
