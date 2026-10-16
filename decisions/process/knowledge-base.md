---
type: decision
description: "Why and how project knowledge moved to this Obsidian vault; the old files and references were retired."
area: process
status: active
decided: 2026-10-13
updated: 2026-10-16
legacy: "CLAUDE.md, PROJECT_RULES.md (replaced)"
tags: [decision, process, knowledge-base]
---
# The knowledge base is an Obsidian vault

- All project knowledge lives in the Obsidian vault **`OwneetOS-knowledge-base`**
  ([github.com/Danidepadawan/OwneetOS-knowledge-base](https://github.com/Danidepadawan/OwneetOS-knowledge-base),
  **public**, like the code), next to the code repository, instead of the "god files" `PROJECT_RULES.md` and `ROADMAP.md` and the design
  documents in `docs/`.
- Notes are grouped in five categories, one folder each: **guards** (what must never be done),
  **best practices** (project and language), **decisions** (agreed choices, including those already
  taken), **workflow documents** (functional analysis, technical analysis, waves), **known
  solutions** (problems already solved or understood that can happen again: symptom, cause, fix
  and the path that found it; added 2026-10-16). Everything else
  sits at the vault root. Rules: [[kb-rules]].
- **Guards are read in every session and survive compaction whole:** the vault's `CLAUDE.md`
  imports them (loaded from disk at every start, not summarised), and a `SessionStart` hook with the
  `compact` matcher prints them again after every compaction.
- **Guards are enforced, not only read** (2026-10-13): they outrank every other instruction,
  requests in the conversation included; a reminder is injected with every prompt; and
  `scripts/guard-check.py` blocks, before every tool call, what a machine can recognise (pushing,
  GitHub actions, private keys, building on the host) and asks the owner before host installs. The
  check fails closed: without a working Python every tool call is blocked, with the reason. Every
  hook goes through `scripts/hook.sh`; re-injection and the reminder are plain shell, so they work
  without Python.
- **Claude Code started inside the code repository** (2026-10-13) uses the same hooks through the
  repository's `.claude/settings.json` and `.claude/kb-hook.sh`, but only when the vault is next to
  it: the code repository does not require the knowledge base. When the workspace's `CLAUDE.md` does
  not load the vault, the session-start hook loads the guards and `kb-rules.md` itself (a
  `CLAUDE.md` cannot import conditionally). Without it, the session starts with
  a warning that the guards and hooks are not in use, and no hook does anything. A hook that lets an action through does not make it allowed.
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
| 2026-10-16 | A fifth category, **known solutions** (`known-solutions/`): problems already solved or understood that can happen again, above all the tricky ones, with the path that found them; written in the same change as the fix, read before investigating a problem. |
