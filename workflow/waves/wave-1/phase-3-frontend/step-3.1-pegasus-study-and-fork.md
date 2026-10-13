---
type: step
phase: "[[phase-3-frontend]]"
step: "3.1"
status: done
legacy: "ROADMAP.md 3.1"
tags: [step, phase-3]
---
# 3.1 Pegasus study and fork

Up: [[phase-3-frontend]] · Status: **done**

- **Deliverables:** clone `mmatyas/pegasus-frontend` (master, with submodules), fork on GitHub as
  `owneet-frontend`, [[frontend-architecture]] describing build system, data providers, theme
  API and the extension points we need, and what must be removed or disabled for the legal
  requirements above.
- **Done when:** the owner has a clear picture of what we change in C++ and what stays in QML.
- **Outcome:** owner's choice: the fork lives **inside this repository** (`frontend/owneet-frontend`,
  no separate GitHub repository). Pegasus `5d58223` imported unmodified (without the CC BY-NC-SA
  grid theme, the unlicensed translations and upstream CI files), then a minimal own theme as the
  built-in default. Builds against the ISO's snapshot with Qt 5.15 (Qt 6 not possible yet: the
  frontend still needs Qt 5-only parts); 20/23 upstream tests pass headless, the 3 QML scene tests
  need a GPU context (same upstream). About +30 MiB in the ISO. [[frontend-architecture]]:
  build, structure, theme API, providers (kept / compiled out), launching (Pegasus unloads its UI
  during games and runs them as children: replaced by owneetd launching, UI kept loaded), the
  owneetd client in C++ (QML cannot reach a Unix socket), and the list of C++ changes.
