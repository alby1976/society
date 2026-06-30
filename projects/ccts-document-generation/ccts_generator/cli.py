import argparse
from pathlib import Path

from .config import BuildConfig
from .exporters import export_docx, export_html, export_pdf
from .links import check_links, render_missing_links_report
from .parser import discover_documents
from .render import copy_obsidian_vault, prepare_dist, render_build_report, render_registry
from .validators import validate_documents


def build(config: BuildConfig) -> int:
    prepare_dist(config)

    docs = discover_documents(config.source_dir)
    validation = validate_documents(docs)
    link_report = check_links(docs)

    copy_obsidian_vault(docs, config)

    config.registry_path.write_text(render_registry(docs, config), encoding="utf-8")
    config.missing_links_path.write_text(render_missing_links_report(link_report), encoding="utf-8")
    config.build_report_path.write_text(
        render_build_report(
            docs,
            warnings=validation.warnings + [
                f"Missing link [[{link}]] referenced from {', '.join(sources)}"
                for link, sources in sorted(link_report.missing_links.items())
            ],
            errors=validation.errors,
        ),
        encoding="utf-8",
    )

    export_html(docs, config)
    export_docx(docs, config)
    export_pdf(docs, config)

    print(f"Discovered {len(docs)} documents")
    print(f"Obsidian vault: {config.obsidian_dir}")
    print(f"Build report: {config.build_report_path}")
    print(f"Registry: {config.registry_path}")
    print(f"Missing links: {config.missing_links_path}")

    if validation.errors:
        print("Build completed with errors")
        return 1

    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the CCTS governance vault")
    parser.add_argument("--source", default="source", help="Source Markdown folder")
    parser.add_argument("--dist", default="dist", help="Output folder")
    args = parser.parse_args()

    dist = Path(args.dist)
    config = BuildConfig(
        source_dir=Path(args.source),
        dist_dir=dist,
        obsidian_dir=dist / "obsidian-vault",
        html_dir=dist / "html",
        docx_dir=dist / "docx",
        pdf_dir=dist / "pdf",
        reports_dir=dist / "reports",
    )

    raise SystemExit(build(config))


if __name__ == "__main__":
    main()
