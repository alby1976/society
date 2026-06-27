# Jinja2 for Dummies

## What Jinja2 Is

Jinja2 is a template engine for Python.

That means you write a text file with placeholders, then Python fills those placeholders with real data.

You can use Jinja2 to generate:

- Markdown files
- HTML pages
- Configuration files
- Emails
- Reports
- Obsidian notes
- Documentation pages

In your generator project, Jinja2 is used to turn auto-discovered Markdown
source files and their YAML frontmatter into Obsidian-ready Markdown files in
`dist/vault/`.

## The Basic Idea

A Jinja2 template looks like normal text with special markers inside it.

Example template:

```jinja2
# {{ title }}

Prepared by {{ author }}
```

Example data:

```python
{
    "title": "Governance Document Standard",
    "author": "Codex"
}
```

Generated output:

```markdown
# Governance Document Standard

Prepared by Codex
```

The `{{ ... }}` syntax means: print this value here.

## Installing Jinja2

Install it with pip:

```powershell
pip install jinja2
```

Or, if you are using a project with `pyproject.toml`, include:

```toml
dependencies = [
  "jinja2>=3.1"
]
```

## A Tiny Working Example

Create this Python file:

```python
from jinja2 import Template

template = Template("Hello, {{ name }}!")
output = template.render(name="Alice")

print(output)
```

Output:

```text
Hello, Alice!
```

That is the heart of Jinja2: template plus data becomes generated text.

## Loading Templates from Files

For real projects, templates usually live in files.

Example folder:

```text
project/
  templates/
    page.md.j2
  build.py
```

Example `templates/page.md.j2`:

```jinja2
# {{ page.title }}

{{ page.body }}
```

Example Python:

```python
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

root = Path(__file__).parent

env = Environment(
    loader=FileSystemLoader(root / "templates"),
    trim_blocks=True,
    lstrip_blocks=True,
)

template = env.get_template("page.md.j2")

output = template.render(
    page={
        "title": "My First Page",
        "body": "This page was generated with Jinja2.",
    }
)

print(output)
```

Generated Markdown:

```markdown
# My First Page

This page was generated with Jinja2.
```

## The Three Most Important Syntax Forms

Jinja2 has three core syntax forms.

### Print a Value

Use double curly braces:

```jinja2
{{ page.title }}
```

This prints the value of `page.title`.

### Run Logic

Use curly braces with percent signs:

```jinja2
{% if page.author %}
Prepared by {{ page.author }}
{% endif %}
```

This controls whether text appears.

### Write Comments

Use curly braces with hash signs:

```jinja2
{# This comment does not appear in the output. #}
```

This is useful for explaining a template without adding text to the generated file.

## Variables

Variables are values passed from Python into the template.

Python:

```python
template.render(title="Annual Policy Review")
```

Template:

```jinja2
# {{ title }}
```

Output:

```markdown
# Annual Policy Review
```

## Dictionaries and Objects

Jinja2 can read dictionary values with dot syntax.

Python:

```python
page = {
    "title": "Board Governance Policy",
    "version": "1.0.0",
}
```

Template:

```jinja2
# {{ page.title }}

Version: {{ page.version }}
```

Output:

```markdown
# Board Governance Policy

Version: 1.0.0
```

## If Statements

Use `if` when a section should only appear sometimes.

Template:

```jinja2
{% if page.author %}
author: "{{ page.author }}"
{% endif %}
```

If `page.author` exists, it appears.

If it is blank or missing, the section is skipped.

This is perfect for optional YAML frontmatter fields.

## For Loops

Use `for` when you need to repeat something.

Python data:

```python
tags = ["governance", "policy", "obsidian"]
```

Template:

```jinja2
tags:
{% for tag in tags %}
  - "{{ tag }}"
{% endfor %}
```

Output:

```yaml
tags:
  - "governance"
  - "policy"
  - "obsidian"
```

## Generating YAML Frontmatter

Jinja2 is very useful for generating Markdown files with YAML frontmatter.

