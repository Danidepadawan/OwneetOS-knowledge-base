---
type: best-practice
scope: project
tags: [best-practice, style]
---
# Formatting (spacing, line length)

From `.editorconfig` and the existing code.

| Files | Indentation |
|---|---|
| everything (default) | 4 spaces |
| `*.md`, `*.yml`, `*.yaml`, `*.json`, `*.html`, `*.css`, `*.js` | 2 spaces |
| `PKGBUILD`, `*.install` | 2 spaces |
| `*.go`, `go.mod`, `Makefile` | tabs (gofmt) |

- UTF-8, LF line endings, a final newline, no trailing whitespace.
- **Lines wrap at 100 columns** in OwneetOS's own code, comments and Markdown prose (tables and URLs
  may be longer: markdownlint's line-length rule is off).
- Imported third-party code (Pegasus, vendored Go modules) keeps its own style.

Language specifics: [[go]], [[qml]], [[cpp-qt]], [[shell]], [[markdown]].
