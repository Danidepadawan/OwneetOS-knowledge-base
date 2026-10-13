---
type: meta
tags: [meta]
---
# Knowledge base rules

How this vault is organised and kept up to date. It is loaded in every AI session together with
the [[guards-index|guards]]. Paths in backticks (`daemon/`, `tools/lint`) are relative to the code
repository `OwneetOS/`; links in double brackets are notes of this vault.

## Precedence

1. The **owner's edits always win**, in any note.
2. [[guards-index|Guards]] (never break them) → [[decision-log|decisions]] → best practices →
   workflow documents. If two notes disagree, the higher one wins and the lower one gets fixed in
   the same change.
3. If something is not covered, or the vault and the code disagree: **ask the owner**, never assume.

## Categories (one folder each)

| Folder | What goes there | Test |
|---|---|---|
| `guards/` | Prohibitions: what must **never** be done. Read in every session, kept whole across compaction. | Can it be written as "Never …"? Would breaking it cause damage, a legal problem, or override the owner? |
| `best-practices/project/` | How this project does things: style, conventions, patterns, checks. | Is it a "how we do it" that applies again and again? |
| `best-practices/languages/` | Conventions for one language or toolkit (Go, QML, C++/Qt, shell, Markdown). | Does it only make sense in that language? |
| `decisions/<area>/` | Choices agreed with the owner between real alternatives, including those already taken. | Was there more than one way, and did the owner choose? Does it steer the project? |
| `workflow/functional-analysis/` | What the product does for the user (vision, features, specs of behaviour). | Is it "what", seen by the user? |
| `workflow/technical-analysis/` | How a component is built (design, API, internals). | Is it "how", seen by a developer? |
| `workflow/waves/` | The plan: waves → phases → steps, with status and outcome. | Is it "when / in which order / is it done"? |
| root, `templates/` | Everything else: this file, the vault home, the legacy map, templates. | — |

Decisions and best practices often justify each other: link both ways (a best practice says
which decision it comes from; a decision lists the practices and guards it creates).

## Writing notes

- **One topic per note.** A note that covers two topics, or grows past ~150 lines, is split.
  Guards stay short (they are loaded every time): one line per rule, no history.
- **File names:** `kebab-case.md`, unique in the whole vault (links use the bare name). Step notes:
  `step-<n.m>-<topic>.md`.
- **Front matter** on every note: `type` (guard, best-practice, decision, functional-analysis,
  technical-analysis, wave, phase, step, meta) and `tags`. Decisions add `area`, `status`
  (active, superseded, proposed), `decided`, `updated`; steps add `status` (done, in-progress,
  todo, needs-decision) and `phase`; `legacy` names the old section it came from.
- **Links:** `[[note]]` or `[[note|text]]` for every reference to another note; never "see the
  rules" without a link. Repository files stay as `code` paths.
- **English**, plain words, absolute dates (`2026-10-12`, never "yesterday").

## Keeping it up to date

- **A new decision with the owner:** in the same change, (1) update or create the decision note
  (summary at the top, a new row in its *History*), (2) add the row to [[decision-log]], (3) update
  every guard, best practice and step note it affects. A replaced decision is never deleted: its
  note gets `status: superseded` and a link to the one that replaces it.
- **A step changes status or gets an outcome:** update its step note and the status in its phase
  note.
- **A new guard** needs the owner's agreement: guards are prohibitions, not preferences.
- Old references in code comments (`PROJECT_RULES.md section 9.1`, `roadmap step 3.4`) are
  resolved with [[legacy-references]].
