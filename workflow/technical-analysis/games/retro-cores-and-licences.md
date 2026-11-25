---
type: technical-analysis
description: "Research for step 4.9: which RetroArch cores OwneetOS may ship (licences read at the source, not from Arch's field), which consoles they cover, the BIOS files each one needs, sizes."
component: games
tags: [technical-analysis, games, retro]
---
# Retro games: cores, licences, BIOS (research, 2026-11-24)

For [[step-4.9-the-users-own-emulators]]. The rule is [[legal]]: no NonCommercial terms. How RetroArch fits the console:
[[retroarch-in-the-console]]. Discs: [[retro-discs]].

## Arch's licence field cannot be trusted here

| Arch package | Arch says | What the source says | Ship? |
|---|---|---|---|
| `libretro-genesis-plus-gx` | BSD-3-Clause, LGPL | `LICENSE.txt`: "may not be sold, nor … used in a commercial product or activity" | never |
| `libretro-picodrive` | BSD-3-Clause | `COPYING`: the same clause | never |
| `libretro-snes9x` | GPL, LGPL, custom | `LICENSE`: "freeware for PERSONAL USE only" | never |
| `libretro-mupen64plus-next`, `libretro-parallel-n64` | GPL-2.0 | Both PKGBUILDs build with `HAVE_THR_AL=1`, which adds the angrylion renderer; upstream angrylion is under MAME's old licence (no commercial use) | never Arch's build |

Also NonCommercial in [libretro's list](https://docs.libretro.com/development/licenses/): FinalBurn (all), MAME 2000-2014, Opera (3DO), fMSX and
others. So OwneetOS needs its **own list of allowed cores**, and each one's source is read when its version changes.

## Candidate cores (Arch `extra`, 2026-11-24)

Sources searched for non-commercial wording on 2026-11-24 (a text search, upstream's newest code, not a full audit: that
is done on the exact version when it is packaged); not searched: Kronos, Mesen-S. Sizes: installed, from Arch. BIOS: from `libretro-core-info` 1.22.2.

| Console | Core | Licence | MB | BIOS files (the user's own) |
|---|---|---|---|---|
| NES, Famicom Disk System | Nestopia (or Mesen, GPL-3) | GPL-2 | 4.2 | only for the Disk System |
| Super NES | bsnes (or Mesen-S, GPL-3) | GPL-3 | 3.8 | none (optional ones) |
| Game Boy, Game Boy Color | SameBoy | MIT | 0.3 | none |
| Game Boy Advance | mGBA | MPL-2.0 | 2.3 | none |
| Nintendo DS | melonDS | GPL-3 | 2.1 | none (a free BIOS is inside, BSD) |
| Mega Drive, Master System, Game Gear, SG-1000, 32X, Mega CD | BlastEm | GPL-3 | 10.2 | Mega CD and 32X: required |
| PC Engine, SuperGrafx, PC Engine CD | Beetle PCE | GPL-2 | 3.9 | CD: the system card |
| PlayStation | Beetle PSX HW | GPL-2 | 17.5 | optional: OpenBIOS (MIT) is inside, per libretro's documentation; the core's info file still lists them as required |
| Saturn | Yabause (own BIOS replacement) or Kronos (BIOS required) | GPL-2 | 1.5 / 7.7 | Yabause: optional |
| Dreamcast | Flycast | GPL-2 | 32.8 | optional (a replacement is inside) |
| PSP | PPSSPP | GPL-2 | 18.9 | none (its own support files are needed) |

About 98 MB installed, plus RetroArch. The Arch versions are recent (2026), except Mesen and Mesen-S (2024).

- **BlastEm** replaces Genesis Plus GX and PicoDrive: its libretro source (branch `libretro`, 2026-11-24) accepts 32X, Master System, Game
  Gear, SG-1000 and Mega CD files, and 1.0 came out on 2026-09-11. It is changing quickly: Mega CD saves were added on
  2026-11-21, after Arch's build of 2026-10-10. **To check on the exact build.**
- **SNES:** bsnes is the exact one and heavier than Snes9x; on a PC of OwneetOS's minimum requirements it is **to be measured**.

## To the legal review (7.5) before shipping

- **Nintendo 64:** own build of mupen64plus-next without angrylion (the `HAVE_THR_AL` switch). One file of its GLideN64 renderer
  (`ClipPolygon.cpp`, 1997) only "encourages" companies to contact its author and gives no licence: unclear.
- **Flycast:** its BIOS replacement thanks the author of a "bios decompile work": where it comes from is unclear.

## Left out of the proposal

- **Arcade:** MAME's current core is GPL-2 as a whole, but takes 328 MB, and a user's file works only with the matching MAME version.
- **PlayStation 2, GameCube, Wii:** the Play! core (MIT) and Dolphin (GPL-2) are in Arch; PCSX2 (GPL-3) is only in the AUR. Big and heavy,
  a step of their own.
- **3DO:** Opera is NonCommercial; no free core found.
- **Atari 2600/7800, Lynx, Neo Geo Pocket, WonderSwan, Virtual Boy:** free cores exist (Stella, ProSystem, Handy, Beetle NeoPop, Cygne,
  VB) but not in Arch: built by OwneetOS, if wanted. Computers (C64, Amiga, MSX): not looked at.

## Sources

[libretro licences](https://docs.libretro.com/development/licenses/) · [Arch packages](https://archlinux.org/groups/x86_64/libretro/) and their PKGBUILDs ·
[core info files 1.22.2](https://github.com/libretro/libretro-core-info) · licence files of
[Genesis Plus GX](https://github.com/libretro/Genesis-Plus-GX/blob/master/LICENSE.txt), [PicoDrive](https://github.com/libretro/picodrive/blob/master/COPYING),
[Snes9x](https://github.com/libretro/snes9x/blob/master/LICENSE), [angrylion](https://github.com/ata4/angrylion-rdp-plus) ·
[BlastEm](https://www.retrodev.com/blastem/) · [Beetle PSX HW](https://docs.libretro.com/library/beetle_psx_hw/)
