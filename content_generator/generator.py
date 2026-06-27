"""Core project loader and generator orchestration.

Classes
-------
Generator
    Build the Obsidian vault, PDF, DOCX, generated governance notes, and
    optional HTML site from Markdown source files.

Functions
---------
load_generator_config
    Load runtime settings from `generator.yml`.
discover_markdown_files
    Recursively discover Markdown source files.
render_home_dashboard
    Render the generated metadata dashboard note.
"""

from pathlib import Path
from html import escape
import re
import shutil

try:
    import yaml
except ModuleNotFoundError:  # Keeps the starter runnable before dependencies are installed.
    yaml = None

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ModuleNotFoundError:
    Environment = FileSystemLoader = select_autoescape = None

from .models import GeneratorConfig, Page, Project
from .exporters import DocxExporter, PdfExporter

DEFAULT_GENERATOR_CONFIG = {
    "paths": {
        "source_dir": "source",
        "site_file": "source/site.yml",
        "template_dir": "templates",
        "dist_dir": "dist",
        "vault_dir": "dist/vault",
        "legacy_pages_dir": "pages",
    },
    "outputs": {
        "index_note": "00 Index.md",
        "pdf_file": "guide.pdf",
        "docx_file": "guide.docx",
    },
    "html": {
        "enabled": False,
        "html_dir": "dist/site",
    },
    "generated_notes": {
        "home_dashboard": "Home Dashboard.md",
        "governance_dashboard": "Governance Dashboard.md",
        "document_registry": "Document Registry.md",
        "decision_register": "Decision Register.md",
        "dependency_map": "Dependency Map.md",
        "link_validation_report": "Link Validation Report.md",
        "release_notes": "Release Notes.md",
        "changelog": "Changelog.md",
        "review_schedule": "Review Schedule.md",
        "international_dashboard": "International Dashboard.md",
        "index_by_category": "_indexes/By Category.md",
        "index_by_status": "_indexes/By Status.md",
        "index_by_type": "_indexes/By Type.md",
        "index_by_tag": "_indexes/By Tag.md",
        "index_by_jurisdiction": "_indexes/By Jurisdiction.md",
        "index_by_chapter": "_indexes/By Chapter.md",
        "dataview_queries": "_indexes/Dataview Queries.md",
    },
    "frontmatter": {
        "required": [
            "document-id",
            "title",
            "version",
            "status",
            "type",
            "document-category",
            "effective-date",
            "last-reviewed",
            "tags",
        ],
        "recommended": [
            "author",
            "next-review-date",
            "review-cycle",
            "approved-by",
            "authority-level",
            "related-documents",
            "owner",
            "decision-id",
            "dependencies",
            "changes",
            "jurisdiction",
            "chapter",
            "governance-level",
            "parent-document",
            "applies-to",
            "reserved-power",
            "local-adaptation",
        ],
        "optional": [
            "scriptural-foundation",
            "confessional-foundation",
            "supersedes",
        ],
    },
}


