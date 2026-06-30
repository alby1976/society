from __future__ import annotations

import subprocess
import sys


def main() -> None:
    commands = [
        [sys.executable, "-m", "pytest"],
        [sys.executable, "scripts/validate_yaml.py"],
        [sys.executable, "scripts/check_links.py"],
    ]

    failures = []
    for command in commands:
        print("\n==>", " ".join(command))
        result = subprocess.run(command)
        if result.returncode != 0:
            failures.append(command)

    if failures:
        print("\nFailures:")
        for failure in failures:
            print("-", " ".join(failure))
        raise SystemExit(1)

    print("\nAll QA checks completed.")


if __name__ == "__main__":
    main()
