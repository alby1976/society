"""Sample import showing how to point the generator at a project.

Run from the repository root:

    python examples/import_and_build.py

The important part is `project_root`: it must be the folder that contains
`source/site.yml`, `source/pages/`, and `templates/`.
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from content_generator import Generator  # noqa: E402


def main() -> None:
    """Build all documentation outputs from a selected project root.

    Examples
    --------
    For this starter project, use the parent folder of this file::

        project_root = Path(__file__).resolve().parents[1]
        Generator(project_root).build_all()

    For a different project, point at that project's root::

        project_root = Path("C:/docs/my-generator-project")
        Generator(project_root).build_all()
    """
    Generator(PROJECT_ROOT).build_all()


if __name__ == "__main__":
    main()
