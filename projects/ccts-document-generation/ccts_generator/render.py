import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .config import BuildConfig
from .models import Document
from .parser import write_markdown_with_frontmatter


def prepare_dist(config: BuildConfig) -> None:
    config.dist_dir.mkdir(parents=True, exist_ok=True)
    for folder in [
        config.obsidian_dir,
        config.html_dir,
        config.docx_dir,
        config.pdf_dir,
        config.reports_dir,
    ]:
        if folder.exists():
            shutil.rmtree(folder)
        folder.mkdir(parents=True, exist_ok=True)


def copy_obsidian_vault(docs: list[Document], config: BuildConfig) -> None:
    for doc in docs:
        out_path = config.obsidian_dir / doc.relative_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(write_markdown_with_frontmatter(doc), encoding="utf-8")


def get_env(config: BuildConfig) -> Environment:
    return Environment(
        loader=FileSystemLoader(str(config.templates_dir)),
        autoescape=select_autoescape(enabled_extensions=("html", "xml")),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def render_registry(docs: list[Document], config: BuildConfig) -> str:
    template_path = config.templates_dir / "registry.md.j2"
    if template_path.exists():
        env = get_env(config)
        return env.get_template("registry.md.j2").render(documents=docs)

    lines = [
        "# Generated Document Registry",
        "",
        "| Document ID | Title | Status | Type | Category | Source Path |",
        "|---|---|---|---|---|---|",
    ]
    for doc in sorted(docs, key=lambda d: (d.category, d.title)):
        lines.append(
            f"| {doc.document_id} | [[{doc.title}]] | {doc.status} | {doc.doc_type} | {doc.category} | `{doc.relative_path}` |"
        )
    return "\n".join(lines) + "\n"


def render_build_report(docs: list[Document], warnings: list[str], errors: list[str]) -> str:
    lines = [
        "# Build Report",
        "",
        f"Documents discovered: **{len(docs)}**",
        f"Warnings: **{len(warnings)}**",
        f"Errors: **{len(errors)}**",
        "",
        "## Errors",
        "",
    ]

    if errors:
        lines.extend(f"- {error}" for error in errors)
    else:
        lines.append("- None")

    lines.extend(["", "## Warnings", ""])

    if warnings:
        lines.extend(f"- {warning}" for warning in warnings)
    else:
        lines.append("- None")

    lines.extend(["", "## Documents", ""])

    for doc in sorted(docs, key=lambda d: d.title):
        lines.append(f"- [[{doc.title}]] — `{doc.relative_path}`")

    return "\n".join(lines) + "\n"
