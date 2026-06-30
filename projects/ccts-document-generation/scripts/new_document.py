from __future__ import annotations

import argparse
from datetime import date, timedelta
from pathlib import Path
import re


def slug_title(title: str) -> str:
    return re.sub(r"\s+", " ", title).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new CCTS Markdown document with standard YAML")
    parser.add_argument("title", help="Document title")
    parser.add_argument("--document-id", required=True, help="Stable document ID")
    parser.add_argument("--folder", default="source/99 Drafts", help="Destination folder")
    parser.add_argument("--type", default="Policy", help="Document type")
    parser.add_argument("--category", default="Governance", help="Document category")
    parser.add_argument("--jurisdiction", default="International")
    parser.add_argument("--chapter", default="Global")
    parser.add_argument("--governance-level", default="Administrative")
    args = parser.parse_args()

    title = slug_title(args.title)
    today = date.today()
    next_year = today + timedelta(days=365)

    content = f'''---
document-id: {args.document_id}
title: {title}
version: 0.1.0
status: Draft
type: {args.type}
document-category: {args.category}
jurisdiction: {args.jurisdiction}
chapter: {args.chapter}
governance-level: {args.governance_level}
effective-date:
last-reviewed: {today.isoformat()}
next-review-date: {next_year.isoformat()}
review-cycle: Annual
approved-by:
authority-level: Administrative
scriptural-foundation:
confessional-foundation:
related-documents:
supersedes:
dependencies:
tags:
  - draft
---

# {title}

## 1. Purpose

## 2. Governing Principle

## 3. Scope

## 4. Content

## 5. Review
'''

    path = Path(args.folder) / f"{title}.md"
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        raise SystemExit(f"File already exists: {path}")

    path.write_text(content, encoding="utf-8")
    print(path)


if __name__ == "__main__":
    main()
