from pathlib import Path
from textwrap import dedent


FOLDERS = [
    "source",
    "templates",
    "scripts",
    "packages",
    "dist/reports",
    "docs",
    "config",
    "tests",
    ".github/workflows",
]


FILES = {
    "docs/README.md": "# Repository Notes\n\nUse this folder for repository helper notes.\n",
    "packages/README.md": "# Packages\n\nPut downloaded CCTS package ZIP files here before running merge automation.\n",
    "config/build_config.yml": "release_name: v0.1-governance-draft\nsource_dir: source\ndist_dir: dist\n",
    "config/local.example.yml": "user_notes: local-only settings can go here\n",
}


def main() -> None:
    created = []
    skipped = []

    for folder in FOLDERS:
        path = Path(folder)
        path.mkdir(parents=True, exist_ok=True)
        created.append(str(path))

    for rel_path, content in FILES.items():
        path = Path(rel_path)
        if path.exists():
            skipped.append(str(path))
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        created.append(str(path))

    report = ["# Bootstrap Report", "", "## Created or Confirmed", ""]
    report.extend(f"- {item}" for item in created)
    report.extend(["", "## Skipped Existing Files", ""])
    report.extend(f"- {item}" for item in skipped) if skipped else report.append("- None")

    out = Path("dist/reports/bootstrap-report.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(report) + "\n", encoding="utf-8")

    print(out)


if __name__ == "__main__":
    main()
