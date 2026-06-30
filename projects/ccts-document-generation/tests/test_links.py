from pathlib import Path

from ccts_generator.models import Document
from ccts_generator.links import check_links


def make_doc(title: str, links: list[str]):
    return Document(
        source_path=Path(f"{title}.md"),
        relative_path=Path(f"{title}.md"),
        metadata={
            "document-id": title.upper().replace(" ", "-"),
            "title": title,
            "status": "Draft",
            "type": "Guide",
            "document-category": "Operations",
        },
        body="# Body",
        raw_text="# Body",
        links=links,
    )


def test_missing_link_reported():
    docs = [make_doc("One", ["Two"])]

    report = check_links(docs)

    assert "Two" in report.missing_links
    assert report.missing_links["Two"] == ["One"]


def test_existing_link_is_inbound():
    docs = [make_doc("One", ["Two"]), make_doc("Two", [])]

    report = check_links(docs)

    assert "Two" not in report.missing_links
    assert report.inbound_links["Two"] == ["One"]
