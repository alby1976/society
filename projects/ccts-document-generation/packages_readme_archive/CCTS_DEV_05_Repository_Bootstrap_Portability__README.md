# CCTS DEV-05 — Repository Bootstrap and Portability

This package adds repository setup, local development, dependency, backup, and portability documentation plus helper setup files.

## Contents

### Source documentation

- `source/94 Build System/Repository Bootstrap Guide.md`
- `source/94 Build System/Local Development Environment Guide.md`
- `source/94 Build System/Dependency and Tooling Reference.md`
- `source/94 Build System/Backup Restore and Portability Guide.md`
- `source/90 Institutional Memory/Registry Updates/Document Registry Update - DEV-05.md`

### Helper files

- `scripts/bootstrap_repo.py`
- `setup.sh`
- `setup.ps1`
- `.devcontainer/devcontainer.json`
- `config/build_config.yml`
- `.env.example`

## Use

Copy these files into the root of your governance generator repository.

Run:

```bash
python scripts/bootstrap_repo.py
```

On Windows:

```powershell
.\setup.ps1
```

On macOS/Linux:

```bash
bash setup.sh
```

## Metadata note

Following the updated YAML rule, `scriptural-foundation` and `confessional-foundation` fields are left blank in these setup documents because they do not directly depend on a specific Scripture passage or confessional article as their document foundation.
