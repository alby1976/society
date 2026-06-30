$ErrorActionPreference = "Stop"

Write-Host "Setting up CCTS governance vault repository..."

python -m venv .venv
. .\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip

if (Test-Path "requirements.txt") {
    pip install -r requirements.txt
}

if (Test-Path "requirements-dev.txt") {
    pip install -r requirements-dev.txt
}

python scripts\bootstrap_repo.py

Write-Host "Setup complete."
