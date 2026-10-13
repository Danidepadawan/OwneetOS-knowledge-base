---
type: decision
area: process
status: active
decided: 2026-10-03
updated: 2026-10-11
legacy: "PROJECT_RULES.md §10 (Roadmap), header; ROADMAP.md How we work"
tags: [decision, process]
---
# Working in steps with the owner

- The knowledge base is the **source of truth** for every requirement and decision agreed so far.
  Anyone working on the project (humans and AI assistants) reads it before starting and must not
  contradict it. If something is not covered, **ask** — do not assume. The owner may edit any
  note at any time; the owner's edits always win.
- The plan lives in [[wave-1]] (and later waves). Work proceeds **one step per prompt, in order**;
  the owner reviews each step before the next one starts. The full procedure is in
  [[how-we-work]].
- **Small hardware checks are batched** with the next larger test instead of a new USB stick each.
- **Testers' boot entries** ("diagnostics", "test games") and the OWNEETLOG test log leave the user
  ISO before the release (roadmap 7.4).

Guard: [[collaboration]]. Practices: [[testing-and-verification]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-03 | Next step: UI mockups for owner approval, then repo structure and builder VM. |
| 2026-10-03 | [[wave-1]] created; work proceeds one step per prompt. |
| 2026-10-08 | Step 3.3 approved. Button prompts also have a Nintendo-style set (chosen automatically for Switch controllers). Small hardware checks are batched with the next larger test instead of a new USB stick each. |
| 2026-10-09 | Steps 3.7 (library) and 3.8 (frontend ↔ owneetd: games through owneetd, Guide / Resume) approved after the owner's test on the NiPoGi. Testers' boot entries ("diagnostics", "test games") leave the user ISO before the release (roadmap 7.4). |
| 2026-10-11 | Step 3.10 (on-screen keyboard) approved. The next USB-stick test on real hardware comes at the end of step 3.12, with everything since step 3.9 (on-screen keyboard, notifications, interface sounds). |
| 2026-10-13 | The knowledge base moves to the Obsidian vault `OwneetOS-knowledge-base`: guards, best practices, decisions and workflow documents in their own folders; guards loaded in every session and re-injected after compaction; `PROJECT_RULES.md`, `ROADMAP.md` and the design documents migrated with their history. |
