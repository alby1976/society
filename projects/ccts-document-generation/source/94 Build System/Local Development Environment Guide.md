---
document-id: BUILD-019
title: Local Development Environment Guide
version: 0.1.0
status: Draft
type: Guide
document-category: Operations
jurisdiction: International
chapter: Global
governance-level: Administrative
effective-date:
last-reviewed: 2026-06-29
next-review-date: 2027-06-29
review-cycle: Annual
approved-by:
authority-level: Administrative
scriptural-foundation:
confessional-foundation:
related-documents:
  - "[[Repository Bootstrap Guide]]"
  - "[[Build Script Procedure]]"
  - "[[Windows Build Workflow]]"
  - "[[Dependency and Tooling Reference]]"
supersedes:
dependencies:
  - "[[Repository Bootstrap Guide]]"
tags:
  - local-development
  - python
  - setup
  - windows
  - guide
---

# Local Development Environment Guide

## 1. Purpose

This guide explains how to set up a local development environment for the governance vault generator.

It is intended for Windows, macOS, Linux, VS Code, PyCharm, and terminal workflows.

---

# 2. Governing Principle

The local setup should be boring, repeatable, and easy to repair.

A governance system should not require cleverness every time it is rebuilt.

---

# 3. Required Tools

Minimum tools:

- Python 3.10 or newer;
- Git;
- text editor;
- Obsidian;
- terminal or PowerShell.

Recommended tools:

- VS Code or PyCharm;
- GitHub Desktop if command-line Git feels heavy;
- 7-Zip or built-in ZIP tools;
- Obsidian Sync or another backup system if approved.

---

# 4. Python Environment

Create a virtual environment:

```bash
python -m venv .venv
```

Activate on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activate on macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

# 5. VS Code Setup

Recommended extensions:

- Python;
- Markdown All in One;
- YAML;
- GitLens;
- markdownlint if desired.

Open the repository folder, then select `.venv` as the Python interpreter.

---

# 6. PyCharm Setup

1. Open repository folder.
2. Configure Python interpreter.
3. Choose `.venv`.
4. Mark repository root as project root.
5. Run `build.py`.
6. Add run configurations for `scripts/build_all.py`, `scripts/audit_all.py`, and `scripts/merge_packages.py`.

---

# 7. Obsidian Setup

After build, open this folder as vault:

```text
dist/obsidian-vault/
```

Use source files for editing unless intentionally using Obsidian as the source editor.

---

# 8. Common Problems

| Problem | Fix |
|---|---|
| Python not found | Install Python and add to PATH |
| pip not found | Use `python -m pip` |
| venv activation blocked | Use PowerShell CurrentUser RemoteSigned policy |
| packages missing | Re-run `pip install -r requirements.txt` |
| generated vault missing | Run `python build.py` |
| changes not appearing | Edit `source/`, rebuild, reopen vault |

---

# 9. Review

This guide should be reviewed when supported tools or setup steps change.
