import re
from pathlib import Path
from typing import Any

import yaml

from .models import Document


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def parse_markdown_file(path: Path, source_dir: Path) -> Document:
    raw = path.read_text(encoding="utf-8")
    metadata: dict[str, Any] = {}
    body = raw

    match = FRONTMATTER_RE.match(raw)
    if match:
        yaml_text = match.group(1)
        parsed = yaml.safe_load(yaml_text) or {}
        if isinstance(parsed, dict):
            metadata = parsed
        body = raw[match.end():]

    links = sorted(set(link.strip() for link in WIKILINK_RE.findall(raw)))

    return Document(
        source_path=path,
        relative_path=path.relative_to(source_dir),
        metadata=metadata,
        body=body,
        raw_text=raw,
        links=links,
    )


def discover_documents(source_dir: Path) -> list[Document]:
    docs: list[Document] = []
    if not source_dir.exists():
        return docs

    for path in sorted(source_dir.rglob("*.md")):
        if any(part.startswith(".") for part in path.parts):
            continue
        docs.append(parse_markdown_file(path, source_dir))
    return docs


def write_markdown_with_frontmatter(doc: Document) -> str:
    frontmatter = yaml.safe_dump(
        doc.metadata,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    ).strip()
    return f"---\n{frontmatter}\n---\n\n{doc.body.lstrip()}"
