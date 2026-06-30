from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZipFile


def find_source_members(zip_file: ZipFile) -> list[str]:
    members = []
    for name in zip_file.namelist():
        normalized = name.replace("\\", "/")
        if "/source/" in normalized and not normalized.endswith("/"):
            members.append(name)
    return members


def source_relative(member_name: str) -> Path:
    normalized = member_name.replace("\\", "/")
    after = normalized.split("/source/", 1)[1]
    return Path(after)


def merge_packages(packages_dir: Path, source_dir: Path, overwrite: bool = False) -> dict[str, list[str]]:
    source_dir.mkdir(parents=True, exist_ok=True)
    report = {
        "packages": [],
        "copied": [],
        "skipped": [],
        "errors": [],
    }

    for zip_path in sorted(packages_dir.glob("*.zip")):
        report["packages"].append(zip_path.name)

        try:
            with ZipFile(zip_path, "r") as z:
                members = find_source_members(z)
                if not members:
                    report["errors"].append(f"{zip_path.name}: no source/ files found")
                    continue

                for member in members:
                    rel = source_relative(member)
                    dest = source_dir / rel

                    if dest.exists() and not overwrite:
                        report["skipped"].append(f"{zip_path.name}: {rel}")
                        continue

                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(z.read(member))
                    report["copied"].append(f"{zip_path.name}: {rel}")

        except Exception as exc:
            report["errors"].append(f"{zip_path.name}: {exc}")

    return report


def write_report(report: dict[str, list[str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Package Merge Report", ""]

    for section in ["packages", "copied", "skipped", "errors"]:
        lines.append(f"## {section.title()}")
        lines.append("")
        items = report.get(section, [])
        if items:
            lines.extend(f"- {item}" for item in items)
        else:
            lines.append("- None")
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge CCTS package ZIP source folders into repository source/")
    parser.add_argument("packages_dir", help="Folder containing package ZIP files")
    parser.add_argument("--source", default="source", help="Destination source folder")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    report = merge_packages(Path(args.packages_dir), Path(args.source), overwrite=args.overwrite)
    report_path = Path("dist/reports/package-merge-report.md")
    write_report(report, report_path)

    print(f"Packages: {len(report['packages'])}")
    print(f"Copied: {len(report['copied'])}")
    print(f"Skipped: {len(report['skipped'])}")
    print(f"Errors: {len(report['errors'])}")
    print(f"Report: {report_path}")

    if report["errors"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
