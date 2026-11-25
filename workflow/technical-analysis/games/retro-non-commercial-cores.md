---
type: technical-analysis
description: "Research for step 4.9: emulators that OwneetOS may not ship (non-commercial licences), downloaded by the user's own console instead: what it takes, from where (libretro or Arch), pros, cons, what it would add."
component: games
tags: [technical-analysis, games, retro, legal]
---
# Non-commercial cores downloaded by the user's console (research, 2026-11-24)

Asked by the owner for [[step-4.9-the-users-own-emulators]] ("the third way"). **Not decided.** The guard [[legal]] applies until
the owner writes that such a download is allowed.

## What it would add to the free cores ([[retro-cores-and-licences]])

| Core | Adds | In Arch |
|---|---|---|
| FinalBurn Neo, MAME 2003-Plus | arcade (small, unlike MAME) | no |
| Opera | 3DO | no |
| mupen64plus-next (Arch's, with angrylion) | Nintendo 64 | yes |
| Snes9x | Super NES, lighter than bsnes | yes |
| Genesis Plus GX, PicoDrive | the consoles BlastEm has already | yes |

Nothing for PlayStation 2, 3, 4, GameCube, Wii and Xbox: their emulators in Batocera are programs of their own, not read one
by one for their licence here (shadPS4 and Dolphin GPL-2, PCSX2 GPL-3).

## Where from

| | libretro's server (as RetroArch's own updater) | Arch's archive (as the system's packages) |
|---|---|---|
| Cores | all | not arcade, not 3DO |
| Checked by | CRC32 in a list, no signature or SHA-256 next to the files; HTTPS works | Arch's signatures, checked by pacman |
| Version | the last nightly only, rebuilt every day: not the one tried | pinned to a date, as the release's |
| Server | wiped by an attacker in August 2020, then restored | already used to go back to a version |
| Size | Snes9x 1 MB | Snes9x 0.9 MB |

## What it takes

Window with the licence's terms and consent (as Widevine's), download with progress and errors (as Windows games'), install
and remove (`owneet-apps` already does it with pacman from the ISO's bundle: a second source, Arch's archive, to add), the
version with each release, demo, texts in every language, credits. For libretro: a checksum of ours per file cannot be
kept, as the file changes every day.

## Pros

- OwneetOS's ISO and repository stay fully open source (C5) and fit SourceForge; nobody's sale of a console is touched by what
  the ISO holds. A known pattern: Widevine here; Debian's `ttf-mscorefonts-installer` (kept apart, in contrib).
- Users get what Batocera gives for these consoles, if they want it.

## Cons

- The law is not settled by it: OwneetOS would offer the download. Snes9x says "freeware for PERSONAL USE only": fine for
  a player, not for a shop's console. No ruling or opinion found: [[step-7.5-legal-review-before-the-public-launch]].
- Arch publishes those packages with a wrong licence field ([[retro-cores-and-licences]]): its archive may drop them.
- From libretro: code not signed and not the one tried, run on the console without a sandbox ([[supply-chain-security]]).
- Internet the first time, and the user's address reaches a third party (it already does with Arch's servers).
- More to keep up at every release, for few consoles.

## Opinion

Little for its cost: with free cores only, **arcade, 3DO and an easy Nintendo 64** are missing. If wanted: Arch's archive only, as an
addition after the first build of 4.9. FinalBurn Neo and Opera by the user's own cores folder (the user puts the file there).

## Sources

[libretro's server](https://buildbot.libretro.com/nightly/linux/x86_64/latest/) (2026-11-24: list with CRC32; `.sig`, `.asc`, `.sha256` not found) ·
[the attack of 2020](https://www.gamingonlinux.com/2020/08/libretro-retroarch-were-hacked-wiping-some-repositories/page=1/) ·
[Arch's archive](https://archive.archlinux.org/packages/l/libretro-snes9x/) (with `.sig`) · RetroArch's `config.def.h`, `task_core_updater.c` ·
[Debian](https://packages.debian.org/stable/ttf-mscorefonts-installer)