class Generator:
    """Build Obsidian, PDF, and DOCX outputs from source files.

    Parameters
    ----------
    root : pathlib.Path
        Project root containing `source/` and `templates/`.

    Attributes
    ----------
    source_dir : pathlib.Path
        Directory containing `site.yml` and page Markdown files.
    template_dir : pathlib.Path
        Directory containing Jinja2 templates for vault output.
    dist_dir : pathlib.Path
        Directory where generated outputs are written.
    vault_dir : pathlib.Path
        Destination directory for Obsidian Markdown notes.

    Examples
    --------
    Import and run the generator from another script::

        from pathlib import Path
        from content_generator import Generator

        project_root = Path("C:/docs/my-project")
        Generator(project_root).build_all()
    """

    def __init__(self, root: Path) -> None:
        """Initialize a generator for a project root.

        Parameters
        ----------
        root : pathlib.Path
            Folder containing `source/site.yml`, Markdown source files, and
            `templates/`.
        """
        self.root = root
        self.config = load_generator_config(root)
        self.source_dir = self.config.source_dir
        self.template_dir = self.config.template_dir
        self.dist_dir = self.config.dist_dir
        self.vault_dir = self.config.vault_dir
        self.env = None
        if Environment and FileSystemLoader and select_autoescape:
            self.env = Environment(
                loader=FileSystemLoader(self.template_dir),
                autoescape=select_autoescape(default_for_string=False),
                trim_blocks=True,
                lstrip_blocks=True,
            )

    def load_project(self) -> Project:
        """Load project metadata and Markdown page content.

        Returns
        -------
        Project
            Fully loaded project object containing page metadata and bodies.

        Raises
        ------
        FileNotFoundError
            If `source/site.yml` exists but a declared page file does not.
        KeyError
            If required project keys such as `title` are missing.
        """
        config = self.load_config()
        page_overrides = page_overrides_by_path(
            self.source_dir,
            config.get("pages", []),
            self.config.legacy_pages_dir,
        )
        markdown_files = discover_markdown_files(self.source_dir)
        ordered_files = order_markdown_files(markdown_files, page_overrides)

        pages = []
        for path in ordered_files:
            relative_path = path.relative_to(self.source_dir)
            frontmatter, body = split_markdown_frontmatter(path.read_text(encoding="utf-8"))
            item = merge_page_metadata(frontmatter, page_overrides.get(path.resolve(), {}), relative_path)
            slug = str(item.get("slug") or title_to_slug(item["title"]))
            output_path = relative_path.with_name(f"{slug}.md")
            pages.append(
                Page(
                    title=item["title"],
                    slug=slug,
                    tags=ensure_list(item.get("tags", [])),
                    frontmatter_lines=build_frontmatter_lines(item, self.config.frontmatter),
                    body=body.strip(),
                    source_path=path,
                    relative_path=relative_path,
                    output_path=output_path,
                    metadata=item,
                )
            )
        if not config.get("pages"):
            pages.sort(key=lambda page: page.output_path.as_posix().lower())
        return Project(
            title=config["title"],
            subtitle=config.get("subtitle", ""),
            author=config.get("author", ""),
            pages=pages,
        )

    def load_config(self) -> dict:
        """Load optional project metadata from `source/site.yml`.

        Returns
        -------
        dict
            Project configuration with default `title` and `pages` values.

        Notes
        -----
        The file is optional. When it is not present, the root directory name
        becomes the project title and pages are discovered only from Markdown
        files below `source/`.
        """
        config_path = self.config.site_file
        if not config_path.exists():
            return {"title": self.root.name, "pages": []}
        config_text = config_path.read_text(encoding="utf-8")
        config = yaml.safe_load(config_text) if yaml else parse_site_yml(config_text)
        if config is None:
            config = {}
        config.setdefault("title", self.root.name)
        config.setdefault("pages", [])
        return config

    def build_all(self) -> None:
        """Build all supported outputs.

        Returns
        -------
        None
            Output files are written to the configured distribution directory.

        Notes
        -----
        This method creates the Obsidian vault, PDF export, and DOCX export in
        `dist/`. It also builds the optional HTML site when enabled in
        `generator.yml`.
        """
        self.dist_dir.mkdir(exist_ok=True)
        self.build_vault()
        self.build_pdf()
        self.build_docx()
        if self.config.html_enabled:
            self.build_html()

    def build_vault(self) -> None:
        """Render the Obsidian Markdown vault.

        Returns
        -------
        None
            Vault Markdown files are written to the configured vault directory.

        Notes
        -----
        Jinja2 is used when installed. A small built-in renderer is used as a
        fallback so the starter kit can still run before dependencies are
        installed.
        """
        project = self.load_project()
        if self.vault_dir.exists():
            shutil.rmtree(self.vault_dir)
        self.vault_dir.mkdir(parents=True, exist_ok=True)
        (self.vault_dir / self.config.index_note).write_text(
            self.render_index(project),
            encoding="utf-8",
        )
        self.write_generated_notes(project)
        for page in project.pages:
            destination = self.vault_dir / page.output_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(
                self.render_page(project, page),
                encoding="utf-8",
            )

    def write_generated_notes(self, project: Project) -> None:
        """Write generated Obsidian support notes.

        Parameters
        ----------
        project : Project
            Loaded project whose page metadata powers the generated notes.

        Returns
        -------
        None
            Generated notes are written to the configured vault directory.

        Notes
        -----
        These notes are generated from metadata and are not controlled by the
        normal page template. They include the home dashboard, registries,
        release notes, and Dataview-ready indexes.
        """
        paths = self.config.generated_notes
        generated = {
            paths["home_dashboard"]: render_home_dashboard(project),
            paths["governance_dashboard"]: render_governance_dashboard(project),
            paths["document_registry"]: render_document_registry(project),
            paths["decision_register"]: render_decision_register(project),
            paths["dependency_map"]: render_dependency_map(project),
            paths["link_validation_report"]: render_link_validation_report(project),
            paths["release_notes"]: render_release_notes(project),
            paths["changelog"]: render_changelog(project),
            paths["review_schedule"]: render_review_schedule(project),
            paths["international_dashboard"]: render_international_dashboard(project),
            paths["index_by_category"]: render_field_index(project, "document-category", "Documents by Category"),
            paths["index_by_status"]: render_field_index(project, "status", "Documents by Status"),
            paths["index_by_type"]: render_field_index(project, "type", "Documents by Type"),
            paths["index_by_tag"]: render_tag_index(project),
            paths["index_by_jurisdiction"]: render_field_index(
                project,
                "jurisdiction",
                "Documents by Jurisdiction",
                include_unspecified=False,
            ),
            paths["index_by_chapter"]: render_field_index(
                project,
                "chapter",
                "Documents by Chapter",
                include_unspecified=False,
            ),
            paths["dataview_queries"]: render_dataview_queries(project),
        }
        for relative_path, text in generated.items():
            destination = self.vault_dir / relative_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(text, encoding="utf-8")

    def build_pdf(self) -> None:
        """Generate `dist/guide.pdf` from the loaded project.

        Returns
        -------
        None
            The PDF file is written to the configured distribution directory.

        Notes
        -----
        Markdown files are loaded fresh for this export so the PDF reflects the
        same auto-discovered source set as the Obsidian vault.
        """
        project = self.load_project()
        self.dist_dir.mkdir(exist_ok=True)
        PdfExporter(project).write(self.dist_dir / self.config.pdf_file)

    def build_docx(self) -> None:
        """Generate `dist/guide.docx` from the loaded project.

        Returns
        -------
        None
            The DOCX file is written to the configured distribution directory.

        Notes
        -----
        Markdown files are loaded fresh for this export so the Word document
        reflects the same auto-discovered source set as the Obsidian vault.
        """
        project = self.load_project()
        self.dist_dir.mkdir(exist_ok=True)
        DocxExporter(project).write(self.dist_dir / self.config.docx_file)

    def build_html(self) -> None:
        """Generate the optional static HTML website.

        Returns
        -------
        None
            HTML files are written to the configured HTML directory.

        Notes
        -----
        HTML generation is intentionally small and dependency-free. It writes
        one `index.html` file and one page per source document.
        """
        project = self.load_project()
        self.config.html_dir.mkdir(parents=True, exist_ok=True)
        for html_file in self.config.html_dir.rglob("*.html"):
            html_file.unlink()
        write_html_site(project, self.config.html_dir)

    def render_index(self, project: Project) -> str:
        """Render the Obsidian index note.

        Parameters
        ----------
        project : Project
            Project to render.

        Returns
        -------
        str
            Markdown text for `00 Index.md`.
        """
        if self.env:
            return self.env.get_template("index.md.j2").render(project=project)
        page_links = "\n".join(f"- {obsidian_link(page)}" for page in project.pages)
        author = f"Prepared by {project.author}\n\n" if project.author else ""
        return (
            f"---\ntitle: {project.title}\ntype: index\n---\n\n"
            f"# {project.title}\n\n{project.subtitle}\n\n{author}## Pages\n\n{page_links}\n"
        )

    def render_page(self, project: Project, page: Page) -> str:
        """Render one Obsidian page note.

        Parameters
        ----------
        project : Project
            Parent project. Included for template context.
        page : Page
            Page to render.

        Returns
        -------
        str
            Markdown text for the generated page note.
        """
        if self.env:
            return self.env.get_template("page.md.j2").render(project=project, page=page)
        frontmatter = "\n".join(page.frontmatter_lines)
        return (
            f"---\n{frontmatter}\n---\n\n"
            f"# {page.title}\n\n{page.body}\n"
        )


def load_generator_config(root: Path) -> GeneratorConfig:
    """Load runtime generator settings from `generator.yml`.

    Parameters
    ----------
    root : pathlib.Path
        Project root to inspect.

    Returns
    -------
    GeneratorConfig
        Resolved generator paths and field settings.

    Notes
    -----
    Missing settings fall back to `DEFAULT_GENERATOR_CONFIG`, so projects can
    include only the values they want to customize.
    """
    config_path = root / "generator.yml"
    raw_config = {}
    if config_path.exists() and yaml:
        raw_config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    elif config_path.exists():
        raw_config = parse_site_yml(config_path.read_text(encoding="utf-8"))

    merged = deep_merge(DEFAULT_GENERATOR_CONFIG, raw_config)
    paths = merged["paths"]
    outputs = merged["outputs"]
    generated_notes = merged["generated_notes"]

    return GeneratorConfig(
        source_dir=root / paths["source_dir"],
        site_file=root / paths["site_file"],
        template_dir=root / paths["template_dir"],
        dist_dir=root / paths["dist_dir"],
        vault_dir=root / paths["vault_dir"],
        index_note=Path(outputs["index_note"]),
        pdf_file=Path(outputs["pdf_file"]),
        docx_file=Path(outputs["docx_file"]),
        generated_notes={key: Path(value) for key, value in generated_notes.items()},
        frontmatter=merged["frontmatter"],
        legacy_pages_dir=str(paths["legacy_pages_dir"]),
        html_enabled=bool(merged.get("html", {}).get("enabled", False)),
        html_dir=root / merged.get("html", {}).get("html_dir", "dist/site"),
    )


