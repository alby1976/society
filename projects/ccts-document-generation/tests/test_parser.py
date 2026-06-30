from pathlib import Path

from ccts_generator.parser import discover_documents, parse_markdown_file


def test_parse_markdown_frontmatter(tmp_path: Path):
    source = tmp_path / "source"
    source.mkdir()
    doc_path = source / "Example.md"
    doc_path.write_text(
        """---
document-id: EXAMPLE-001
title: Example
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
  - example
---

# Example

See [[Other Document]].
""",
        encoding="utf-8",
    )

    doc = parse_markdown_file(doc_path, source)

    assert doc.document_id == "EXAMPLE-001"
    assert doc.title == "Example"
    assert "Other Document" in doc.links
    assert doc.relative_path == Path("Example.md")


def test_discover_documents_recursively(tmp_path: Path):
    source = tmp_path / "source"
    nested = source / "A" / "B"
    nested.mkdir(parents=True)
    (nested / "Doc.md").write_text("# Doc\n", encoding="utf-8")

    docs = discover_documents(source)

    assert len(docs) == 1
    assert docs[0].relative_path == Path("A/B/Doc.md")
