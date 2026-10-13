---
type: technical-analysis
component: owneet-frontend
legacy: "docs/frontend-architecture.md"
tags: [technical-analysis, frontend]
---
# owneet-frontend — architecture (roadmap step 3.1)

The OwneetOS console interface is **owneet-frontend**, a modified version of
[Pegasus Frontend](https://pegasus-frontend.org) by Mátyás Mustoha and contributors
(GPL-3.0-or-later with additional terms). This document describes how Pegasus is built, how it
works, and what OwneetOS changes in C++ and in QML. Legal requirements: [[legal-compliance]]
 and the introduction of roadmap phase 3.

Decision: [[frontend-fork]] · Practices: [[qml]], [[cpp-qt]]

## 1. Where the code lives

- `frontend/owneet-frontend/`: the Pegasus source, imported **unmodified** in one commit
  (upstream `master`, commit `5d58223e58f84afb31d5d14a67438841b981a6fa`, 2026-10-02), with
  `thirdparty/SortFilterProxyModel` (MIT, commit `2061f8136ba372fd06c1928a610258b7d88cb144`).
  Every OwneetOS change is a separate, later commit, so it can always be compared with upstream.
- **Not imported:** `src/themes/pegasus-theme-grid` (CC BY-NC-SA 4.0, not free), `lang/`
  (translations of Pegasus's own menus, no declared licence), upstream CI files.
- The OwneetOS theme (roadmap 3.3 onwards) is QML inside the fork, under `src/themes/`.
- Third-party code: excluded from the project's shellcheck, SPDX and markdownlint checks.

**Updating from upstream:** list the upstream commits since the imported one, read them, and
apply the useful ones with `git am --directory=frontend/owneet-frontend` (or by hand), one commit
each, noting the upstream commit id in the message.

## 2. Build

| | |
|---|---|
| Build system | CMake ≥ 3.16 (a qmake project also exists; we use CMake) |
| Toolkit | **Qt 5.15** (Arch: 5.15.19 with KDE's patch collection): Core, Qml, Quick, QuickCompiler, Multimedia, Sql, Svg, LinguistTools |
| Gamepads | SDL2 (Arch: `sdl2-compat` on SDL3), option `PEGASUS_USE_SDL2_GAMEPAD` (on) |
| Battery info | SDL2, option `PEGASUS_USE_SDL2_POWER` (on) |
| Result | one executable (`pegasus-fe`, 3.5 MB), QML compiled into it |
| Time | about 35 s in the builder VM (4 CPUs) |

Checked on 2026-10-08 in a chroot pinned to the ISO's Arch snapshot: the build succeeds; 20 of
the 23 upstream tests pass with `QT_QPA_PLATFORM=offscreen`; 3 QML scene tests (`KeyEditor`,
`Blurhash`, `SortFilter`) abort without a GPU context, exactly as on unmodified upstream (to be
run in the test VM, step 3.2).

**Qt 6 is not possible yet.** Pegasus's CMake looks for Qt 6 first, but the frontend still needs
Qt 5-only parts (`QuickCompiler`, the Qt 5 translation macros): with Qt 6 installed, CMake mixes
both versions and stops. The Qt 6 port stays a later step, as planned ([[architecture-stack]]).

**Image size:** the frontend adds about 95 MiB installed (Qt 5 base, declarative, multimedia,
SVG and a few small libraries), roughly 30 MiB in the compressed ISO (now 1671 MiB of 2 GB).

## 3. How Pegasus works, and 4. what OwneetOS changes

- [[frontend-pegasus-internals]] — structure, theme API, data providers, game launching.
- [[frontend-steam-local-files]] — Steam's local files (step 4.1).
- [[frontend-input]] — gamepad input and the OwneetOS input map.
- [[frontend-changes]] — changes in C++ and in QML.

## 5. Checks for step 3.2

- The frontend runs in gamescope in the test VM with the minimal theme, driven by a gamepad.
- The 3 QML tests run in the test VM (GPU context).
- RAM of the frontend at idle (constraint C1: system + UI under 500 MB).
- Seamless handover from the boot splash to the interface.
