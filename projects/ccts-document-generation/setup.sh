#!/usr/bin/env bash
set -euo pipefail

echo "Setting up CCTS governance vault repository..."

python -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip

if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi

if [ -f requirements-dev.txt ]; then
  pip install -r requirements-dev.txt
fi

python scripts/bootstrap_repo.py

echo "Setup complete."
