# CCTS DEV-01 — Python Generator Source Code

This package provides a working starter Python generator for the Christian Community Transformation Society governance vault.

It is designed to:

- read Markdown files recursively from `source/`;
- parse YAML frontmatter;
- preserve folder structure;
- generate an Obsidian-ready vault;
- create master registries;
- check missing links;
- create HTML output;
- create simple DOCX output when `python-docx` is installed;
- create simple PDF output when `reportlab` is installed;
- produce build reports;
- package release output.

## Quick Start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python build.py
```

On macOS or Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python build.py
```

## Folder Structure

```text
.
├── build.py
├── pyproject.toml
├── requirements.txt
├── Makefile
├── ccts_generator/
├── scripts/
├── templates/
├── source/
└── dist/
```

## Source of Truth

Edit Markdown documents in:

```text
source/
```

Generated output in `dist/` should not be edited as the master copy.

## Commands

```bash
python build.py
python scripts/validate_yaml.py
python scripts/check_links.py
python scripts/package_release.py
```

or:

```bash
make build
make audit
make release
```

## Optional Export Dependencies

The generator will create DOCX and PDF output only if optional dependencies are installed.

```bash
pip install python-docx reportlab markdown
```

If those packages are missing, the generator will skip those outputs and still build the Obsidian vault and reports.

## Metadata Rule

`scriptural-foundation` and `confessional-foundation` should be filled only when those references directly provide the foundation for that specific document.

Leave them blank for ordinary administrative, registry, operational, legal-readiness, release, audit, or build-system documents unless directly foundational.
