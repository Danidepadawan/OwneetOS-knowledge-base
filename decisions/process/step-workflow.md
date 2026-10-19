---
type: decision
description: "In steps with the owner"
area: process
status: active
decided: 2026-10-03
updated: 2026-10-19
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
  [[how-we-work]]. **Exception** (owner, 2026-10-19): an author (the owner or Danidepadawan) may
  expressly ask to move on before the current step is approved; that step stays in progress, is
  tested together with the next one, and is approved afterwards (the owner wrote it in the guard
  [[collaboration]]).
- **Small hardware checks are batched** with the next larger test instead of a new USB stick each.
- **Testers' boot entries** ("diagnostics", "test games", "Install OwneetOS (testers)") and the
  OWNEETLOG test log leave the user ISO before the release (roadmap 7.4). Test PCs are installed and
  updated from the stick ([[test-pcs]]).

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
| 2026-10-13 | **Test PCs are installed**, not run from a stick: a tester installer (step 4.2a, boot entry "Install OwneetOS (testers)") and updates from a USB stick (step 4.2b: the `owneet-updates` folder on the OWNEETLOG stick, applied automatically at boot and from Settings → System), before step 4.3. Nothing is published online. Only systems installed by the tester installer accept unsigned OwneetOS packages, and only from that stick (option b). Test PC: "FrankenPC" (i7-6700, 16 GB, 96 GB SSD + 2 TB HDD, GTX 1660 Super); the NiPoGi stays a live-stick test PC. |
| 2026-10-19 | An author (the owner or Danidepadawan) may expressly ask to move on before the current step is approved: that step stays in progress, is tested together with the next one, and is approved afterwards (the owner changed the guard [[collaboration]]). First use: step 4.7 started while 4.6 waits for its test. |