def deep_merge(base: dict, override: dict) -> dict:
    """Merge nested configuration dictionaries.

    Parameters
    ----------
    base : dict
        Default configuration.
    override : dict
        User-supplied configuration values.

    Returns
    -------
    dict
        New dictionary containing `base` with `override` values applied.
    """
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def discover_markdown_files(source_dir: Path) -> list[Path]:
    """Return Markdown files discovered below a source directory.

    Parameters
    ----------
    source_dir : pathlib.Path
        Directory to scan recursively.

    Returns
    -------
    list[pathlib.Path]
        Sorted Markdown file paths, excluding files in hidden directories.
    """
    return sorted(
        path for path in source_dir.rglob("*.md")
        if path.is_file() and not any(part.startswith(".") for part in path.parts)
    )


def page_overrides_by_path(source_dir: Path, pages: list[dict], legacy_pages_dir: str) -> dict[Path, dict]:
    """Index optional `site.yml` page metadata by source path.

    Parameters
    ----------
    source_dir : pathlib.Path
        Root source directory used to resolve page file paths.
    pages : list[dict]
        Optional page override entries from `source/site.yml`.
    legacy_pages_dir : str
        Source-relative folder used to resolve bare filenames.

    Returns
    -------
    dict[pathlib.Path, dict]
        Mapping of resolved source file paths to override metadata.

    Notes
    -----
    Bare filenames are resolved against the configured legacy pages directory
    for compatibility with older projects. Nested paths are resolved against
    `source/`.
    """
    overrides: dict[Path, dict] = {}
    for item in pages:
        file_value = item.get("file")
        if not file_value:
            continue
        relative = Path(str(file_value))
        candidates = [Path(legacy_pages_dir) / relative] if len(relative.parts) == 1 else [relative]
        candidates.append(relative)
        for candidate in candidates:
            overrides[(source_dir / candidate).resolve()] = item
    return overrides


def order_markdown_files(markdown_files: list[Path], overrides: dict[Path, dict]) -> list[Path]:
    """Order Markdown files using optional `site.yml` overrides.

    Parameters
    ----------
    markdown_files : list[pathlib.Path]
        Auto-discovered Markdown files.
    overrides : dict[pathlib.Path, dict]
        Metadata overrides keyed by resolved source file path.

    Returns
    -------
    list[pathlib.Path]
        Ordered Markdown files. Files listed in `site.yml` come first, followed
        by remaining discovered files.
    """
    file_by_resolved = {path.resolve(): path for path in markdown_files}
    ordered: list[Path] = []
    for resolved in overrides:
        path = file_by_resolved.get(resolved)
        if path and path not in ordered:
            ordered.append(path)
    ordered.extend(path for path in markdown_files if path not in ordered)
    return ordered


def split_markdown_frontmatter(text: str) -> tuple[dict, str]:
    """Split a Markdown document into frontmatter and body text.

    Parameters
    ----------
    text : str
        Full Markdown file content.

    Returns
    -------
    tuple[dict, str]
        Parsed YAML frontmatter metadata and Markdown body text. When no valid
        frontmatter block exists, the metadata dictionary is empty.
    """
    if not text.startswith("---"):
        return {}, text
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not match:
        return {}, text
    frontmatter_text, body = match.groups()
    if yaml:
        metadata = yaml.safe_load(frontmatter_text) or {}
    else:
        metadata = parse_simple_frontmatter(frontmatter_text)
    return metadata, body


def parse_simple_frontmatter(text: str) -> dict:
    """Parse a small YAML frontmatter subset when PyYAML is unavailable.

    Parameters
    ----------
    text : str
        Frontmatter text without the opening or closing `---` delimiters.

    Returns
    -------
    dict
        Parsed scalar and inline-list metadata.

    Notes
    -----
    This fallback is intentionally limited. Install PyYAML for full YAML
    support, including nested structures and block lists.
    """
    metadata = {}
    for raw in text.splitlines():
        if not raw.strip() or raw.strip().startswith("#") or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        metadata[key.strip()] = clean_scalar(value)
    return metadata


def merge_page_metadata(frontmatter: dict, override: dict, relative_path: Path) -> dict:
    """Merge source metadata, config overrides, and derived defaults.

    Parameters
    ----------
    frontmatter : dict
        Metadata parsed from a Markdown file.
    override : dict
        Optional metadata entry from `source/site.yml`.
    relative_path : pathlib.Path
        Markdown file path relative to `source/`.

    Returns
    -------
    dict
        Complete page metadata with derived `title` and `slug` defaults.
    """
    item = dict(frontmatter)
    item.update({key: value for key, value in override.items() if key != "file"})
    item.setdefault("title", title_from_path(relative_path))
    item.setdefault("slug", title_to_slug(str(item["title"])))
    return item


def title_from_path(path: Path) -> str:
    """Create a readable title from a Markdown file path.

    Parameters
    ----------
    path : pathlib.Path
        Markdown file path.

    Returns
    -------
    str
        Title-cased filename stem with hyphens and underscores replaced.
    """
    return path.stem.replace("-", " ").replace("_", " ").title()


def title_to_slug(title: str) -> str:
    """Create a filesystem-friendly note slug from a title.

    Parameters
    ----------
    title : str
        Human-readable title.

    Returns
    -------
    str
        Slug suitable for use as a Markdown filename stem.
    """
    slug = re.sub(r"[^\w .()-]+", "", title).strip()
    return slug or "Untitled"


def ensure_list(value: object) -> list[str]:
    """Normalize scalars and missing values to a list of strings.

    Parameters
    ----------
    value : object
        Metadata value that may be missing, scalar, or list-like.

    Returns
    -------
    list[str]
        Normalized string list.
    """
    if is_blank(value):
        return []
    if isinstance(value, list):
        return [str(item) for item in value if not is_blank(item)]
    return [str(value)]


def obsidian_link(page: Page) -> str:
    """Return an Obsidian wiki link for a generated page.

    Parameters
    ----------
    page : Page
        Page to link to.

    Returns
    -------
    str
        Wiki link using the generated vault path and page title.
    """
    return f"[[{page.output_path.as_posix()}|{page.title}]]"


def metadata_value(page: Page, key: str, default: str = "") -> str:
    """Return one displayable metadata value.

    Parameters
    ----------
    page : Page
        Page whose metadata should be read.
    key : str
        Metadata key to read.
    default : str, optional
        Value to display when the key is missing.

    Returns
    -------
    str
        String value suitable for Markdown tables and lists.
    """
    value = page.metadata.get(key, default)
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return str(value) if value is not None else default


def owner_value(page: Page) -> str:
    """Return the document owner value.

    Parameters
    ----------
    page : Page
        Page whose owner metadata should be read.

    Returns
    -------
    str
        `owner` metadata when present, otherwise `author`.
    """
    return metadata_value(page, "owner") or metadata_value(page, "author")


def review_date_value(page: Page) -> str:
    """Return the next review date or last reviewed date.

    Parameters
    ----------
    page : Page
        Page whose review metadata should be read.

    Returns
    -------
    str
        `next-review-date` when present, otherwise `last-reviewed`.
    """
    return metadata_value(page, "next-review-date") or metadata_value(page, "last-reviewed")


