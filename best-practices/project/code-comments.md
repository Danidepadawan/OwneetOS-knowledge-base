---
type: best-practice
description: "How comments are written: header blocks, why not what, comment size, citing vault notes as wikilinks, no TODOs."
scope: project
tags: [best-practice, style]
---
# Code comments

How comments are written in OwneetOS's own code (observed across Go, QML, C++ and shell).

- **English, full sentences, plain words**, wrapped at 100 columns ([[formatting]]).
- **File header:** after the SPDX line ([[license-headers]]), a short block saying what the file is
  for and where it fits, with the roadmap step or decision it implements, e.g.
  `// Input map and navigation, shared by every screen ([[controller-input-map]]):`.
- **Citing the knowledge base:** a vault note is written as an Obsidian link, `[[note-name]]`,
  in code comments and in the repository's documents (steps as `[[step-3.9-settings]]`). Never
  cite the retired files (`PROJECT_RULES.md`, `ROADMAP.md`, `docs/*-design.md`); see
  [[legacy-references]].
- **Scripts** list in their header how they are run, their options and test hooks
  (`owneet.debug.*` kernel options), aligned in two columns.
- **Explain why, not what**: the reason for a non-obvious choice, the hardware or bug that caused
  it ("direct scanout showed flickering rectangles with the NVIDIA driver").
- **Size:** one line for a simple reason; a short paragraph (2–6 lines) for a design choice; longer
  explanations belong in a technical analysis note, linked from the comment.
- **Go:** every exported identifier and package has a doc comment that starts with its name
  ([[go]]).
- **C++ headers:** `///` doc comments on public methods ([[cpp-qt]]).
- **No `TODO` / `FIXME` comments** (the project's own code has none): open work is tracked in the
  step notes of [[wave-1]] ("Open:", "Still to come:").
