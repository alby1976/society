@echo off
setlocal

echo Building CCTS governance vault...

if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
)

call .venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo Running build...
python build.py
if errorlevel 1 exit /b 1

echo Running YAML validation...
python scripts\validate_yaml.py
if errorlevel 1 exit /b 1

echo Running link check...
python scripts\check_links.py
if errorlevel 1 exit /b 1

echo Done. Open dist\obsidian-vault in Obsidian.
endlocal