def page_aliases(page: Page) -> set[str]:
    """Return names that may refer to a page in wiki links.

    Parameters
    ----------
    page : Page
        Page to index.

    Returns
    -------
    set[str]
        Link aliases based on title, slug, output path, and filename stems.
    """
    return {
        page.title,
        page.slug,
        page.source_path.stem,
        page.relative_path.as_posix(),
        page.output_path.as_posix(),
        page.output_path.stem,
    }


def resolve_page_reference(project: Project, reference: str) -> Page | None:
    """Resolve a wiki link or dependency value to a project page.

    Parameters
    ----------
    project : Project
        Project to search.
    reference : str
        Link target or dependency text.

    Returns
    -------
    Page or None
        Matched page, when one can be found.
    """
    clean = reference.strip().strip('"')
    if clean.startswith("[[") and clean.endswith("]]"):
        clean = clean[2:-2]
    clean = clean.split("|", 1)[0].split("#", 1)[0].strip()
    for page in project.pages:
        if clean in page_aliases(page):
            return page
    return None


def wiki_links(text: str) -> list[str]:
    """Extract Obsidian wiki link targets from text.

    Parameters
    ----------
    text : str
        Markdown or metadata text to inspect.

    Returns
    -------
    list[str]
        Raw wiki link targets without surrounding brackets.
    """
    return re.findall(r"\[\[([^\]]+)\]\]", text)


def page_outgoing_references(page: Page) -> list[str]:
    """Return outgoing wiki links and dependencies for one page.

    Parameters
    ----------
    page : Page
        Page to inspect.

    Returns
    -------
    list[str]
        Referenced link/dependency targets.
    """
    references = wiki_links(page.body)
    for value in page.metadata.values():
        if isinstance(value, list):
            for item in value:
                references.extend(wiki_links(str(item)))
        else:
            references.extend(wiki_links(str(value)))
    references.extend(ensure_list(page.metadata.get("dependencies", [])))
    return references


def page_wiki_references(page: Page) -> list[str]:
    """Return explicit Obsidian wiki links from body and metadata.

    Parameters
    ----------
    page : Page
        Page to inspect.

    Returns
    -------
    list[str]
        Explicit `[[...]]` references only.
    """
    references = wiki_links(page.body)
    for value in page.metadata.values():
        if isinstance(value, list):
            for item in value:
                references.extend(wiki_links(str(item)))
        else:
            references.extend(wiki_links(str(value)))
    return references


def validate_parent_document_links(project: Project) -> list[str]:
    """Validate chapter documents against their international parent documents.

    Parameters
    ----------
    project : Project
        Project to validate.

    Returns
    -------
    list[str]
        Markdown bullet lines describing missing, unresolved, or non-linked
        `parent-document` metadata.
    """
    issues: list[str] = []
    for page in international_pages(project):
        if not requires_parent_document(page):
            continue
        parent_references = ensure_list(page.metadata.get("parent-document", []))
        if not parent_references:
            issues.append(f"- {obsidian_link(page)} is a chapter document without `parent-document`.")
            continue
        explicit_links = page_wiki_references(page)
        for reference in parent_references:
            parent = resolve_page_reference(project, reference)
            if not parent:
                issues.append(f"- {obsidian_link(page)} has unresolved `parent-document`: `{reference}`.")
                continue
            links_to_parent = any(resolve_page_reference(project, link) is parent for link in explicit_links)
            if not links_to_parent:
                issues.append(
                    f"- {obsidian_link(page)} declares parent {obsidian_link(parent)} "
                    "but does not include a wiki link back to it."
                )
    return issues


def requires_parent_document(page: Page) -> bool:
    """Return whether a document should link to an international parent.

    Parameters
    ----------
    page : Page
        Page to inspect.

    Returns
    -------
    bool
        True for chapter/local documents and false for international/global
        parent documents.
    """
    governance_level = metadata_value(page, "governance-level").strip().lower()
    chapter = metadata_value(page, "chapter").strip().lower()
    if governance_level and governance_level != "international":
        return True
    if chapter and chapter != "global":
        return True
    return False


def render_home_dashboard(project: Project) -> str:
    """Render the generated home dashboard note.

    Parameters
    ----------
    project : Project
        Loaded project to summarize.

    Returns
    -------
    str
        Markdown text for `Home Dashboard.md`.
    """
    status_lines = render_count_list(count_by_field(project.pages, "status"))
    category_lines = render_grouped_links(project, "document-category")
    type_lines = render_grouped_links(project, "type")
    recent = sorted(project.pages, key=lambda page: metadata_value(page, "last-reviewed"), reverse=True)[:10]
    recent_lines = "\n".join(f"- {obsidian_link(page)} - reviewed {metadata_value(page, 'last-reviewed', 'unknown')}" for page in recent)
    return (
        "---\ntitle: Home Dashboard\ntype: dashboard\n---\n\n"
        "# Home Dashboard\n\n"
        f"Project: {project.title}\n\n"
        "## Status\n\n"
        f"{status_lines}\n\n"
        "## Categories\n\n"
        f"{category_lines}\n\n"
        "## Types\n\n"
        f"{type_lines}\n\n"
        "## Recently Reviewed\n\n"
        f"{recent_lines}\n\n"
        "## Dataview\n\n"
        "```dataview\n"
        "TABLE status, type, document-category, last-reviewed\n"
        "FROM \"\"\n"
        "WHERE type != \"dashboard\" AND type != \"index\"\n"
        "SORT last-reviewed DESC\n"
        "```\n"
    )


def render_governance_dashboard(project: Project) -> str:
    """Render a governance dashboard with Dataview-ready sections.

    Parameters
    ----------
    project : Project
        Loaded project to summarize.

    Returns
    -------
    str
        Markdown text for `Governance Dashboard.md`.
    """
    return (
        "---\ntitle: Governance Dashboard\ntype: dashboard\n---\n\n"
        "# Governance Dashboard\n\n"
        f"- Documents: {len(project.pages)}\n"
        f"- Decisions: {len(decision_pages(project))}\n"
        f"- Drafts: {count_by_field(project.pages, 'status').get('draft', 0)}\n\n"
        "## Documents Needing Review\n\n"
        "```dataview\n"
        "TABLE next-review-date, owner, status\n"
        "FROM \"\"\n"
        "WHERE next-review-date AND date(next-review-date) <= date(today)\n"
        "SORT next-review-date ASC\n"
        "```\n\n"
        "## Policies Approved This Year\n\n"
        "```dataview\n"
        "TABLE effective-date, version, approved-by\n"
        "FROM \"\"\n"
        "WHERE type = \"policy\" AND startswith(string(effective-date), string(date(today).year))\n"
        "SORT effective-date DESC\n"
        "```\n\n"
        "## Draft Documents\n\n"
        "```dataview\n"
        "TABLE type, document-category, owner, last-reviewed\n"
        "FROM \"\"\n"
        "WHERE status = \"draft\"\n"
        "SORT title ASC\n"
        "```\n\n"
        "## Theology Documents\n\n"
        "```dataview\n"
        "TABLE status, version, owner\n"
        "FROM \"\"\n"
        "WHERE contains(tags, \"theology\") OR document-category = \"theology\"\n"
        "SORT title ASC\n"
        "```\n\n"
        "## Housing Documents\n\n"
        "```dataview\n"
        "TABLE status, version, owner\n"
        "FROM \"\"\n"
        "WHERE contains(tags, \"housing\") OR document-category = \"housing\"\n"
        "SORT title ASC\n"
        "```\n"
    )


