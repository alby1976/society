---
document-id: BUILD-009
title: Windows Build Workflow
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
  - "[[Automated Build Scripts Guide]]"
  - "[[Build Script Procedure]]"
  - "[[Obsidian Import and Review Guide]]"
supersedes:
dependencies:
  - "[[Build Script Procedure]]"
tags:
  - windows
  - build-system
  - guide
  - powershell
  - obsidian
---

# Windows Build Workflow

## 1. Purpose

This guide gives a simple Windows workflow for building the governance vault.

It is intended for users who want a repeatable process from Windows 11 using PowerShell, Command Prompt, or an editor such as VS Code or PyCharm.

---

# 2. One-Time Setup

Open PowerShell in the repository folder.

Run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then try again.

---

# 3. Build

Run:

```powershell
.\build.ps1
```

or:

```powershell
python build.py
```

---

# 4. Command Prompt Build

Run:

```cmd
build.cmd
```

---

# 5. Review Output

Open:

```text
dist\obsidian-vault\
```

as an Obsidian vault.

Review:

- `dist\reports\build-report.md`;
- `dist\reports\missing-links.md`;
- `dist\reports\generated-document-registry.md`.

---

# 6. Common Windows Issues

| Issue | Action |
|---|---|
| Python not found | Install Python and check PATH |
| Activation blocked | Set PowerShell execution policy for current user |
| Missing packages | Run `pip install -r requirements.txt` |
| Build output old | Delete `dist/` or run clean command |
| Obsidian not updating | Close and reopen vault or rebuild |

---

# 7. Review

This guide should be reviewed whenever the Windows build process changes.
