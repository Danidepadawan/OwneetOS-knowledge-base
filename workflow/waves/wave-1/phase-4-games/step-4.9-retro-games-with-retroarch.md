---
type: step
description: "Retro games with RetroArch, as Batocera does: the user's own ROMs from a folder on the disks, in the console's library; cores with free licences; BIOS files the user's own. After the games' tests, before the legal review."
phase: "[[phase-4-games]]"
step: "4.9"
status: in-progress
tags: [step, phase-4]
---
# 4.9 Retro games with RetroArch *(added 2026-11-21)*

Up: [[phase-4-games]] · Status: **in-progress**

- **Origin:** moved from Wave 2 (item 11b of [[wave-2]]) by the owner on 2026-11-21: the idea of "ownership" has to come
  across in the first release; "exactly what Batocera does".
- **When (owner):** at the end of the games' tests, before the legal review ([[step-7.5-legal-review-before-the-public-launch]]),
  so that the review covers it.
- **Deliverables (from [[wave-2]] 11b):** RetroArch as an optional app ([[step-5.0.1-optional-gaming-apps]]); the user's
  own ROMs from a folder on the disks, listed in the library like any other game; BIOS files the user's own, never
  shipped; Guide stays owneetd's (RetroArch's menu through a binding agreed in [[controller-input-map]] first); covers
  local (libretro's thumbnails only if the owner agrees).
- **Open, for the owner:** Batocera ships cores whose licences forbid commercial use (Snes9x, Genesis Plus GX,
  PicoDrive, FinalBurn Neo, Opera: libretro's licence list), which [[legal]] forbids OwneetOS to ship. With free
  licences only, other cores cover the same consoles (to list with sources before the step starts).
- **Proposed by the owner, to study:** the user's own CD and DVD discs (e.g. PlayStation, PlayStation 2) copied by the
  console from a disc drive to its disk and played from there. Technique and law (a private copy, no protection
  circumvented, [[legal]]) researched with sources, and a question for the legal review.
- **Asked on GitHub (issue 2, 2026-11-22):** playing straight from the disc, not only from a copy. Found (to confirm when
  the step starts): RetroArch's "Load Disc" plays physical CDs with some cores (Beetle PSX, Beetle Saturn; others with
  NonCommercial licences) and "Dump Disc" copies them as bin/cue, working better on Linux (the `sg` module may be
  needed); PCSX2 has a disc mode (`-disc`) but advises copying the game first. Both ways to weigh with the owner.
- **First:** research with sources, a demo of what the user sees ([[demo-before-code]]), the controller bindings.
- **Order (owner, 2026-11-24):** 4.9 before [[step-5.0.1-optional-gaming-apps]]; RetroArch goes into today's catalogue by itself.

## Research (2026-11-24)

[[retro-cores-and-licences]] (what may be shipped, which consoles, BIOS), [[retroarch-in-the-console]] (how it fits, what is
proposed), [[retro-discs]] (discs and the law). **Waits for the owner's choices**; then the demo.

**Owner (2026-11-24):** a first installation that needs internet is acceptable; why can Batocera emulate up to the PlayStation 4
and OwneetOS cannot, and may the user add emulators of their own? (Internet: the owner added the
retro emulators' one-time download to the guard [[product-invariants]].)

**Found (2026-11-24):**
- Batocera's own code is LGPL-3; the whole is "a mix of GPL, LGPL, BSD, MIT and non-commercial licenses", so selling it
  preinstalled "is forbidden" ([licence page](https://wiki.batocera.org/license)). It ships no BIOS and no commercial game. The non-commercial licences read allow free
  redistribution: **not shipping them is OwneetOS's own rule ([[legal]]; its text says "assets"), not the law.**
- What would stop OwneetOS from shipping them: code put on SourceForge must be under an OSI-approved or compliant licence
  ([terms, section 10](https://slashdotmedia.com/terms-of-use/)); nobody could sell a console with OwneetOS; donations ([[step-7.10-donations-choice]]) to weigh.
- PlayStation 4 in Batocera is shadPS4, a program of its own (GPL-2, not a RetroArch core): "very experimental", AVX2 and Vulkan 1.3,
  "may need" system modules from a jailbroken console ([page](https://wiki.batocera.org/systems:ps4)). Its repository has packages also for
  PCSX2, RPCS3, Dolphin, Cemu, xemu, Xenia, Vita3K. The limit of the first proposal was the step's scope (RetroArch),
  not a licence: each one is an integration of its own (controller, Guide, saves, settings without a mouse).
- The user's own emulators: RetroArch loads any core file it is given, so a folder of the user's cores is possible (native
  code: a warning, as for the Proton tools of [[wave-2]]). An emulator as an AppImage in the Games folder already fits
  [[frontend-disk-games]] (not tried). Pages of Batocera read: custom systems yes, a way to add a core not found.
- A third way: the user's own console downloads a non-commercial core from libretro, with consent (as Widevine): nothing
  redistributed by OwneetOS. Not checked yet: libretro's signing ([[supply-chain-security]]), the legal review; the guard [[legal]]
  does not say whether a download by the user's console counts, so it applies until the owner writes it.
  Looked into at the owner's request, pros and cons: [[retro-non-commercial-cores]].
- The user's own PlayStation 3, Xbox 360 and PlayStation 4 emulators (the owner's question, 2026-11-24): [[retro-users-own-emulators]].
- **The owner's wish (2026-11-24):** any emulator the user wants, put in a folder by the user, little work, nothing from OwneetOS
  that may bring its authors legal trouble: a folder per console with its emulators and its games. Found feasible, same note;
  waits for the owner's go.
