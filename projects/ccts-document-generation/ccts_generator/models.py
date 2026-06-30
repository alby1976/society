from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "document-id",
    "title",
    "version",
    "status",
    "type",
    "document-category",
    "jurisdiction",
    "chapter",
    "governance-level",
    "last-reviewed",
    "next-review-date",
    "review-cycle",
    "authority-level",
    "tags",
]

VALID_STATUSES = {"Draft", "Proposed", "Active", "Archived", "Superseded"}

VALID_TYPES = {
    "Policy",
    "Procedure",
    "Framework",
    "Charter",
    "Manual",
    "Bylaw",
    "Constitution",
    "Report",
    "Guideline",
    "Form",
    "Template",
    "Register",
    "Checklist",
    "Plan",
    "Standard",
    "Commentary",
    "Guide",
}

VALID_CATEGORIES = {
    "Governance",
    "Theology",
    "Ministry",
    "Operations",
    "Finance",
    "Housing",
    "Cooperative",
    "Human Resources",
    "Risk Management",
    "Communications",
    "Legal Readiness",
}


@dataclass
class Document:
    source_path: Path
    relative_path: Path
    metadata: dict[str, Any]
    body: str
    raw_text: str
    links: list[str] = field(default_factory=list)

    @property
    def document_id(self) -> str:
        return str(self.metadata.get("document-id", "") or "")

    @property
    def title(self) -> str:
        return str(self.metadata.get("title", "") or self.source_path.stem)

    @property
    def status(self) -> str:
        return str(self.metadata.get("status", "") or "")

    @property
    def doc_type(self) -> str:
        return str(self.metadata.get("type", "") or "")

    @property
    def category(self) -> str:
        return str(self.metadata.get("document-category", "") or "")

    @property
    def tags(self) -> list[str]:
        value = self.metadata.get("tags", [])
        if isinstance(value, list):
            return [str(v) for v in value]
        if isinstance(value, str):
            return [value]
        return []

    def obsidian_filename(self) -> str:
        return f"{self.title}.md"
