---
type: technical-analysis
description: "Research for step 4.9: emulators the user adds (PlayStation 3, Xbox 360, PlayStation 4): licences, what the player must supply, what the console may make easier, what it must not, the law."
component: games
tags: [technical-analysis, games, retro, legal]
---
# The user's own emulators: PlayStation 3, Xbox 360, PlayStation 4 (research, 2026-11-24)

Asked by the owner for [[step-4.9-retro-games-with-retroarch]]: may the user add them, and can the console make it easier without
shipping them and within the law? **Not decided.** Not legal advice.

## They are programs, not RetroArch cores

| | RPCS3 (PS3) | Xenia Canary (Xbox 360) | shadPS4 (PS4) |
|---|---|---|---|
| Licence | GPL-2 | BSD, three clauses | GPL-2 |
| Linux | AppImage (its releases; the latest not checked) | AppImage of 2026-11-24 | a command-line build and an AppImage launcher |
| In Arch | no | no | no |
| System files | Sony's firmware (`--installfw` is in its source; its site refused to be read) | none ("doesn't require any Xbox 360 system files") | modules dumped from a jailbroken console |
| Games | not read (site refused) | a normal console and a USB disk; some need a modded console | dumped, decrypted, from a jailbroken console |
| Start without its window | `--no-gui --fullscreen`, `--config`, `--input-config` (also `--big-picture`) | the game's file as argument (hypothesis) | `--game`, `--fullscreen true` (also `--big-picture`) |
| State | not read | experimental; Vulkan or DirectX 12; "AMD GPUs are not recommended" | "still early in development. Many games do not work" |

The emulators' licences are not the obstacle (all free: OwneetOS could even ship them). The files the player needs are.

## The law

- **Art. 102-quater:** protections the rights holder puts on a work (encryption, copy control) are "efficaci". **Art. 171-ter, f-bis:** punishes
  equipment, products, components or services whose prevalent purpose, or design, is to get round them; its general words ask for
  profit ("a fini di lucro").
- **PlayStation 4:** the emulator's own guide asks for a jailbroken console and decryption. C-355/12 counts disc and console
  protection as one measure ([[retro-discs]]).
- **PlayStation 3:** Sony offers the firmware file freely on its site; its licence (2009 text) allows it "solely … on the PS3 system".
- **Xbox 360:** nothing of the system is needed and a normal console is enough for most games: the clearest of the three.

## What the console may make easier (proposed)

1. A folder for the user's emulators: the console recognises the program it knows and lists that console's games in the library.
2. A game starts straight in full screen with its controller already set, with no desktop window (a guard:
   [[product-invariants]], never a mouse), Guide as ever.
3. It says which program or file is missing, in plain words, and shows the **emulator's official site** (address or code for a phone).
4. Before the first start of an added program: a warning that it is other people's code.

## What it must not do

Ship or download firmware, keys or games; decrypt; link to or explain jailbreaks, keys or dumps; run RPCS3's `--decrypt`
([[legal]]: no DRM circumvention).

## Opinion

- **Xbox 360:** yes to points 1-4, after trying it.
- **PlayStation 3:** points 1-4 without installing the firmware for the user; to the legal review first.
- **PlayStation 4:** no special help: its guide needs a jailbroken console; the general way (a program in the Games
  folder) is the user's own.
- It is a step of its own, after the first build of 4.9: each emulator is tried on the test PC, controller only.

**Not tried:** any of them on OwneetOS; an AppImage unpacks itself at every start here (no FUSE): how long it takes is not known.

## Sources

[RPCS3](https://github.com/RPCS3/rpcs3) (source) · [Xenia Canary](https://github.com/xenia-canary/xenia-canary/wiki/Quickstart) ·
[shadPS4](https://github.com/shadps4-emu/shadPS4/wiki/I.-Quick-start-%5BUsers%5D) ·
[art. 102-quater](https://www.brocardi.it/legge-diritto-autore/titolo-ii-ter/art102quater.html) · [art. 171-ter](https://www.brocardi.it/legge-diritto-autore/titolo-iii/capo-iii/sezione-ii/art171ter.html) ·
[Sony's firmware](https://www.playstation.com/en-us/support/hardware/ps3/system-software/) and [licence](https://www.playstation.com/en-us/legal/ps3-system-software-license-agreement/)
