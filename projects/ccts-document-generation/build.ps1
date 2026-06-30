$ErrorActionPreference = "Stop"

Write-Host "Building CCTS governance vault..."

if (!(Test-Path ".venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
}

Write-Host "Activating virtual environment..."
. .\.venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..."
pip install -r requirements.txt

Write-Host "Running build..."
python build.py

Write-Host "Running YAML validation..."
python scripts/validate_yaml.py

Write-Host "Running link check..."
python scripts/check_links.py

Write-Host "Done. Open dist\obsidian-vault in Obsidian."
