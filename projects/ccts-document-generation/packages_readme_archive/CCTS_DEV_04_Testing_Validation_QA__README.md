# CCTS DEV-04 — Testing, Validation, and QA

This package adds testing and quality assurance documentation, pytest starter tests, metadata schema reference, and CI workflow for the CCTS governance vault generator.

## Contents

### Source documentation

- `source/94 Build System/Testing and Quality Assurance Guide.md`
- `source/94 Build System/Pytest Validation Suite Guide.md`
- `source/94 Build System/Metadata Schema Reference.md`
- `source/94 Build System/Link Checker and Registry Audit Procedure.md`
- `source/90 Institutional Memory/Registry Updates/Document Registry Update - DEV-04.md`

### Test files

- `tests/test_parser.py`
- `tests/test_validators.py`
- `tests/test_links.py`
- `tests/test_build_smoke.py`

### QA support

- `metadata_schema.yml`
- `requirements-dev.txt`
- `pytest.ini`
- `scripts/run_tests.py`
- `.github/workflows/test.yml`

## Use

Copy these files into the root of your governance generator repository.

Install test dependencies:

```bash
pip install -r requirements-dev.txt
```

Run tests:

```bash
pytest
```

Run QA checks:

```bash
python scripts/run_tests.py
```

## Metadata note

Following the updated YAML rule, `scriptural-foundation` and `confessional-foundation` fields are left blank in these QA documents because they do not directly depend on a specific Scripture passage or confessional article as their document foundation.
