---
type: technical-analysis
description: "Research for step 4.9: how RetroArch fits the console (its own build, commands over stdin, Guide, the user's folders, BIOS, covers, the catalogue) and what is left to choose."
component: games
tags: [technical-analysis, games, retro]
---
# RetroArch in the console (research, 2026-11-24)

For [[step-4.9-the-users-own-emulators]]. Cores: [[retro-cores-and-licences]]. RetroArch 1.22.2 (GPL-3) read at the source.

## What was found

- **Starting a game:** `retroarch -L <core> <game>` with `--config` / `--appendconfig`: a program like any other for owneetd.
- **Arch's package** (17.4 MB) needs `qt6-base` (about 71 MB, not on the console; only for its desktop window) and leaves the
  network on. The other dependencies looked up are already there. **Own build** proposed (as DOSBox Staging):
  no Qt, no network, so no online updater either (it would download NonCommercial cores).
- **Commands from the console:** RetroArch has `SAVE_STATE`, `LOAD_STATE`, `STATE_SLOT_PLUS` / `MINUS`, `RESET`, `DISK_EJECT_TOGGLE`, `DISK_NEXT` /
  `PREV`, `PAUSE_TOGGLE`, `MENU_TOGGLE`, `QUIT`. Over the network they are a UDP port bound to every interface (`command.c`,
  `AI_PASSIVE`): **never used**. Over **stdin** (`stdin_cmd_enable`) they come only from who started it: owneetd.
- **Guide:** with RetroArch's `udev` driver, its controller profiles bind Guide to its menu (e.g. the Xbox One S profile:
  `input_menu_toggle_btn = "8"`), which the guard [[product-invariants]] forbids. With its `sdl2` driver the built-in layout has neither
  Guide nor a menu button, and works with no profile: proposed, with the menu binding and combos off.
- **The folders:** a file's extension does not say its console (`.bin`, `.cue`, `.iso`, `.chd` belong to several). Batocera uses one folder per
  console (`roms/<system>/`) and lists only consoles that have games; its `bios/` folder is checked, the missing files listed with their
  MD5.
- **Covers:** libretro's thumbnails (thumbnails.libretro.com, matched by name) carry **no licence**; their README says the art belongs to the
  games' developers and publishers.
- **Internet:** the emulators may be downloaded once (owner, 2026-11-24, [[product-invariants]]); after that, offline. In the ISO or
  downloaded: to choose ([[retro-non-commercial-cores]] for the ones that may not be shipped).
- **The catalogue of 5.0.0** ([[optional-apps]]) knows two kinds, `webapp` (opened by the user) and `engine` (hidden, packages). Installing
  and removing an engine's packages from the ISO's bundled repository already works; a tile for something that is not a web
  app is **new**: a third kind, to build.
- **Batocera in a game:** Hotkey + a button saves, loads, opens the menu, leaves. Here the system may take nothing but Guide while
  a game runs ([[product-invariants]]).

## Proposed

1. **No RetroArch menu**, so its name, look and technical words are never seen. The console offers in its own look, on the home
   screen (Guide, then the running game's options): save the game's state, load it, change disc, restart. owneetd
   sends them over stdin. **No new controller binding.** The cost: RetroArch's own settings (shaders, filters, remapping)
   are not reachable in Wave 1.
2. **One folder per console** in the Games folder, under one folder for retro games: names to choose in the demo.
3. **BIOS:** a folder of the user's; the console says which file a game needs and does not have.
4. **Covers local only:** the picture next to the game, or chosen as in step 6.9 ([[step-6.9-cover-images-from-a-disk]]).
5. **Saves:** to decide in the demo's step: next to the game when the disk can be written, as GOG's DOS games ([[games-on-disk]]).

## To try before the demo's approval becomes code (hypotheses)

- stdin commands reach RetroArch inside the scope owneetd starts a game in; SAVE_STATE while the game is behind the home screen
  (RetroArch pauses without the focus by default: `pause_nonactive`).
- The `sdl2` driver with the console's controllers (Xbox, PlayStation), and their order with more players.
- Test games: free homebrew, the names agreed with the owner first.

## Sources

[Network commands](https://docs.libretro.com/development/retroarch/network-control-interface/) · [command line](https://docs.libretro.com/guides/cli-intro/) ·
RetroArch 1.22.2: `command.c`, `net_socket.c`, `input_autodetect_builtin.c`, `qb/` ·
[controller profiles](https://github.com/libretro/retroarch-joypad-autoconfig) · [Arch's PKGBUILD](https://gitlab.archlinux.org/archlinux/packaging/packages/retroarch) ·
[Batocera: games and BIOS](https://wiki.batocera.org/add_games_bios), [hotkeys](https://wiki.batocera.org/basic_commands) ·
[thumbnails](https://github.com/libretro-thumbnails/libretro-thumbnails)
