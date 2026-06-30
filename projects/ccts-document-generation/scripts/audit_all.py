from __future__ import annotations

from collections import Counter
from pathlib import Path

from ccts_generator.parser import discover_documents
from ccts_generator.validators import validate_documents
from ccts_generator.links import check_links


def main() -> None:
    docs = discover_documents(Path("source"))
    validation = validate_documents(docs)
    links = check_links(docs)

    ids = [doc.document_id for doc in docs if doc.document_id]
    titles = [doc.title for doc in docs if doc.title]

    duplicate_ids = [item for item, count in Counter(ids).items() if count > 1]
    duplicate_titles = [item for item, count in Counter(titles).items() if count > 1]

    lines = [
        "# Audit Summary",
        "",
        f"Documents discovered: **{len(docs)}**",
        f"Validation errors: **{len(validation.errors)}**",
        f"Validation warnings: **{len(validation.warnings)}**",
        f"Missing links: **{len(links.missing_links)}**",
        f"Duplicate document IDs: **{len(duplicate_ids)}**",
        f"Duplicate titles: **{len(duplicate_titles)}**",
        "",
        "## Duplicate Document IDs",
        "",
    ]

    lines.extend(f"- {item}" for item in duplicate_ids) if duplicate_ids else lines.append("- None")

    lines.extend(["", "## Duplicate Titles", ""])
    lines.extend(f"- {item}" for item in duplicate_titles) if duplicate_titles else lines.append("- None")

    lines.extend(["", "## Missing Links", ""])
    if links.missing_links:
        for link, sources in sorted(links.missing_links.items()):
            lines.append(f"- [[{link}]] linked from {', '.join(f'[[{s}]]' for s in sources)}")
    else:
        lines.append("- None")

    lines.extend(["", "## Warnings", ""])
    lines.extend(f"- {warning}" for warning in validation.warnings) if validation.warnings else lines.append("- None")

    lines.extend(["", "## Errors", ""])
    lines.extend(f"- {error}" for error in validation.errors) if validation.errors else lines.append("- None")

    out = Path("dist/reports/audit-summary.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out)

    if validation.errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
