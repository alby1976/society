from pathlib import Path
import sys

from ccts_generator.parser import discover_documents
from ccts_generator.validators import validate_documents

docs = discover_documents(Path("source"))
result = validate_documents(docs)

print(f"Documents: {len(docs)}")
print(f"Errors: {len(result.errors)}")
print(f"Warnings: {len(result.warnings)}")

if result.errors:
    print("\nErrors")
    for error in result.errors:
        print(f"- {error}")

if result.warnings:
    print("\nWarnings")
    for warning in result.warnings:
        print(f"- {warning}")

sys.exit(1 if result.errors else 0)
