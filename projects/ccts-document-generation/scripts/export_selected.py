from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZipFile

import yaml

from ccts_generator.parser import discover_documents


def main() -> None:
    parser = argparse.ArgumentParser(description="Export selected documents by title or document ID")
    parser.add_argument("--package", default="custom", help="Output package name")
    parser.add_argument("--document", action="append", default=[], help="Document title or ID to include")
    parser.add_argument("--source", default="source")
    args = parser.parse_args()

    docs = discover_documents(Path(args.source))
    requested = set(args.document)

    selected = [doc for doc in docs if doc.title in requested or doc.document_id in requested]

    out_dir = Path("dist/review-packages") / args.package
    out_dir.mkdir(parents=True, exist_ok=True)

    index_lines = [
        f"# {args.package} Export",
        "",
        "| Document ID | Title | Source |",
        "|---|---|---|",
    ]

    for doc in selected:
        target = out_dir / "documents" / doc.relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(doc.raw_text, encoding="utf-8")
        index_lines.append(f"| {doc.document_id} | [[{doc.title}]] | `{doc.relative_path}` |")

    (out_dir / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    zip_path = out_dir.parent / f"{args.package}.zip"
    with ZipFile(zip_path, "w") as z:
        for path in out_dir.rglob("*"):
            if path.is_file():
                z.write(path, path.relative_to(out_dir.parent))

    print(zip_path)


if __name__ == "__main__":
    main()
