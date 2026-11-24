---
type: technical-analysis
description: "Research for step 4.9: the user's own game discs, played straight from the drive or copied (which consoles' discs a PC drive reads, what RetroArch does, the law in Italy and the EU)."
component: games
tags: [technical-analysis, games, retro, legal]
---
# Retro games from the user's own discs (research, 2026-11-24)

For [[step-4.9-retro-games-with-retroarch]] (the owner's proposal to copy, GitHub's issue 2 to play from the disc). Not legal advice.

## What a PC drive reads

| Disc | Readable | Source |
|---|---|---|
| PlayStation | yes | PCSX2 and libretro's disc project |
| Saturn, Mega CD | yes: libretro's disc project (2019) plays them; its Mega CD core is NonCommercial ([[retro-cores-and-licences]]) | [post](https://www.libretro.com/index.php/retroarch-disc-project-alpha-testing-has-begun-details-inside/) |
| PC Engine CD | no source found | - |
| PlayStation 2 | yes, "unencrypted DVDs and CDs" | [PCSX2](https://pcsx2.net/docs/setup/dumping) |
| Dreamcast (GD-ROM) | no: the high-density area only with a few drives | [Redump](https://wikiredump.pages.dev/index.php%3Ftitle=GD-ROM_Dumping_Guide) |
| GameCube, Wii | no: only some old drives | Dolphin's forum |

## What RetroArch does (1.22.2)

- **Plays from the disc** with Beetle PSX and Beetle Saturn (not in Arch). Not with Yabause or BlastEm, as far as found.
  The post (2019) warns: not with its "precache" disc setting; its Vulkan renderer can break it; LibCrypt games did not work.
- It finds drives through **`/dev/sg0` to `/dev/sg9`** only (`cdrom.c`, one digit) and needs the `sg` module; the name is
  `cdrom://drive1.cue`. **Hypothesis to try:** that name given on the command line.
- **Copies** ("Dump Disc") to bin/cue, from its menu only, in its downloads folder. No command for it was found: the console would use
  a copying program of its own.
- PCSX2 advises against playing from the disc (wear); reading from a drive is also slower than from a file.

## The law

- **Backup copy of a program:** Italian law 633/1941, art. 64-ter, par. 2, as Directive 2009/24, art. 5(2): a contract cannot prevent
  it, "in so far as it is necessary for that use". Only for who has the right to use it: a copy cannot go with a resale
  (Court of Justice, C-166/15, Ranks, on the older directive).
- **A game is more than a program:** C-355/12 (Nintendo / PC Box, par. 23): a videogame is complex matter; its pictures and
  sounds are protected by Directive 2001/29 too.
- **Private copy** (art. 71-sexies): of "fonogrammi e videogrammi", for personal use. Games are not named.
- **Protection:** C-355/12 takes the protection of the disc and the console together as one measure. Whether reading a disc that an
  ordinary drive reads goes round it: not found.

**Reading of it (opinion):** a copy of one's own disc is **not clearly allowed**, above all with discs that still work.
Playing from the disc keeps no copy, so it looks safer (the law on temporary copies was not read). Both go to
[[step-7.5-legal-review-before-the-public-launch]].

## Proposed

- **Not in the first build of 4.9.** Then, one at a time, only with the owner: PlayStation discs played straight from the
  drive (Beetle PSX, free licence; own a drive on a test PC first); copying only after the legal review.

## Sources

[art. 64-ter](https://brocardi.it/legge-diritto-autore/titolo-i/capo-iv/sezione-vi/art64ter.html) ·
[art. 71-sexies](https://brocardi.it/legge-diritto-autore/titolo-i/capo-v/sezione-ii/art71sexies.html) ·
[2009/24](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32009L0024) ·
[C-355/12](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62012CJ0355) · [C-166/15](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62015CJ0166)
