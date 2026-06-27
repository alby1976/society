#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
python build.py
echo "Built dist/vault, dist/guide.pdf, and dist/guide.docx"
