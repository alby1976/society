from pathlib import Path

from ccts_generator.cli import build
from ccts_generator.config import BuildConfig


def test_build_smoke(tmp_path: Path):
    source = tmp_path / "source"
    source.mkdir()
    (source / "Sample.md").write_text(
        """---
document-id: SAMPLE-001
title: Sample
version: 0.1.0
status: Draft
type: Guide
document-category: Operations
jurisdiction: International
chapter: Global
governance-level: Administrative
last-reviewed: 2026-06-29
next-review-date: 2027-06-29
review-cycle: Annual
authority-level: Administrative
tags:
  - sample
---

# Sample
""",
        encoding="utf-8",
    )

    dist = tmp_path / "dist"
    config = BuildConfig(
        source_dir=source,
        dist_dir=dist,
        obsidian_dir=dist / "obsidian-vault",
        html_dir=dist / "html",
        docx_dir=dist / "docx",
        pdf_dir=dist / "pdf",
        reports_dir=dist / "reports",
    )

    code = build(config)

    assert code == 0
    assert (dist / "obsidian-vault" / "Sample.md").exists()
    assert (dist / "reports" / "build-report.md").exists()
