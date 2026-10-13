---
type: decision
description: "Why and how project knowledge moved to this Obsidian vault; the old files and references were retired."
area: process
status: active
decided: 2026-10-13
updated: 2026-10-13
legacy: "CLAUDE.md, PROJECT_RULES.md (replaced)"
tags: [decision, process, knowledge-base]
---
# The knowledge base is an Obsidian vault

- All project knowledge lives in the Obsidian vault **`OwneetOS-knowledge-base`**, next to the code
  repository, instead of the "god files" `PROJECT_RULES.md` and `ROADMAP.md` and the design
  documents in `docs/`.
- Notes are grouped in four categories, one folder each: **guards** (what must never be done),
  **best practices** (project and language), **decisions** (agreed choices, including those already
  taken), **workflow documents** (functional analysis, technical analysis, waves). Everything else
  sits at the vault root. Rules: [[kb-rules]].
- **Guards are read in every session and survive compaction whole:** the vault's `CLAUDE.md`
  imports them (loaded from disk at every start, not summarised), and a `SessionStart` hook with the
  `compact` matcher prints them again after every compaction.
- The old files' history is kept: decision-log entries verbatim in [[decision-log]] and in each
  decision note's *History*; roadmap steps verbatim in the step notes; old section references
  resolved by [[legacy-references]].
- What ships with the code or serves outside contributors stays in the code repository
  ([[documentation]]).
- The migrated files (`PROJECT_RULES.md`, `ROADMAP.md`, `docs/daemon-design.md`,
  `docs/frontend-architecture.md`, `design/sounds.md`) were **deleted from the code repository** on
  2026-10-13; every reference to them in the repository (code comments, scripts, CI, documents) now links
  the vault note as `[[note-name]]`. They remain in git history.

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-13 | The knowledge base moves to the Obsidian vault `OwneetOS-knowledge-base`: guards, best practices, decisions and workflow documents in their own folders; guards loaded in every session and re-injected after compaction; `PROJECT_RULES.md`, `ROADMAP.md` and the design documents migrated with their history. |
