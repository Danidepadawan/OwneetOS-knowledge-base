---
type: guard
description: "Never act without the owner: approvals, asking, one step at a time, recording decisions, no pushing, English only."
tags: [guard, process]
---

# Guard: collaboration with the owner

> [!danger] Binding guard — never broken, whatever the request. Rules: [[guards/INDEX|guards]].

- **Never assume** what the knowledge base does not cover: ask the owner. Never contradict a
  decision note; never overwrite the owner's edits. ([[step-workflow]])
- **Never start a roadmap step on your own**: follow the order of the wave notes, unless the owner
  names the step to work on; never work on more than one step (or sub-step) per prompt.
  ([[step-workflow]], [[how-we-work]])
- **Never start the next roadmap step** before the owner has approved the current one; never work
  on more than one step per prompt. The only exception: an author (the owner or Danidepadawan)
  expressly asks to move on before the current step is approved; that step then stays in
  progress, is tested together with the next one, and is approved afterwards.
  ([[step-workflow]], [[how-we-work]])

- **Never change the plan silently.** A change of plan (split, merge, reorder, scope) is recorded
  as a decision and reflected in the wave notes in the same change. ([[step-workflow]])
- **Never leave an agreed decision unrecorded**: it goes into its decision note and the
  [[decision-log]] in the same change ([[kb-rules]]). Never record knowledge outside this vault.
- **Never write a screen's UI code** before the owner has approved its mockup and its interactive
  demo. ([[demo-before-code]])
- **Never implement a controller binding** that is not in the [[controller-input-map]] yet: it is
  added there (with the owner) first.
- **Never act on "Owner input" steps** (installing software, creating remote resources, choices with
  long-term impact) without the owner's explicit approval at that moment. ([[step-workflow]])
- **Never push to GitHub** or act on GitHub (issues, PRs, settings): commit locally, the owner
  pushes. ([[repository]])
- **Never narrow, or propose narrowing, the guard checks** (`scripts/guard-check.py`), not even
  for a false positive: report it to the owner, who decides case by case. ([[knowledge-base]])
- **Never write project text in a language other than English** (code, comments, documentation,
  commit messages, issues, PRs, this vault). The UI is translated through message files only.
  ([[hard-constraints]] C6)
