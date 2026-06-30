from collections import Counter
from dataclasses import dataclass

from .models import Document, REQUIRED_FIELDS, VALID_CATEGORIES, VALID_STATUSES, VALID_TYPES


@dataclass
class ValidationResult:
    warnings: list[str]
    errors: list[str]

    @property
    def ok(self) -> bool:
        return not self.errors


def validate_documents(docs: list[Document]) -> ValidationResult:
    warnings: list[str] = []
    errors: list[str] = []

    ids = [doc.document_id for doc in docs if doc.document_id]
    titles = [doc.title for doc in docs if doc.title]

    duplicate_ids = [doc_id for doc_id, count in Counter(ids).items() if count > 1]
    duplicate_titles = [title for title, count in Counter(titles).items() if count > 1]

    for duplicate_id in duplicate_ids:
        errors.append(f"Duplicate document-id: {duplicate_id}")

    for duplicate_title in duplicate_titles:
        warnings.append(f"Duplicate title: {duplicate_title}")

    for doc in docs:
        if not doc.metadata:
            warnings.append(f"{doc.relative_path}: missing YAML frontmatter")
            continue

        for field in REQUIRED_FIELDS:
            if field not in doc.metadata or doc.metadata.get(field) in (None, ""):
                warnings.append(f"{doc.relative_path}: missing or blank required field `{field}`")

        if doc.status and doc.status not in VALID_STATUSES:
            warnings.append(f"{doc.relative_path}: unexpected status `{doc.status}`")

        if doc.doc_type and doc.doc_type not in VALID_TYPES:
            warnings.append(f"{doc.relative_path}: unexpected type `{doc.doc_type}`")

        if doc.category and doc.category not in VALID_CATEGORIES:
            warnings.append(f"{doc.relative_path}: unexpected document-category `{doc.category}`")

        for foundation_field in ("scriptural-foundation", "confessional-foundation"):
            value = doc.metadata.get(foundation_field)
            if value not in (None, "", []):
                warnings.append(
                    f"{doc.relative_path}: `{foundation_field}` is populated; confirm it is directly foundational"
                )

    return ValidationResult(warnings=warnings, errors=errors)