def render_international_dashboard(project: Project) -> str:
    """Render a dashboard for international and chapter governance documents.

    Parameters
    ----------
    project : Project
        Loaded project to summarize.

    Returns
    -------
    str
        Markdown text for `International Dashboard.md`.
    """
    pages = international_pages(project)
    jurisdiction_lines = render_count_list(count_by_field(pages, "jurisdiction"))
    chapter_lines = render_count_list(count_by_field(pages, "chapter"))
    governance_level_lines = render_count_list(count_by_field(pages, "governance-level"))
    parent_lines = "\n".join(
        f"- {obsidian_link(page)} -> {parent_document_text(project, page)}"
        for page in pages
        if not is_blank(page.metadata.get("parent-document"))
    )
    return (
        "---\ntitle: International Dashboard\ntype: dashboard\n---\n\n"
        "# International Dashboard\n\n"
        f"- International documents: {len(pages)}\n"
        f"- Jurisdictions: {len(count_by_field(pages, 'jurisdiction'))}\n"
        f"- Chapters: {len(count_by_field(pages, 'chapter'))}\n\n"
        "## Jurisdictions\n\n"
        f"{jurisdiction_lines}\n\n"
        "## Chapters\n\n"
        f"{chapter_lines}\n\n"
        "## Governance Levels\n\n"
        f"{governance_level_lines}\n\n"
        "## Parent Documents\n\n"
        f"{parent_lines or '- None'}\n\n"
        "## Dataview\n\n"
        "```dataview\n"
        "TABLE jurisdiction, chapter, governance-level, parent-document, applies-to, status, version\n"
        "FROM \"\"\n"
        "WHERE jurisdiction OR chapter OR governance-level\n"
        "SORT jurisdiction ASC, chapter ASC, title ASC\n"
        "```\n"
    )


