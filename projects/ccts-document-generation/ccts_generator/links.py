from dataclasses import dataclass

from .models import Document


@dataclass
class LinkReport:
    missing_links: dict[str, list[str]]
    inbound_links: dict[str, list[str]]


def check_links(docs: list[Document]) -> LinkReport:
    titles = {doc.title for doc in docs}
    missing: dict[str, list[str]] = {}
    inbound: dict[str, list[str]] = {doc.title: [] for doc in docs}

    for doc in docs:
        for link in doc.links:
            if link in titles:
                inbound.setdefault(link, []).append(doc.title)
            else:
                missing.setdefault(link, []).append(doc.title)

    return LinkReport(missing_links=missing, inbound_links=inbound)


def render_missing_links_report(report: LinkReport) -> str:
    lines = [
        "# Missing Links Report",
        "",
        "| Missing Link | Linked From |",
        "|---|---|",
    ]

    if not report.missing_links:
        lines.append("| None | None |")
    else:
        for missing, sources in sorted(report.missing_links.items()):
            lines.append(f"| [[{missing}]] | {', '.join(f'[[{s}]]' for s in sorted(sources))} |")

    return "\n".join(lines) + "\n"
