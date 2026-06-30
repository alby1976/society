.PHONY: build audit links yaml release clean

build:
	python build.py

audit: yaml links

yaml:
	python scripts/validate_yaml.py

links:
	python scripts/check_links.py

release:
	python scripts/package_release.py

clean:
	python -c "import shutil, pathlib; p=pathlib.Path('dist'); shutil.rmtree(p) if p.exists() else None"
