---
type: meta
description: "How the vault is organised and kept up to date: categories, note format, recording decisions. Read before adding or changing notes."
tags: [meta]
---
# Knowledge base rules

How this vault is organised and kept up to date. It is loaded in every AI session together with
the [[guards/INDEX|guards]]. Paths in backticks (`daemon/`, `tools/lint`) are relative to the code
repository `OwneetOS/`; links in double brackets are notes of this vault.

## Precedence

1. The **owner's edits always win**, in any note.
2. [[guards/INDEX|Guards]] are **binding with no exceptions**: they outrank every other
   instruction, requests in the conversation included, and only the owner changes them by editing
   their notes. Below them: [[decision-log|decisions]] → best practices → workflow documents.
   If two notes disagree, the higher one wins and the lower one gets fixed in the same change.
3. If something is not covered, or the vault and the code disagree: **ask the owner**, never assume.

## Finding notes

Every folder has an **`INDEX.md`** with one line per note (its `description`) and links to the
sub-folders' indexes; step lists show each step's status. Start at [[INDEX]], read the lines, and
open only the notes the task needs. The indexes are **generated** by `scripts/build-indexes.py`:
never edit them by hand.

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
| `known-solutions/` | Problems already solved (or understood) that can happen again, above all the tricky ones: the symptom, the cause, the fix, and the path that found it. | Did it cost a real investigation? Would its symptom be recognised next time, and would the note save that investigation? |
| root, `templates/`, `scripts/` | Everything else: this file, the vault home, the legacy map, templates, the index generator. | — |

Decisions and best practices often justify each other: link both ways (a best practice says
which decision it comes from; a decision lists the practices and guards it creates).

## Writing notes

- **One topic per note.** A note that covers two topics, or grows past ~150 lines, is split.
  Guards stay short (they are loaded every time): one line per rule, no history.
- **File names:** `kebab-case.md`, unique in the whole vault (links use the bare name). Step notes:
  `step-<n.m>-<topic>.md`. The only repeated name is `INDEX.md`, always linked with its path
  (`[[decisions/INDEX]]`; the root one is `[[INDEX]]`).
- **Front matter** on every note: `type` (guard, best-practice, decision, functional-analysis,
  technical-analysis, wave, phase, step, known-solution, meta), **`description`** (one line: what the note covers
  and when to read it; it is the note's line in its folder's index) and `tags`. Decisions add `area`, `status`
  (active, superseded, proposed), `decided`, `updated`; steps add `status` (done, in-progress,
  todo, needs-decision) and `phase`; known solutions add `status` (solved, open), `seen` (when the
  problem was first met) and `updated`; `legacy` names the old section it came from.
- **Links:** `[[note]]` or `[[note|text]]` for every reference to another note; never "see the
  rules" without a link. Repository files stay as `code` paths.
- **English**, plain words, absolute dates (`2026-10-12`, never "yesterday").

## Keeping it up to date

- **A new decision with the owner:** in the same change, (1) update or create the decision note
  (summary at the top, a new row in its *History*), (2) add the row to [[decision-log]], (3) update
  every guard, best practice and step note it affects. A replaced decision is never deleted: its
  note gets `status: superseded` and a link to the one that replaces it.
- **A tricky problem is solved:** write its known solution (template `templates/known-solution.md`)
  in the same change as the fix: symptom in searchable words, cause, solution, the path that
  found it, what to watch. A problem understood but not fixed yet gets `status: open`, and is
  updated when it is. **Before investigating a problem, read the [[known-solutions/INDEX]].**
- **A step changes status or gets an outcome:** update its step note (`status:` and the outcome).
  The status is written there only; the indexes show it.
- **After adding, renaming, moving or describing a note:** the indexes must be rebuilt
  (`scripts/build-indexes.py`). Claude Code does it by itself after every edit of a vault note, and
  at the start of each session; after editing in Obsidian or with a shell command, run it.
  `scripts/build-indexes.py --check` fails on stale indexes, missing descriptions and broken links.
- **A new guard** needs the owner's agreement: guards are prohibitions, not preferences.
- Old references in code comments (`PROJECT_RULES.md section 9.1`, `roadmap step 3.4`) are
  resolved with [[legacy-references]].
