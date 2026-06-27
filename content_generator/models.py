from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GeneratorConfig:
    """Runtime configuration loaded from `generator.yml`.

    Parameters
    ----------
    source_dir : pathlib.Path
        Directory where Markdown source files are discovered.
    site_file : pathlib.Path
        Project metadata file, usually `source/site.yml`.
    template_dir : pathlib.Path
        Directory containing Jinja2 templates.
    dist_dir : pathlib.Path
        Directory where generated outputs are written.
    vault_dir : pathlib.Path
        Generated Obsidian vault directory.
    index_note : pathlib.Path
        Vault-relative path for the main index note.
    pdf_file : pathlib.Path
        Dist-relative PDF output path.
    docx_file : pathlib.Path
        Dist-relative DOCX output path.
    generated_notes : dict[str, pathlib.Path]
        Named generated-note paths relative to the vault directory.
    frontmatter : dict[str, list[str]]
        Required, recommended, and optional frontmatter field groups.
    legacy_pages_dir : str
        Folder used to resolve bare `pages[].file` values.
    html_enabled : bool
        Whether `build_all` should generate the optional HTML website.
    html_dir : pathlib.Path
        Generated HTML website directory.
    """

    source_dir: Path
    site_file: Path
    template_dir: Path
    dist_dir: Path
    vault_dir: Path
    index_note: Path
    pdf_file: Path
    docx_file: Path
    generated_notes: dict[str, Path]
    frontmatter: dict[str, list[str]]
    legacy_pages_dir: str
    html_enabled: bool
    html_dir: Path


@dataclass(frozen=True)
class Page:
    """Markdown page loaded from the source directory.

    Parameters
    ----------
    title : str
        Human-readable page title.
    slug : str
        Filename stem used for the generated Obsidian note.
    tags : list[str]
        Obsidian/YAML tags attached to the generated note.
    frontmatter_lines : list[str]
        Pre-rendered YAML frontmatter lines in the required output order.
    body : str
        Markdown content loaded from a source document.
    source_path : pathlib.Path
        Source Markdown file path.
    relative_path : pathlib.Path
        Source path relative to `source/`, used to preserve vault folders.
    output_path : pathlib.Path
        Generated Obsidian note path relative to `dist/vault/`.
    metadata : dict
        Normalized page metadata used by dashboards and index notes.
    """

    title: str
    slug: str
    tags: list[str]
    frontmatter_lines: list[str]
    body: str
    source_path: Path
    relative_path: Path
    output_path: Path
    metadata: dict


@dataclass(frozen=True)
class Project:
    """Complete project configuration and loaded pages.

    Parameters
    ----------
    title : str
        Project title used in the index, PDF, and DOCX.
    subtitle : str
        Short description or deck line for generated documents.
    author : str
        Author name displayed in exported documents.
    pages : list[Page]
        Ordered page collection discovered from the source directory.
    """

    title: str
    subtitle: str
    author: str
    pages: list[Page]
