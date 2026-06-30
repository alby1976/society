from __future__ import annotations

import subprocess
import sys
from pathlib import Path


COMMANDS = [
    [sys.executable, "build.py"],
    [sys.executable, "scripts/validate_yaml.py"],
    [sys.executable, "scripts/check_links.py"],
]


def run(command: list[str]) -> int:
    print("\n==>", " ".join(command))
    completed = subprocess.run(command)
    return completed.returncode


def main() -> None:
    Path("dist/reports").mkdir(parents=True, exist_ok=True)

    failures = []
    for command in COMMANDS:
        code = run(command)
        if code != 0:
            failures.append((" ".join(command), code))

    summary = ["# Build All Summary", ""]
    if failures:
        summary.append("## Failures")
        summary.append("")
        for command, code in failures:
            summary.append(f"- `{command}` exited with code `{code}`")
    else:
        summary.append("All build steps completed successfully.")

    Path("dist/reports/build-all-summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