Template:

```jinja2
---
document-id: "{{ page.document_id }}"
title: "{{ page.title }}"
version: "{{ page.version }}"
status: "{{ page.status }}"
type: "{{ page.type }}"
document-category: "{{ page.document_category }}"
effective-date: "{{ page.effective_date }}"
last-reviewed: "{{ page.last_reviewed }}"
tags:
{% for tag in page.tags %}
  - "{{ tag }}"
{% endfor %}
---

# {{ page.title }}

{{ page.body }}
```

Generated output:

```markdown
---
document-id: "DOC-GOV-0001"
title: "Board Governance Policy"
version: "1.0.0"
status: "approved"
type: "policy"
document-category: "governance"
effective-date: "2026-06-25"
last-reviewed: "2026-06-25"
tags:
  - "board"
  - "governance"
---

# Board Governance Policy

This policy defines board authority and accountability.
```

## Why Your Generator Uses Prebuilt Frontmatter Lines

In the generator project, frontmatter is built in Python first, then passed to Jinja2 as `page.frontmatter_lines`.

That template looks like this:

```jinja2
---
{% for line in page.frontmatter_lines -%}
{{ line }}
{% endfor -%}
---

# {{ page.title }}

{{ page.body }}
```

This is a good design because Python can enforce rules before Jinja2 writes the file:

- Required fields must exist.
- Fields stay in the exact required order.
- Optional fields are omitted when blank.
- YAML values are quoted safely.

Jinja2 then focuses on presentation instead of validation.

## Whitespace Control

Jinja2 can leave extra blank lines if you are not careful.

This:

```jinja2
{% for item in items %}
- {{ item }}
{% endfor %}
```

May produce extra spacing depending on your template settings.

This:

```jinja2
{% for item in items -%}
- {{ item }}
{% endfor %}
```

Uses `-%}` to trim whitespace.

In Python, these settings also help:

```python
Environment(
    loader=FileSystemLoader("templates"),
    trim_blocks=True,
    lstrip_blocks=True,
)
```

For beginners, remember this rule:

Use normal `{% ... %}` first. Add `-` only when the output has too many blank lines.

## Filters

Filters change a value before printing it.

Template:

```jinja2
{{ title | upper }}
```

Output:

```text
BOARD GOVERNANCE POLICY
```

Common filters:

```jinja2
{{ name | lower }}
{{ name | upper }}
{{ title | title }}
{{ items | length }}
{{ value | default("Not provided") }}
```

## Includes

Includes let one template reuse another template.

Example:

```text
templates/
  page.md.j2
  sections/
    references.md.j2
```

In `page.md.j2`:

```jinja2
{% include "sections/references.md.j2" %}
```

This is useful when many generated documents share the same section.

## Template Inheritance

Template inheritance is more common in websites, but it can also help with documents.

Base template:

```jinja2
# {{ page.title }}

{% block content %}{% endblock %}
```

Child template:

```jinja2
{% extends "base.md.j2" %}

{% block content %}
## Executive Summary

{{ page.summary }}
{% endblock %}
```

For simple Markdown generation, includes are usually easier than inheritance.

## Autoescaping

Autoescaping protects HTML output from unsafe text.

For Markdown generation, you usually do not want HTML autoescaping.

Good Markdown setup:

```python
Environment(
    loader=FileSystemLoader("templates"),
    autoescape=False,
)
```

Your generator uses:

```python
select_autoescape(default_for_string=False)
```

That keeps Markdown output readable.

## Common Beginner Mistakes

### Mistake 1: Forgetting to Pass a Variable

Template:

```jinja2
{{ page.title }}
```

Python:

```python
template.render(document=page)
```

This will not work because the template expects `page`, but Python passed `document`.

Fix:

```python
template.render(page=page)
```

### Mistake 2: Broken YAML from Unquoted Values

This can be risky:

```jinja2
related-documents:
  - {{ document }}
```

