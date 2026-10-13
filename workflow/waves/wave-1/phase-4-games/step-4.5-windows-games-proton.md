---
type: step
description: "Windows DRM-free games start like any other: umu-launcher + GE-Proton, one prefix per game, never named in the interface; a 'preparing…"
phase: "[[phase-4-games]]"
step: "4.5"
status: todo
legacy: "ROADMAP.md 4.5"
tags: [step, phase-4]
---
# 4.5 Windows games (Proton) *(added 2026-10-11)*

Up: [[phase-4-games]] · Status: **todo**

- **Deliverables:** Windows DRM-free games start like any other: umu-launcher + GE-Proton, one
  prefix per game, never named in the interface; a "preparing the game" screen until the game's
  first picture. Credits and licences (Wine LGPL, Proton BSD, DXVK / VKD3D-Proton zlib/LGPL).
- **Decided (owner, 2026-10-11):** Proton and its runtime (about 1 GB) stay out of the ISO:
  downloaded once, in the background, the first time the console is online; until
  then a Windows game says that it needs a one-time download (the only exception to C9).
- **Broken Linux versions of Steam games (owner, 2026-10-13):** some Steam games ship a Linux
  version that cannot start (e.g. Dragon's Wake, 399070: its Linux files lack the executable its
  launch settings name; Steam says "Missing game executable"). owneetd notices the failed launch
  in Steam's log and the console asks "This game's Linux version does not start. Try the version
  for Windows?" [Try] [Cancel]; Try sets Proton for that game in Steam (Steam closed and reopened:
  it saves the setting only while closed) and starts it again. Demo first; checked on real
  hardware with the owner's account (it reads an undocumented Steam log).
- **Note:** shader pre-compilation exists only for Steam games (Steam's own "Processing
  Vulkan shaders"); other games compile while they play, so the "preparing" screen covers the
  start only.
