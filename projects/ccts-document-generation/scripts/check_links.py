from pathlib import Path

from ccts_generator.parser import discover_documents
from ccts_generator.links import check_links, render_missing_links_report

docs = discover_documents(Path("source"))
report = check_links(docs)
text = render_missing_links_report(report)

Path("dist/reports").mkdir(parents=True, exist_ok=True)
Path("dist/reports/missing-links.md").write_text(text, encoding="utf-8")

print(text)
