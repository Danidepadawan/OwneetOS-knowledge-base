---
type: decision
description: "Steam in the ISO, controller-only Steam, its screens shown automatically, 12 GB RAM in the live session."
area: games
status: active
decided: 2026-10-11
updated: 2026-10-14
legacy: "PROJECT_RULES.md §8 (Steam), §13 (2026-10-11, 2026-10-12)"
tags: [decision, games, steam]
---
# Steam integration

- **Steam is in the ISO** with 32-bit drivers for every GPU (about +300 MiB, [multilib] from the
  same snapshot); Steam's runtime is downloaded by Steam on first launch.
- Steam runs in `-gamepadui` mode. Anything the console opens (Steam included) must be fully usable
  with the controller: first start, login (Steam Guard included), store, installing, launching and
  closing a game. The user must **never** be forced to use a mouse or keyboard
  ([[hard-constraints]] C2), and Guide always brings back the home screen with the selection where
  it was ([[guide-button]]).
- Steam's own screens (login, progress of a game's launch) are **shown by the console
  automatically** when they matter: the user never has to look for them. The console shows its own
  "Preparing Steam" screen during Steam's first download.
- **Live session:** Steam's first download (about 2.4 GB) is kept in RAM, so Steam opens only with
  **at least 12 GB of RAM**; otherwise a clear message asks to install OwneetOS to use Steam. The
  installed system's requirements do not change (4 GB minimum, 8 GB recommended); Steam is started
  only when needed (C1 is measured with Steam closed).
- **Guide over Steam**: a short press is Steam's, holding 1 second comes back ([[guide-button]]).
- **Steam without its interface** (2026-10-14, replaces "owned games are installed from Steam's
  library"): Steam runs hidden and the console replaces its interface in everyday use, because
  with the NVIDIA driver Steam's own window shows glitches no setting removed (a known problem of
  X11 windows on that driver; not reported upstream for now). Every owned game is listed by the
  console from Steam's local caches (88 games on the owner's account, as Steam shows); installing
  goes through Steam's official `steam://install/<appid>`, whose confirmation window is the only
  Steam window left in everyday use, announced on NVIDIA as a temporary display problem (option
  a); the console shows the download itself. Writing Steam's files to start downloads is turned
  down. Step: [[step-4.2c-steam-without-its-interface]]. Library: [[game-library]].
- **Installing and uninstalling** (demo 4.2c proposal, 2026-10-14): the console asks first
  ("Install {game}?"), then, **on NVIDIA only**, a notice "Before Steam opens": Steam's window
  *might* show display errors for a moment (never naming the driver), **every time until the
  user ticks "Don't show again"**; then Steam's confirmation window. The same before the store.
  *(2026-10-14 to 2026-10-15 the notice also said what to press, on every PC: dropped once Steam's
  window became readable with the repaint overlay, owner 2026-10-15.)*
- **Starting a game**, Steam stays hidden behind the console's "Starting …" screen, also while it
  prepares the game's shaders; it is shown only if it seems to wait for the user.
- **Steam's window on NVIDIA** (2026-10-15): while it is on screen, owneetd keeps gamescope
  composing every frame (a changing, all but transparent one-pixel overlay), which removes the
  stale parts of the window; permanent on NVIDIA until Valve fixes the problem
  ([[step-4.2c-steam-without-its-interface]]).
- **"How to come back from Steam"** (owner, 2026-10-15): before Steam's window opens the first
  time after each start of the console (store, installing, uninstalling, a licence agreement),
  a window says to hold Home to come back, and to close Steam (Menu on its tile) when a page
  keeps loading; "Don't show again" ends it. *(It replaced a bar drawn over Steam's window for 6
  seconds, which did not show on the FrankenPC.)*
- **Steam Input for every controller** (owner, 2026-10-15): the console turns on the account's
  `SteamController_XBoxSupport`, `SteamController_SwitchSupport` and
  `SteamController_GenericGamepadSupport` (localconfig.vdf, UserLocalConfigStore; read on the
  FrankenPC) once per account, while Steam is closed; PlayStation controllers keep Steam's
  default ("on in games without support"). Later choices in Steam are kept.
- **Steam's pages with the GPU on NVIDIA** (owner, 2026-10-15): since the repaint overlay they no
  longer show stale pictures with it, so `-cef-disable-gpu` is dropped (test switch
  `owneet.debug.steam_cef_gpu=off` brings it back); turned off again if the defects return.
- **Closing Steam** (owner, 2026-10-15): Menu on the home screen's Steam tile while Steam runs:
  "Close Steam?" (downloads stop; a Steam game running closes too), Cancel first. Also the way
  out of a Steam page that never finishes loading.
- **Licence agreements** Steam asks to accept at a game's first start: the console first shows
  its own window with the agreement's official address as a QR code (to read on a phone) and
  "in Steam's window, press Left and then A to accept"; Steam is then shown at once. The console
  never moves Steam's selection to "Accept" itself (owner, 2026-10-14). The same notice comes before **Steam's store** on those PCs, as long as the store is
  Steam's own window (until [[step-5.1-brave-in-the-os]]). **Uninstalling** must always be possible without Steam's interface: Options →
  "Uninstall" (and "Cancel installation" while a game downloads) goes through Steam's official
  `steam://uninstall/<appid>`, with the same console question and notice before Steam's window.
  Downloads are shown on the game's cover, in its details, in the home screen's notices, and a
  banner says when a game is ready.
