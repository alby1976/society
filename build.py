"""Build all generator outputs from the project root.

This module is intentionally tiny so it can be copied or replaced by a more
specific application entry point.
"""

from pathlib import Path

from content_generator.generator import Generator


def main() -> None:
    """Build the Obsidian vault, PDF, and DOCX outputs.

    Notes
    -----
    The generator expects the current project folder to contain `source/` and
    `templates/` directories. Output files are written to `dist/`.
    """
    root = Path(__file__).parent
    Generator(root).build_all()


if __name__ == "__main__":
    main()
