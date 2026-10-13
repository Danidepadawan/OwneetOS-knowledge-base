---
type: best-practice
scope: language
language: markdown
tags: [best-practice, markdown, docs]
---
# Markdown

- markdownlint (`markdownlint-cli2` 0.23.3) with the repository's `.markdownlint-cli2.yaml`:
  default rules, **line length not enforced** (tables and URLs), repeated headings allowed in
  different sections, table column alignment free.
- Prose wraps at 100 columns; 2-space indentation for nested lists ([[formatting]]).
- Tables for structured facts (decisions, API endpoints, measurements).
- Code, paths and commands in backticks; command blocks fenced as ```` ```text ````.
- In this vault: wikilinks for notes, front matter on every note ([[kb-rules]]).
