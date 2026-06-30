from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from zipfile import ZipFile
import shutil

import yaml
from jinja2 import Environment, FileSystemLoader

from ccts_generator.parser import discover_documents
from ccts_generator.config import BuildConfig


@dataclass
class ExportPackage:
    key: str
    title: str
    confidentiality: str
    include_categories: list[str]
    include_tags: list[str]
    include_documents: list[str]
    exclude_documents: list[str]
    exclude_statuses: list[str]
    output_formats: list[str]
    review_instructions: str


def load_packages(path: Path) -> list[ExportPackage]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    packages = []
    for key, raw in (data.get("packages") or {}).items():
        packages.append(
            ExportPackage(
                key=key,
                title=raw.get("title", key),
                confidentiality=raw.get("confidentiality", "Internal"),
                include_categories=raw.get("include_categories", []) or [],
                include_tags=raw.get("include_tags", []) or [],
                include_documents=raw.get("include_documents", []) or [],
                exclude_documents=raw.get("exclude_documents", []) or [],
                exclude_statuses=raw.get("exclude_statuses", []) or [],
                output_formats=raw.get("output_formats", ["markdown"]) or ["markdown"],
                review_instructions=raw.get("review_instructions", "") or "",
            )
        )
    return packages


def select_documents(package: ExportPackage, docs):
    selected = []
    include_doc_set = set(package.include_documents)
    exclude_doc_set = set(package.exclude_documents)

    for doc in docs:
        if doc.status in package.exclude_statuses:
            continue

        if doc.title in exclude_doc_set or doc.document_id in exclude_doc_set:
            continue

        include = False

        if doc.title in include_doc_set or doc.document_id in include_doc_set:
            include = True

        if package.include_categories and doc.category in package.include_categories:
            include = True

        if package.include_tags and set(doc.tags).intersection(set(package.include_tags)):
            include = True

        if include:
            selected.append(doc)

    return sorted(selected, key=lambda d: (d.category, d.title))


def main() -> None:
    config = BuildConfig()
    packages_path = Path("export_packages.yml")
    if not packages_path.exists():
        raise SystemExit("Missing export_packages.yml")

    docs = discover_documents(Path("source"))
    packages = load_packages(packages_path)

    env = Environment(loader=FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True)

    out_root = Path("dist/review-packages")
    if out_root.exists():
        shutil.rmtree(out_root)
    out_root.mkdir(parents=True, exist_ok=True)

    generated = date.today().isoformat()

    for package in packages:
        selected = select_documents(package, docs)
        package_dir = out_root / package.key
        package_dir.mkdir(parents=True, exist_ok=True)

        index_template = env.get_template("review-package-index.md.j2")
        bundle_template = env.get_template("document-bundle.md.j2")

        index = index_template.render(package=package, documents=selected, generated_date=generated)
        bundle = bundle_template.render(package=package, documents=selected, generated_date=generated)

        (package_dir / "index.md").write_text(index, encoding="utf-8")
        (package_dir / "bundle.md").write_text(bundle, encoding="utf-8")

        docs_dir = package_dir / "documents"
        docs_dir.mkdir(exist_ok=True)
        for doc in selected:
            target = docs_dir / doc.relative_path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(doc.raw_text, encoding="utf-8")

        zip_path = out_root / f"{package.key}.zip"
        with ZipFile(zip_path, "w") as z:
            for path in package_dir.rglob("*"):
                if path.is_file():
                    z.write(path, path.relative_to(package_dir.parent))

        print(f"{package.key}: {len(selected)} documents -> {zip_path}")


if __name__ == "__main__":
    main()
