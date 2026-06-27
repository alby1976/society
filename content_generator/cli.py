"""Command-line entry point for the content generator.

Functions
---------
main
    Parse CLI arguments and run the requested build target.
"""

import argparse
from pathlib import Path

from .generator import Generator


def main() -> None:
    """Run the content generator from the command line.

    Returns
    -------
    None
        This function is executed for its side effects.

    Notes
    -----
    The CLI delegates all build behavior to :class:`content_generator.Generator`.

    Examples
    --------
    Build everything from the current directory::

        contentgen --root . --target all

    Build only the Obsidian vault::

        contentgen --root C:/path/to/project --target vault
    """
    parser = argparse.ArgumentParser(description="Build an Obsidian vault plus PDF/DOCX exports.")
    parser.add_argument("--root", default=".", help="Project root containing source/ and templates/.")
    parser.add_argument(
        "--target",
        choices=["all", "vault", "pdf", "docx", "html"],
        default="all",
        help="Output target to build.",
    )
    args = parser.parse_args()

    generator = Generator(Path(args.root).resolve())
    if args.target == "all":
        generator.build_all()
    elif args.target == "vault":
        generator.build_vault()
    elif args.target == "pdf":
        generator.build_pdf()
    elif args.target == "docx":
        generator.build_docx()
    elif args.target == "html":
        generator.build_html()
