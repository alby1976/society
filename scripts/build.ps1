$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot
Push-Location $ProjectRoot
try {
    python .\build.py
    Write-Host "Built dist/vault, dist/guide.pdf, and dist/guide.docx"
}
finally {
    Pop-Location
}
