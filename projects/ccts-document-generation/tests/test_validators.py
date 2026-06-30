from pathlib import Path

from ccts_generator.models import Document
from ccts_generator.validators import validate_documents


def make_doc(document_id: str, title: str):
    metadata = {
        "document-id": document_id,
        "title": title,
        "version": "0.1.0",
        "status": "Draft",
        "type": "Guide",
        "document-category": "Operations",
        "jurisdiction": "International",
        "chapter": "Global",
        "governance-level": "Administrative",
        "last-reviewed": "2026-06-29",
        "next-review-date": "2027-06-29",
        "review-cycle": "Annual",
        "authority-level": "Administrative",
        "tags": ["test"],
    }
    return Document(
        source_path=Path(f"{title}.md"),
        relative_path=Path(f"{title}.md"),
        metadata=metadata,
        body="# Body",
        raw_text="# Body",
    )


def test_duplicate_document_id_is_error():
    docs = [make_doc("DUP-001", "One"), make_doc("DUP-001", "Two")]

    result = validate_documents(docs)

    assert any("Duplicate document-id" in error for error in result.errors)


def test_invalid_status_is_warning():
    doc = make_doc("TEST-001", "Test")
    doc.metadata["status"] = "Almost Done"

    result = validate_documents([doc])

    assert any("unexpected status" in warning for warning in result.warnings)


def test_populated_foundation_field_warns_for_manual_confirmation():
    doc = make_doc("TEST-002", "Foundation Test")
    doc.metadata["scriptural-foundation"] = ["James 1:5"]

    result = validate_documents([doc])

    assert any("scriptural-foundation" in warning for warning in result.warnings)
