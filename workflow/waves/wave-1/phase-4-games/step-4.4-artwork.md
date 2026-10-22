---
type: step
description: "Covers of Steam games from Steam's local cache (`appcache/librarycache`, 4.1; no download), covers of games on disks (`cover.jpg` /…"
phase: "[[phase-4-games]]"
step: "4.4"
status: done
legacy: "ROADMAP.md 4.4"
tags: [step, phase-4]
---
# 4.4 Artwork

Up: [[phase-4-games]] · Status: **done**

- **Deliverables:** covers of Steam games from Steam's local cache (`appcache/librarycache`, 4.1;
  no download), covers of games on disks (`cover.jpg` / `cover.png`), generated fallback covers.
- **No demo (owner, 2026-10-16):** the covers and the home screen's card were approved in the
  earlier demos; the new art is checked on preview screenshots instead.
- **Agreed (owner, 2026-10-16, [[game-library]]):**
  - **Covers** (library, home screen's row): the portrait cover (Steam's `library_600x900.jpg` /
    `library_capsule.jpg`, or a disk game's `cover.jpg` / `.png`); else, for Steam games, the
    title header (`header.jpg` / `library_header.jpg`) **shown whole** over the generated art,
    with the title below (option A; option C, the header cropped to fill, if A does not look
    right); else the generated art. In the owner's cache only 112 of 391 apps have a portrait
    cover, 358 a header.
  - **Home screen's card:** Steam's wide picture (`library_hero.jpg`), else the header, else the
    generated art; a game on a disk shows its cover, whole, on the right.
- **Status (2026-10-16):** code written (owneet-frontend 0.19.0): `add_cached_artwork` in the
  Steam provider (both layouts of the cache: files at the top of `librarycache/<appid>/` or in
  sub-folders named after a hash; the newest copy wins), `GameArt.fit`; images another art has
  already loaded are drawn at once (a library opened after the home screen showed none). Preview:
  `tools/preview-steps/artwork.txt`, `artwork-steam-home.txt` (invented pictures).
- **FrankenPC test (2026-10-16):** everything works; all 88 owned games found a portrait cover in
  Steam's cache. Option A kept. **Step approved by the owner (2026-10-16).**