- **No internet**: when an action needs the internet (Steam's first download, signing in to
  Steam, installing a game) and there is none, the console says so plainly and **blocks the
  action** with a clear message and a way to the network settings; it never shows "Preparing
  Steam" or "Steam opens by itself" then. *(Owner, 2026-10-14: today the "Preparing Steam" screen
  shows and disappears after a second offline, and its last words, "Steam opens by itself", are
  not true.)*
- **A Steam game whose Linux version cannot start** (Steam: "Missing game executable") gets an
  automatic recovery, offered to the user: try the version for Windows with Proton
  ([[step-4.5-windows-games-proton]]).
- Steam stays in the ISO until [[optional-apps]] arrive (step 5.0): then it is downloaded when chosen.

Technical design: [[owneetd-api-apps]], [[frontend-steam-local-files]]. Steps: [[step-4.1-steam-library]],
[[step-4.2-steam-integration]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-11 | Steam library (step 4.1): installed games only, from local files; games on a disk that is not connected are not shown; owned games that are not installed are installed from Steam's own library, because no local file lists them with certainty (the licence packages gave 92 games, the client shows 90). Steam, like everything the console opens, must work with the controller alone ([[game-library]]). |
| 2026-10-11 | Demo 4.2 approved (with the generic store icon for Steam and no "Add games" in Favorites). **Distribution:** the ISO goes to SourceForge, the website to a `.org` domain on GitHub Pages, packages stay on GitHub ([[distribution-and-updates]]). **Steam is in the ISO** with 32-bit drivers for every GPU (about +300 MiB, [multilib] from the same snapshot). |
| 2026-10-11 | Steam in the **live session** (no installed disk: Steam's first download of about 2.4 GB is kept in RAM): only with at least **12 GB of RAM**; otherwise a clear message asks to install OwneetOS to use Steam. The **installed system's requirements do not change** (4 GB minimum, 8 GB recommended); Steam is started only when needed (C1 is measured with Steam closed). |
| 2026-10-12 | After the owner's first Steam test (Guide fought over by owneetd and Steam): **while Steam or a Steam game is on screen, a short Guide press is Steam's; holding Guide for 1 second comes back to the console** (option A; [[controller-input-map]]). "Exit Steam" in Steam's menu also comes back. Steam's own screens that matter (login, a game's launch progress) are shown automatically ([[game-library]]). |
| 2026-10-13 | A Steam game whose Linux version cannot start (Steam: "Missing game executable") gets an automatic recovery, offered to the user: try the version for Windows with Proton ([[step-4.5-windows-games-proton]]). |
| 2026-10-14 | **Steam without its interface:** Steam runs hidden; every owned game is listed from Steam's local caches (licences in `packageinfo.vdf`, types in `appinfo.vdf`, package 0 and inactive licences left out: 88 games, as Steam shows); installing through `steam://install/<appid>` (Steam's confirmation window, announced on NVIDIA as a temporary display problem; option a), the download shown by the console. Replaces "owned games are installed from Steam's library" (2026-10-11). Reason: glitches in Steam's own window with the NVIDIA driver, NVIDIA-only (same ISO clean on AMD), not removed by any setting. |
| 2026-10-14 | Proposal for demo 4.2c agreed: the console asks before installing; the NVIDIA notice comes every time until "Don't show again"; uninstalling (and cancelling a download) through `steam://uninstall/<appid>`, so a game can always be uninstalled; downloads shown on the cover, in the details, in the home notices and with a "ready" banner; **without internet, an action that needs it is blocked with a clear message** (today's "Preparing Steam" screen disappears offline and wrongly says Steam opens by itself). |
| 2026-10-14 | Demo 4.2c review: the display-errors notice also comes before Steam's store (Steam's own window until step 5.1). |
| 2026-10-14 | After the FrankenPC test: the notice before Steam's confirmations says what to press, on every PC; Steam stays hidden while it prepares a game's shaders; owned games = every licence but package 0 and free weekends. |
| 2026-10-15 | The notice before Steam's window: NVIDIA only again, titled "Before Steam opens", "might show", without what to press; the home screen's "Steam Store" app is named "Steam". |
| 2026-10-15 | Steam's window on NVIDIA: gamescope kept composing every frame while it is on screen, permanent until Valve fixes the problem (clean in the FrankenPC test); if it fails, reverted. Other bugs first, Steam's visual defects afterwards. |
| 2026-10-15 | Steam's pages keep the GPU on NVIDIA (no defects came back with it). "Close Steam" from the home screen's Steam tile. |
| 2026-10-15 | The bar over Steam's window did not show: replaced by a window "How to come back from Steam" at the first opening of Steam's window after each start, until "Don't show again". Steam Input turned on for Xbox, Switch and generic controllers once per account. |
| 2026-10-14 | Licence agreements at a game's first start: the console's window with a QR code of the official address and "press Left and then A to accept"; the console does not move Steam's selection. |