def render_document_registry(project: Project) -> str:
    """Render a document registry note with static and Dataview tables.

    Parameters
    ----------
    project : Project
        Loaded project to register.

    Returns
    -------
    str
        Markdown text for `Document Registry.md`.
    """
    rows = [
        "| Document ID | Document | Status | Version | Owner | Review Date | Type | Category |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for page in project.pages:
        rows.append(
            "| "
            + " | ".join(
                [
                    metadata_value(page, "document-id"),
                    obsidian_link(page),
                    metadata_value(page, "status"),
                    metadata_value(page, "version"),
                    owner_value(page),
                    review_date_value(page),
                    metadata_value(page, "type"),
                    metadata_value(page, "document-category"),
                ]
            )
            + " |"
        )
    return (
        "---\ntitle: Document Registry\ntype: registry\n---\n\n"
        "# Document Registry\n\n"
        + "\n".join(rows)
        + "\n\n## Dataview\n\n"
        "```dataview\n"
        "TABLE document-id, status, version, owner, author, next-review-date, last-reviewed, type, document-category\n"
        "FROM \"\"\n"
        "WHERE version\n"
        "SORT document-category ASC, title ASC\n"
        "```\n"
    )


def render_decision_register(project: Project) -> str:
    """Render documents that are decisions or approval-bearing records.

    Parameters
    ----------
    project : Project
        Loaded project to inspect.

    Returns
    -------
    str
        Markdown text for `Decision Register.md`.
    """
    lines = [
        "| Decision ID | Document ID | Decision | Status | Authority | Approved By | Effective Date | Related Documents |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for page in decision_pages(project):
        lines.append(
            "| "
            + " | ".join(
                [
                    metadata_value(page, "decision-id"),
                    metadata_value(page, "document-id"),
                    obsidian_link(page),
                    metadata_value(page, "status"),
                    metadata_value(page, "authority-level"),
                    metadata_value(page, "approved-by"),
                    metadata_value(page, "effective-date"),
                    metadata_value(page, "related-documents"),
                ]
            )
            + " |"
        )
    return (
        "---\ntitle: Decision Register\ntype: register\n---\n\n"
        "# Decision Register\n\n"
        + "\n".join(lines)
        + "\n\n## Dataview\n\n"
        "```dataview\n"
        "TABLE decision-id, document-id, status, authority-level, approved-by, effective-date, related-documents\n"
        "FROM \"\"\n"
        "WHERE decision-id OR type = \"decision\"\n"
        "SORT effective-date DESC\n"
        "```\n"
    )


def render_dependency_map(project: Project) -> str:
    """Render dependency links and a Mermaid dependency graph.

    Parameters
    ----------
    project : Project
        Loaded project to inspect.

    Returns
    -------
    str
        Markdown text for `Dependency Map.md`.
    """
    edges: list[tuple[Page, Page | str]] = []
    for page in project.pages:
        for dependency in ensure_list(page.metadata.get("dependencies", [])):
            target = resolve_page_reference(project, dependency)
            edges.append((page, target or dependency))

    lines = ["---", "title: Dependency Map", "type: dependency-map", "---", "", "# Dependency Map", ""]
    lines.extend(render_dependency_lines(edges))
    lines.extend(["", "## Mermaid", "", "```mermaid", "graph TD"])
    if edges:
        for page, target in edges:
            target_label = target.title if isinstance(target, Page) else str(target)
            lines.append(f"  {mermaid_node(target_label)} --> {mermaid_node(page.title)}")
    else:
        lines.append("  No_dependencies[No dependencies declared]")
    lines.extend(["```", ""])
    return "\n".join(lines)


def render_link_validation_report(project: Project) -> str:
    """Render missing links, broken dependencies, and orphan documents.

    Parameters
    ----------
    project : Project
        Loaded project to validate.

    Returns
    -------
    str
        Markdown text for `Link Validation Report.md`.
    """
    incoming: dict[Path, int] = {page.output_path: 0 for page in project.pages}
    missing: list[str] = []
    seen_missing: set[tuple[Path, str]] = set()
    for page in project.pages:
        for reference in page_outgoing_references(page):
            target = resolve_page_reference(project, reference)
            if target:
                incoming[target.output_path] += 1
            else:
                key = (page.output_path, reference)
                if key not in seen_missing:
                    seen_missing.add(key)
                    missing.append(f"- {obsidian_link(page)} -> `{reference}`")
    orphan_lines = [
        f"- {obsidian_link(page)}"
        for page in project.pages
        if incoming[page.output_path] == 0 and page is not project.pages[0]
    ]
    parent_issues = validate_parent_document_links(project)
    return (
        "---\ntitle: Link Validation Report\ntype: validation-report\n---\n\n"
        "# Link Validation Report\n\n"
        "## Missing Or Broken Links\n\n"
        + ("\n".join(missing) if missing else "No missing links found.")
        + "\n\n## International Parent Links\n\n"
        + ("\n".join(parent_issues) if parent_issues else "All chapter parent links are valid.")
        + "\n\n## Orphan Documents\n\n"
        + ("\n".join(orphan_lines) if orphan_lines else "No orphan documents found.")
        + "\n"
    )


def render_release_notes(project: Project) -> str:
    """Render release notes grouped by effective date.

    Parameters
    ----------
    project : Project
        Loaded project to summarize.

    Returns
    -------
    str
        Markdown text for `Release Notes.md`.
    """
    lines = ["---", "title: Release Notes", "type: release-notes", "---", "", "# Release Notes", ""]
    for page in sorted(project.pages, key=lambda item: metadata_value(item, "effective-date"), reverse=True):
        lines.append(
            f"- {metadata_value(page, 'effective-date', 'undated')} - "
            f"{metadata_value(page, 'document-id', 'no-id')} - {obsidian_link(page)} "
            f"v{metadata_value(page, 'version', 'unknown')} "
            f"({metadata_value(page, 'status', 'unknown')})"
        )
    lines.extend(
        [
            "",
            "## Dataview",
            "",
            "```dataview",
            "TABLE document-id, version, status, effective-date, last-reviewed",
            "FROM \"\"",
            "WHERE version",
            "SORT effective-date DESC",
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def render_changelog(project: Project) -> str:
    """Render a changelog from document change metadata.

    Parameters
    ----------
    project : Project
        Loaded project to summarize.

    Returns
    -------
    str
        Markdown text for `Changelog.md`.
    """
    lines = ["---", "title: Changelog", "type: changelog", "---", "", "# Changelog", ""]
    entries = sorted(changelog_entries(project), key=lambda item: item["date"], reverse=True)
    for entry in entries:
        lines.append(format_changelog_entry(entry))
    lines.extend(
        [
            "",
            "## Dataview",
            "",
            "```dataview",
            "TABLE document-id, version, status, last-reviewed, changes",
            "FROM \"\"",
            "WHERE changes OR version",
            "SORT last-reviewed DESC",
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def render_review_schedule(project: Project) -> str:
    """Render a review schedule from review metadata.

    Parameters
    ----------
    project : Project
        Loaded project to schedule.

    Returns
    -------
    str
        Markdown text for `Review Schedule.md`.
    """
    lines = [
        "---",
        "title: Review Schedule",
        "type: review-schedule",
        "---",
        "",
        "# Review Schedule",
        "",
        "| Document ID | Document | Owner | Last Reviewed | Next Review | Status |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for page in sorted(project.pages, key=lambda item: review_date_value(item)):
        lines.append(
            f"| {metadata_value(page, 'document-id')} | {obsidian_link(page)} | {owner_value(page)} | "
            f"{metadata_value(page, 'last-reviewed')} | {metadata_value(page, 'next-review-date')} | "
            f"{metadata_value(page, 'status')} |"
        )
    lines.extend(
        [
            "",
            "## Dataview",
            "",
            "```dataview",
            "TABLE document-id, owner, author, last-reviewed, next-review-date, status",
            "FROM \"\"",
            "WHERE next-review-date OR last-reviewed",
            "SORT next-review-date ASC",
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def changelog_entries(project: Project) -> list[dict[str, str]]:
    """Return normalized changelog entries for all pages.

    Parameters
    ----------
    project : Project
        Project whose pages should be summarized.

    Returns
    -------
    list[dict[str, str]]
        Normalized changelog entries containing date, document metadata, and
        summary text.

    Notes
    -----
    Authors can provide `changes` in YAML frontmatter as a list of strings or a
    list of mappings. When `changes` is absent, the current document version is
    used as a fallback entry.
    """
    entries: list[dict[str, str]] = []
    for page in project.pages:
        changes = page.metadata.get("changes")
        if isinstance(changes, list) and changes:
            for change in changes:
                entries.append(normalize_change_entry(page, change))
        elif isinstance(changes, str) and changes.strip():
            entries.append(normalize_change_entry(page, changes))
        else:
            entries.append(
                {
                    "date": metadata_value(page, "last-reviewed", "undated"),
                    "document_id": metadata_value(page, "document-id", "no-id"),
                    "document": obsidian_link(page),
                    "version": metadata_value(page, "version", "unknown"),
                    "status": metadata_value(page, "status", "unknown"),
                    "summary": "Current published metadata.",
                }
            )
    return entries


def normalize_change_entry(page: Page, change: object) -> dict[str, str]:
    """Normalize one YAML change entry.

    Parameters
    ----------
    page : Page
        Page that owns the change entry.
    change : object
        String or mapping from the page's `changes` metadata.

    Returns
    -------
    dict[str, str]
        Normalized changelog entry.
    """
    if isinstance(change, dict):
        summary = change.get("summary") or change.get("description") or change.get("change") or ""
        return {
            "date": str(change.get("date") or metadata_value(page, "last-reviewed", "undated")),
            "document_id": metadata_value(page, "document-id", "no-id"),
            "document": obsidian_link(page),
            "version": str(change.get("version") or metadata_value(page, "version", "unknown")),
            "status": str(change.get("status") or metadata_value(page, "status", "unknown")),
            "summary": str(summary or "Updated document."),
        }
    return {
        "date": metadata_value(page, "last-reviewed", "undated"),
        "document_id": metadata_value(page, "document-id", "no-id"),
        "document": obsidian_link(page),
        "version": metadata_value(page, "version", "unknown"),
        "status": metadata_value(page, "status", "unknown"),
        "summary": str(change),
    }


def format_changelog_entry(entry: dict[str, str]) -> str:
    """Format one normalized changelog entry.

    Parameters
    ----------
    entry : dict[str, str]
        Normalized changelog entry.

    Returns
    -------
    str
        Markdown bullet line for `Changelog.md`.
    """
    return (
        f"- {entry['date']} - {entry['document_id']} - {entry['document']} "
        f"v{entry['version']} ({entry['status']}) - {entry['summary']}"
    )


def render_field_index(
    project: Project,
    field: str,
    title: str,
    include_unspecified: bool = True,
) -> str:
    """Render a grouped field index note.

    Parameters
    ----------
    project : Project
        Loaded project to index.
    field : str
        Metadata field to group by.
    title : str
        Note title.
    include_unspecified : bool, optional
        Include documents without this metadata field.

    Returns
    -------
    str
        Markdown text for one generated field index.
    """
    groups: dict[str, list[Page]] = {}
    for page in project.pages:
        value = metadata_value(page, field, "Unspecified")
        if not include_unspecified and value == "Unspecified":
            continue
        groups.setdefault(value, []).append(page)
    lines = ["---", f"title: {title}", "type: index", "---", "", f"# {title}", ""]
    for group, pages in sorted(groups.items()):
        lines.extend([f"## {group}", ""])
        lines.extend(f"- {obsidian_link(page)}" for page in pages)
        lines.append("")
    if not groups:
        lines.extend(["No documents found.", ""])
    lines.extend(
        [
            "## Dataview",
            "",
            "```dataview",
            f"TABLE title, status, version, {field}",
            "FROM \"\"",
            f"WHERE {field}",
            f"SORT {field} ASC, title ASC",
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def render_tag_index(project: Project) -> str:
    """Render a grouped tag index note.

    Parameters
    ----------
    project : Project
        Loaded project to index.

    Returns
    -------
    str
        Markdown text for `_indexes/By Tag.md`.
    """
    groups: dict[str, list[Page]] = {}
    for page in project.pages:
        for tag in page.tags:
            groups.setdefault(tag, []).append(page)
    lines = ["---", "title: Documents by Tag", "type: index", "---", "", "# Documents by Tag", ""]
    for tag, pages in sorted(groups.items()):
        lines.extend([f"## #{tag}", ""])
        lines.extend(f"- {obsidian_link(page)}" for page in pages)
        lines.append("")
    lines.extend(
        [
            "## Dataview",
            "",
            "```dataview",
            "TABLE file.tags, status, version",
            "FROM \"\"",
            "WHERE version",
            "SORT title ASC",
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def render_dataview_queries(project: Project) -> str:
    """Render reusable Dataview query snippets.

    Parameters
    ----------
    project : Project
        Loaded project. Included for a consistent generated-note API.

    Returns
    -------
    str
        Markdown text for `_indexes/Dataview Queries.md`.
    """
    return (
        "---\ntitle: Dataview Queries\ntype: index\n---\n\n"
        "# Dataview Queries\n\n"
        "## Review Queue\n\n"
        "```dataview\n"
        "TABLE next-review-date, owner, status\n"
        "FROM \"\"\n"
        "WHERE next-review-date\n"
        "SORT next-review-date ASC\n"
        "```\n\n"
        "## Approved Documents\n\n"
        "```dataview\n"
        "LIST FROM \"\" WHERE status = \"approved\" SORT title ASC\n"
        "```\n\n"
        "## Superseded Documents\n\n"
        "```dataview\n"
        "TABLE supersedes, version, effective-date\n"
        "FROM \"\"\n"
        "WHERE supersedes\n"
        "SORT effective-date DESC\n"
        "```\n\n"
        "## Policies Approved This Year\n\n"
        "```dataview\n"
        "TABLE effective-date, version, approved-by\n"
        "FROM \"\"\n"
        "WHERE type = \"policy\" AND startswith(string(effective-date), string(date(today).year))\n"
        "SORT effective-date DESC\n"
        "```\n\n"
        "## Draft Documents\n\n"
        "```dataview\n"
        "TABLE type, document-category, owner, last-reviewed\n"
        "FROM \"\"\n"
        "WHERE status = \"draft\"\n"
        "SORT title ASC\n"
        "```\n\n"
        "## Theology Documents\n\n"
        "```dataview\n"
        "TABLE status, version, owner\n"
        "FROM \"\"\n"
        "WHERE contains(tags, \"theology\") OR document-category = \"theology\"\n"
        "SORT title ASC\n"
        "```\n\n"
        "## Housing Documents\n\n"
        "```dataview\n"
        "TABLE status, version, owner\n"
        "FROM \"\"\n"
        "WHERE contains(tags, \"housing\") OR document-category = \"housing\"\n"
        "SORT title ASC\n"
        "```\n"
    )


def international_pages(project: Project) -> list[Page]:
    """Return documents that use international governance metadata.

    Parameters
    ----------
    project : Project
        Project to inspect.

    Returns
    -------
    list[Page]
        Pages with jurisdiction, chapter, governance-level, parent-document, or
        applies-to metadata.
    """
    keys = ("jurisdiction", "chapter", "governance-level", "parent-document", "applies-to")
    return [
        page for page in project.pages
        if any(not is_blank(page.metadata.get(key)) for key in keys)
    ]


def parent_document_text(project: Project, page: Page) -> str:
    """Return display text for a page's parent document.

    Parameters
    ----------
    project : Project
        Project used to resolve the parent reference.
    page : Page
        Page whose `parent-document` metadata should be displayed.

    Returns
    -------
    str
        Obsidian link when the parent resolves, otherwise the raw reference.
    """
    references = ensure_list(page.metadata.get("parent-document", []))
    labels: list[str] = []
    for reference in references:
        target = resolve_page_reference(project, reference)
        labels.append(obsidian_link(target) if target else f"`{reference}`")
    return ", ".join(labels) if labels else "None"


def count_by_field(pages: list[Page], field: str) -> dict[str, int]:
    """Count pages by a metadata field.

    Parameters
    ----------
    pages : list[Page]
        Pages to count.
    field : str
        Metadata field name.

    Returns
    -------
    dict[str, int]
        Sorted mapping of field value to page count.
    """
    counts: dict[str, int] = {}
    for page in pages:
        value = metadata_value(page, field, "Unspecified")
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items()))


def render_count_list(counts: dict[str, int]) -> str:
    """Render count data as Markdown bullets.

    Parameters
    ----------
    counts : dict[str, int]
        Mapping of label to count.

    Returns
    -------
    str
        Markdown bullet list.
    """
    if not counts:
        return "- None"
    return "\n".join(f"- {label}: {count}" for label, count in counts.items())


def render_grouped_links(project: Project, field: str) -> str:
    """Render pages grouped by a metadata field.

    Parameters
    ----------
    project : Project
        Project whose pages should be grouped.
    field : str
        Metadata field name.

    Returns
    -------
    str
        Markdown headings and links grouped by field value.
    """
    groups: dict[str, list[Page]] = {}
    for page in project.pages:
        groups.setdefault(metadata_value(page, field, "Unspecified"), []).append(page)
    lines: list[str] = []
    for group, pages in sorted(groups.items()):
        lines.append(f"### {group}")
        lines.extend(f"- {obsidian_link(page)}" for page in pages)
        lines.append("")
    return "\n".join(lines).strip() or "- None"


def decision_pages(project: Project) -> list[Page]:
    """Return pages that should appear in the decision register.

    Parameters
    ----------
    project : Project
        Project to inspect.

    Returns
    -------
    list[Page]
        Pages with `decision-id` or `type: decision`.
    """
    return [
        page for page in project.pages
        if not is_blank(page.metadata.get("decision-id"))
        or metadata_value(page, "type").lower() == "decision"
    ]


def render_dependency_lines(edges: list[tuple[Page, Page | str]]) -> list[str]:
    """Render dependency edges as Markdown bullets.

    Parameters
    ----------
    edges : list[tuple[Page, Page or str]]
        Dependency edges where the first item depends on the second.

    Returns
    -------
    list[str]
        Markdown bullet lines.
    """
    if not edges:
        return ["No dependencies declared."]
    lines = []
    for page, target in edges:
        target_text = obsidian_link(target) if isinstance(target, Page) else f"`{target}`"
        lines.append(f"- {obsidian_link(page)} depends on {target_text}")
    return lines


def mermaid_node(label: str) -> str:
    """Return a Mermaid-safe node expression.

    Parameters
    ----------
    label : str
        Human-readable node label.

    Returns
    -------
    str
        Mermaid node identifier with a display label.
    """
    node_id = re.sub(r"[^A-Za-z0-9_]", "_", label).strip("_") or "Document"
    return f'{node_id}["{label.replace(chr(34), chr(39))}"]'


def write_html_site(project: Project, html_dir: Path) -> None:
    """Write a small static HTML website.

    Parameters
    ----------
    project : Project
        Project to publish.
    html_dir : pathlib.Path
        Destination directory for generated HTML files.

    Returns
    -------
    None
        HTML files are written to disk.
    """
    links = "\n".join(
        f'<li><a href="{escape(page.output_path.with_suffix(".html").as_posix())}">{escape(page.title)}</a></li>'
        for page in project.pages
    )
    (html_dir / "index.html").write_text(
        html_page(project.title, f"<h1>{escape(project.title)}</h1><ul>{links}</ul>"),
        encoding="utf-8",
    )
    for page in project.pages:
        destination = html_dir / page.output_path.with_suffix(".html")
        destination.parent.mkdir(parents=True, exist_ok=True)
        body = "\n".join(f"<p>{escape(line)}</p>" for line in page.body.splitlines() if line.strip())
        destination.write_text(
            html_page(page.title, f"<h1>{escape(page.title)}</h1>{body}"),
            encoding="utf-8",
        )


def html_page(title: str, body: str) -> str:
    """Wrap body HTML in a complete document.

    Parameters
    ----------
    title : str
        HTML document title.
    body : str
        Body HTML.

    Returns
    -------
    str
        Complete HTML document text.
    """
    return (
        "<!doctype html>\n"
        "<html lang=\"en\">\n"
        "<head><meta charset=\"utf-8\"><title>"
        f"{escape(title)}</title></head>\n"
        f"<body>{body}</body>\n"
        "</html>\n"
    )


def build_frontmatter_lines(item: dict, frontmatter_config: dict[str, list[str]]) -> list[str]:
    """Build ordered YAML frontmatter lines for one document.

    Parameters
    ----------
    item : dict
        Page configuration from `source/site.yml`.
    frontmatter_config : dict[str, list[str]]
        Configured `required`, `recommended`, and `optional` field names.

    Returns
    -------
    list[str]
        YAML frontmatter lines in the universal governance document order.

    Raises
    ------
    ValueError
        If a required property is missing or blank.
    """
    lines: list[str] = []
    for key in frontmatter_config.get("required", []):
        value = item.get(key)
        if is_blank(value):
            raise ValueError(f"Missing required frontmatter property: {key}")
        lines.extend(format_yaml_property(key, value))

    optional_keys = frontmatter_config.get("recommended", []) + frontmatter_config.get("optional", [])
    for key in optional_keys:
        value = item.get(key)
        if not is_blank(value):
            lines.extend(format_yaml_property(key, value))

    return lines


def format_yaml_property(key: str, value: object) -> list[str]:
    """Format a frontmatter property as YAML.

    Parameters
    ----------
    key : str
        YAML property name.
    value : object
        Property value. Scalars, lists, and mappings are emitted as readable
        YAML suitable for Obsidian and Dataview.

    Returns
    -------
    list[str]
        One or more YAML lines.
    """
    if isinstance(value, list):
        return [f"{key}:"] + format_yaml_sequence(value, indent=2)
    if isinstance(value, dict):
        return [f"{key}:"] + format_yaml_mapping(value, indent=2)
    return [f"{key}: {format_yaml_scalar(value)}"]


def format_yaml_sequence(values: list, indent: int) -> list[str]:
    """Format a YAML block sequence.

    Parameters
    ----------
    values : list
        Values to emit as sequence items.
    indent : int
        Number of spaces before each sequence marker.

    Returns
    -------
    list[str]
        YAML sequence lines.
    """
    lines: list[str] = []
    prefix = " " * indent
    for item in values:
        if is_blank(item):
            continue
        if isinstance(item, dict):
            mapping_lines = format_yaml_mapping(item, indent=indent + 2)
            if mapping_lines:
                first_line = mapping_lines[0].lstrip()
                lines.append(f"{prefix}- {first_line}")
                lines.extend(mapping_lines[1:])
        elif isinstance(item, list):
            lines.append(f"{prefix}-")
            lines.extend(format_yaml_sequence(item, indent=indent + 2))
        else:
            lines.append(f"{prefix}- {format_yaml_scalar(item)}")
    return lines


def format_yaml_mapping(values: dict, indent: int) -> list[str]:
    """Format a YAML block mapping.

    Parameters
    ----------
    values : dict
        Mapping to emit as nested YAML.
    indent : int
        Number of spaces before each mapping key.

    Returns
    -------
    list[str]
        YAML mapping lines.
    """
    lines: list[str] = []
    prefix = " " * indent
    for key, value in values.items():
        if is_blank(value):
            continue
        if isinstance(value, list):
            lines.append(f"{prefix}{key}:")
            lines.extend(format_yaml_sequence(value, indent=indent + 2))
        elif isinstance(value, dict):
            lines.append(f"{prefix}{key}:")
            lines.extend(format_yaml_mapping(value, indent=indent + 2))
        else:
            lines.append(f"{prefix}{key}: {format_yaml_scalar(value)}")
    return lines


def format_yaml_scalar(value: object) -> str:
    """Format a scalar for YAML frontmatter.

    Parameters
    ----------
    value : object
        Scalar value to format.

    Returns
    -------
    str
        YAML scalar text.
    """
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int | float):
        return str(value)
    return yaml_quote(str(value))


def yaml_quote(value: str) -> str:
    """Quote a string for safe YAML frontmatter output.

    Parameters
    ----------
    value : str
        String to quote.

    Returns
    -------
    str
        Double-quoted YAML scalar.
    """
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def is_blank(value: object) -> bool:
    """Return whether a value should be omitted from frontmatter.

    Parameters
    ----------
    value : object
        Candidate YAML value.

    Returns
    -------
    bool
        True when the value is missing, empty, or an empty list.
    """
    return value is None or value == "" or value == []


def parse_site_yml(text: str) -> dict:
    """Parse the starter kit's simple YAML configuration.

    Parameters
    ----------
    text : str
        Raw text from `source/site.yml`.

    Returns
    -------
    dict
        Configuration dictionary with top-level project fields and `pages`.

    Notes
    -----
    This is a fallback for environments where PyYAML has not been installed.
    It supports the simple shape used by the starter kit, not full YAML.
    """
    config: dict = {"pages": []}
    current_page: dict | None = None
    in_pages = False

    for raw in text.splitlines():
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        stripped = raw.strip()
        if stripped == "pages:":
            in_pages = True
            continue
        if not in_pages:
            key, value = stripped.split(":", 1)
            config[key] = clean_scalar(value)
            continue
        if stripped.startswith("- "):
            current_page = {}
            config["pages"].append(current_page)
            field = stripped[2:]
            if field:
                key, value = field.split(":", 1)
                current_page[key] = clean_scalar(value)
            continue
        if current_page is not None and ":" in stripped:
            key, value = stripped.split(":", 1)
            current_page[key] = clean_scalar(value)

    return config


def clean_scalar(value: str) -> str | list[str]:
    """Convert a simple YAML scalar or inline list.

    Parameters
    ----------
    value : str
        Raw value text after the colon in a simple key-value line.

    Returns
    -------
    str or list[str]
        Unquoted string or inline list of strings.
    """
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        return [item.strip().strip('"') for item in value[1:-1].split(",") if item.strip()]
    return value
