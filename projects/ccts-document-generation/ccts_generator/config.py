from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BuildConfig:
    source_dir: Path = Path("source")
    dist_dir: Path = Path("dist")
    obsidian_dir: Path = Path("dist/obsidian-vault")
    html_dir: Path = Path("dist/html")
    docx_dir: Path = Path("dist/docx")
    pdf_dir: Path = Path("dist/pdf")
    reports_dir: Path = Path("dist/reports")
    templates_dir: Path = Path("templates")
    release_name: str = "v0.1-governance-draft"

    @property
    def registry_path(self) -> Path:
        return self.reports_dir / "generated-document-registry.md"

    @property
    def build_report_path(self) -> Path:
        return self.reports_dir / "build-report.md"

    @property
    def missing_links_path(self) -> Path:
        return self.reports_dir / "missing-links.md"
