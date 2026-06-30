from pathlib import Path
from zipfile import ZipFile

release_name = "ccts-governance-vault-v0.1-draft"
dist = Path("dist")
output = Path(f"{release_name}.zip")

if not dist.exists():
    raise SystemExit("dist/ does not exist. Run python build.py first.")

with ZipFile(output, "w") as z:
    for path in dist.rglob("*"):
        if path.is_file():
            z.write(path, path.relative_to(dist.parent))

print(output)