If `document` is `[[Board Policy]]`, YAML may interpret the brackets incorrectly.

Safer:

```jinja2
related-documents:
  - "{{ document }}"
```

### Mistake 3: Too Much Logic in Templates

Templates should mostly describe output shape.

Python should handle:

- Validation
- Sorting
- Required field checks
- Date formatting
- YAML quoting rules

Jinja2 should handle:

- Where values appear
- Repeated sections
- Conditional sections

## How This Fits Your Generator

Your generator has this basic flow:

```text
source/site.yml
        |
        v
Python loads project metadata
        |
        v
Python discovers Markdown files recursively under source/
        |
        v
Python validates and prepares frontmatter
        |
        v
Jinja2 renders Markdown files
        |
        v
dist/vault/
```

The key files are:

```text
content_generator/generator.py
generator.yml
templates/page.md.j2
templates/index.md.j2
source/site.yml
source/
dist/vault/
```

`generator.yml` controls build behavior such as paths, output names, generated
note names, and frontmatter field groups. `source/site.yml` controls project
metadata and optional page ordering or overrides. The Markdown files under
`source/` carry the normal document body and YAML frontmatter.

## A Practical Mini Project

Create a template named `policy.md.j2`:

```jinja2
---
document-id: "{{ document_id }}"
title: "{{ title }}"
version: "{{ version }}"
status: "{{ status }}"
type: "policy"
document-category: "{{ category }}"
effective-date: "{{ effective_date }}"
last-reviewed: "{{ last_reviewed }}"
tags:
{% for tag in tags %}
  - "{{ tag }}"
{% endfor %}
---

# {{ title }}

## Executive Summary

{{ executive_summary }}

## Purpose

{{ purpose }}

## Scope

{{ scope }}

## References

{% for reference in references %}
- [[{{ reference }}]]
{% endfor %}
```

Render it with Python:

```python
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("policy.md.j2")

output = template.render(
    document_id="DOC-RISK-0001",
    title="Volunteer Screening Policy",
    version="1.0.0",
    status="approved",
    category="risk-management",
    effective_date="2026-06-25",
    last_reviewed="2026-06-25",
    tags=["volunteers", "risk-management"],
    executive_summary="This policy defines screening expectations for volunteers.",
    purpose="To protect participants, volunteers, and the organization.",
    scope="This policy applies to all volunteer roles.",
    references=["Child Safety Policy", "Code of Conduct"],
)

with open("Volunteer Screening Policy.md", "w", encoding="utf-8") as file:
    file.write(output)
```

## When to Use Jinja2

Use Jinja2 when:

- Many documents share the same structure.
- You want consistent frontmatter.
- You need repeatable Markdown generation.
- You want to separate content from layout.
- You want to generate many files from one configuration.

Do not overuse Jinja2 when:

- You only need one static document.
- The template logic becomes harder to read than Python.
- You need complex parsing that belongs in real Python code.

## Beginner Cheat Sheet

```jinja2
{{ value }}
```

Print a value.

```jinja2
{% if value %}
Show this.
{% endif %}
```

Show something conditionally.

```jinja2
{% for item in items %}
- {{ item }}
{% endfor %}
```

Repeat something.

```jinja2
{# comment #}
```

Write a template comment.

```jinja2
{{ value | upper }}
```

Apply a filter.

## Final Mental Model

Think of Jinja2 as a mail merge for code and documents.

Python provides the data.

Jinja2 provides the shape.

The generated file is the result.

For your project, that means:

- Markdown files under `source/` define the documents.
- YAML frontmatter on each Markdown file defines document metadata.
- `source/site.yml` defines project metadata and optional page order or overrides.
- `generator.yml` defines build paths, generated note names, and frontmatter field groups.
- `templates/` controls the generated page and index Markdown shape.
- `content_generator/` loads, validates, and renders everything.
- `dist/vault/` receives the generated Obsidian-ready files and generated governance notes.
- Optional `dist/site/` receives the static HTML website when enabled.
