---
type: decision
description: "C1-C9: lightweight, gamepad only, x86_64, minimal Arch, GPLv3, English, name, modular, offline."
area: product
status: active
decided: 2026-10-03
updated: 2026-10-11
legacy: "PROJECT_RULES.md §2"
tags: [decision, product]
---
# Hard constraints (C1–C9)

The constraints every part of OwneetOS must respect. Code and documents refer to them by number.

| # | Constraint |
|---|---|
| C1 | **Lightweight** is a must: no bloatware, minimal RAM/CPU/disk footprint. Target: system + UI idle under **500 MB RAM** (with Steam and Brave closed). |
| C2 | **Gamepad-only** operation everywhere (installer, first setup, apps, settings). |
| C3 | Architecture: **x86_64 only**. ARM is out of scope. |
| C4 | Base distro: **minimal Arch Linux**. No desktop environment, no display manager. |
| C5 | **Fully open source**, license **GPLv3** (also required by the Pegasus fork). |
| C6 | **English is mandatory** for code, comments, documentation, commit messages, issues and PRs. The UI itself is multilingual. |
| C7 | The OS name **OwneetOS** is final. |
| C8 | Prefer modular, independent components — within feasibility and without creating bloat. |
| C9 | Must work **offline** for local / DRM-free content; internet is needed only for streaming and stores. |

**Exception to C9** (2026-10-11): Proton and its runtime are downloaded once, in the background,
the first time the console is online ("a necessary evil") — see [[games-on-disk]].
**C1 is measured with Steam closed**: Steam is started only when needed ([[steam-integration]]).

## Creates

- Guards: [[product-invariants]], [[collaboration]] (English).
- Best practices: [[dependencies]], [[testing-and-verification]] (RAM measurements).
- Product goal: [[vision]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-03 | Public repo; English mandatory for all project text. |
| 2026-10-11 | Proton and its runtime are downloaded once, in the background, the first time the console is online ("a necessary evil": the only exception to C9, for Windows games before the first connection). Installing a game from an installer first shows "By installing you accept the game's licence" [Read] [Install] (the user is informed, the project is covered). Step 4.1 approved. |
