---
type: step
description: "Appearance (palette, text size, reduce motion, persisted), Network, Controllers and Bluetooth, Audio, Display (resolution, refresh rate…"
phase: "[[phase-3-frontend]]"
step: "3.9"
status: done
legacy: "ROADMAP.md 3.9"
tags: [step, phase-3]
---
# 3.9 Settings *(multi-prompt; demo approved 2026-10-09; approved 2026-10-10)*

Up: [[phase-3-frontend]] · Status: **done**

- **Deliverables:** Appearance (palette, text size, reduce motion, persisted), Network, Controllers
  and Bluetooth, Audio, Display (resolution, refresh rate via gamescope; with several screens,
  which one the console uses), Language, Storage (read-only), System (version, restart, shut down).
- **Known issue to fix here (2026-10-08, owner's desktop with two monitors on two GPUs):**
  gamescope uses one screen; a screen on the other GPU keeps showing the frozen boot splash.
  **Decision 2026-10-10:** the other screens are turned off (gamescope turns off those on its own
  GPU; those on other GPUs need a small privileged helper). The logo on other screens is an
  optional choice after Wave 1; using a second screen for something (e.g. chat, guides) is a
  possible later feature.
- **Demo:** `design/demos/3.9-settings.html`. Proposals in it: the sections in a list on the left
  and the panel on the right, which follows the selection; right or A enters the panel, B (or left
  at its edge) goes back to the list; sliders change with left / right (the click plays at the new
  volume); up / down go to the nearest row first, so a row of buttons is never skipped.
  **Network:** offline notice, Wi-Fi switch, cable status, networks nearby (connected, saved,
  signal, open or protected), password window (typed with the on-screen keyboard, 3.10), wrong
  password, Menu on a saved network: disconnect / forget. **Controllers and Bluetooth:** connected
  controllers with connection and battery, **"Pair a new controller"** (also with a controller
  already connected: owneetd's auto-pair for a while) with per-brand instructions (Xbox,
  PlayStation, Nintendo, others; wired ones need nothing), known devices with Menu → forget.
  **Sound:** output picker, volume, mute, interface sounds on/off and their volume. **Display:**
  with several screens, the one the console uses and "Other screens: show the OwneetOS logo / turn
  off" (logo by default); resolution and refresh rate (Automatic recommended). **Appearance:** as
  in demo 3.3. **Language:** picker; on-screen keyboard layout follows the language. **Storage:**
  disks with free space and notices. **System:** version, check for updates (7.1), Sleep /
  Restart / Shut down with confirmation (Cancel first), **About → Credits and licences** (the
  projects of CREDITS.md, then every installed package with its licence).
- **Review 1 (2026-10-09):** (1) the pairing window draws generic controller outlines with the
  buttons to hold marked where they really are (pairing / sync button on the top edge next to the
  cable port; PS + Create), and no drawing for "other controllers"; (2) connected controllers are
  selectable: Bluetooth ones can be **turned off** (disconnected, they stay known) or
  **forgotten**; wired and adapter ones say how to remove them; (3) Display: **brightness** slider,
  **shown only on screens that allow it** (owner, 2026-10-09) — to build: laptop backlight through
  logind, monitors through DDC/CI (`ddcutil`, a new dependency to check and credit), TVs usually
  not; (4) Language: the
  **keyboard layout** is chosen separately (default "same as the language"); owneetd has US and
  Italian tables today, more layouts need their tables (2.4); (5) the **right stick scrolls the
  page** and the content of windows such as Credits and licences.
- **Part 1 (2026-10-09):** the Settings section as in the demo (list of sections and panel, B
  back to the list, right stick scrolls the panel) with **Sound** (output picker, volume, mute
  through owneetd; interface sounds on/off and volume, used by 3.12), **Appearance** (moved from
  the temporary window, now removed), **Language** (language; keyboard layout "same as the
  language" or one of owneetd's layouts, sent to owneetd for the on-screen keyboard), **Storage**
  (disks and free space) and **System** (version, updates in 7.1, Sleep / Restart / Shut down
  through owneetd with confirmation, **Credits and licences**: CREDITS.md, then every installed
  package with its licence from pacman's database, `owneet::SystemInfo`). Shared parts: up / down
  go to the nearest row first (`Nav`), `SettingSlider`, `InfoRow`, `NavArea.scrollTarget` (the
  right stick scrolls the page, also in windows). Found and fixed: request bodies sent from QML
  reached owneetd empty (a JavaScript object arrives as a QJSValue) — new unit test `test_Daemon`.
  Checked with `tools/frontend-preview` (`settings.txt`) and in the test VM with owneetd and the
  virtual sound cards (volume 40 → 50, output switched, keyboard layout it/us). A keyboard plugged
  in still types with the session's layout: following the setting there needs the compositor's
  keyboard configuration (part 3). **Next:** Network, Controllers and Bluetooth (part 2), Display
  (part 3).
- **Part 2 (2026-10-10):** **Network** (first section): offline notice (crossed icon), Wi-Fi
  switch (with a note when a hardware switch turns it off), cable status, networks nearby
  (connected first, then by signal; Connected / Saved badges, lock or "Open network"), "Search
  again" (owneetd scan), password window with "Connecting…", wrong / too short password shown in
  the window, other failures as a message; a saved network connects without asking its password;
  A on the connected network or Menu on a saved one: Disconnect / Forget (Cancel first).
  Enterprise and WEP networks say they are not supported yet. **Until the on-screen keyboard
  (3.10) the password is typed with a keyboard** (the field says so). **Controllers and
  Bluetooth:** connected controllers with connection and battery; A or Menu: Bluetooth ones
  **Turn off** (disconnect) / **Forget**, cable and adapter ones say how to remove them; **"Pair
  a new controller"** window with the drawn outlines (`PadDrawing`, pulsing marks) and per-brand
  instructions, owneetd's auto-pair for two minutes (also with a controller connected), "Pairing
  …" / failure / "No controller found" with "Search again", closes with a toast when one pairs
  and turns auto-pair off again; known devices (paired, not a connected controller) with Forget;
  "No Bluetooth on this console" without an adapter. Rows from owneetd keep the selection when
  their lists change. Found and fixed: in Settings, A ran a row's action twice (a switch went on
  and straight off again; part 1 was affected). New `tools/preview-steps/fake-owneetd.py`
  (steps files starting with `@owneetd`) and the `type` step: `settings-network.txt` covers the
  panels and windows with invented networks and devices. Checked in the test VM with the real
  owneetd (cable connected, no Wi-Fi, no Bluetooth adapter, test pad listed as "Cable").
  owneet-frontend 0.9.0. Real Wi-Fi and Bluetooth pairing go in the next hardware batch.
- **Part 3 (2026-10-10):** **Display** (after Sound): the screen used by the console, chosen
  among all connected screens (the others are turned off, decision 2026-10-10; with a game or app
  open: "close it first"); brightness only where the screen allows it (laptop backlight through
  logind, monitors through DDC/CI with `ddcutil`); resolution and refresh rate from the screen's
  own modes ("Automatic (recommended)" first; a laptop's built-in screen keeps its native mode);
  every change asks **"Keep this?"** and goes back after 15 s (B also goes back); the reduced
  (cage) session says these settings need the main mode. **Language → Keyboard layout** now also
  sets physical keyboards (gamescope at once, cage at the next start). owneetd 0.10.0:
  `internal/display`, `/v1/display` API and events, `owneet-screens-off@CARD.service` with its
  polkit rule ([[owneetd-design]]); owneet-session 0.0.13 reads `display.conf`; new
  dependencies `ddcutil` and `hwdata` (credited; ISO 1749 MiB, +29 MiB). Found and fixed:
  gamescope's main process is called `gamescope-wl` (found by its program instead); a QML `Timer`
  follows the frames drawn, not the clock (the countdown runs from the clock). Checked with
  `tools/frontend-preview` (`settings-display.txt`, pretend screens and modes) and in the test VM
  (see [[owneetd-design]]). **To check on hardware:** modes and "Keep this?" on a TV, moving between
  two screens and two graphics cards (owner's desktop), brightness on a monitor with DDC/CI
  (NVIDIA cards may need ddcutil's `nvidia-i2c.conf`) and on a laptop.
- **Hardware test 1 (2026-10-10, NiPoGi):** held-button timing, Sound and Appearance, Wi-Fi
  (wrong and right password, forget, reconnect, disconnect), controllers (Xbox by cable, Pro
  Controller paired from Settings, turned off, forgotten), resolution with "Keep this?" (expired
  and kept): all working. Changed after it: **Mute first**, hiding the other sound settings while
  on; **"Show password"** switch in the password window (the keyboard layout could not be checked
  with hidden characters). Still to check: physical keyboard layout, the owner's desktop (two
  screens on two graphics cards, DDC/CI brightness).
- **Hardware test 2 (2026-10-10, owner's desktop: RTX 4060 and a second graphics card, two
  monitors):** mute, show password, physical keyboard layout: working. **Failed:** the second
  monitor kept the boot splash; moving to the other monitor turned both off for good (forced
  power-off); no brightness on either PC. No logs (live system, forced power-off). Found in the
  code and fixed: the screen in use was guessed as "the first one on", but a frozen splash counts
  as "on" too: owneetd now reads the card gamescope holds open (`/proc/PID/fd`), keeps that one
  and marks its lit screen as the one in use; `owneet-screens-off` retries busy cards for a
  minute; a move to another screen is a trial: `owneet-session` goes back to the previous
  `display.conf` if gamescope does not start there, owneetd kills a gamescope that does not stop
  and goes back after the countdown even when gamescope is gone; ddcutil runs only once the
  compositor holds its card (opening a card first could keep the compositor from taking it), and
  owneetd logs what it says. New tester tool **`owneet-testlog`**: with a USB stick labelled
  OWNEETLOG (FAT32 or exFAT) plugged in, the whole system log and a display report (every 30 s)
  are written there as the system runs. owneetd 0.10.1, owneet-session 0.0.14, owneet-base 0.0.17.
- **Hardware test 3 (2026-10-10, desktop: Intel UHD 770 `card1` with an ASUS VK192 1440 × 900 on
  HDMI, RTX 4060 `card2` with an HP 24o; logs from `owneet-testlog`):** the second monitor now
  turns off; moving to the other monitor came back by itself after the countdown, but the
  Intel monitor stayed black. From the log: gamescope opened the Intel card and set 1440 × 900,
  then `drmModeAddFB2WithModifiers failed: Invalid argument` — Intel's compressed (CCS) buffers
  need a width that is a multiple of 128 pixels on these GPUs. Fixed: gamescope runs with
  `INTEL_DEBUG=noccs` (compositor and interface only). Also from the log: the helper started
  again between "go back" and the new gamescope, holding the NVIDIA card and making that start
  fail once (owneetd now waits for the new session); neither monitor answers DDC/CI (the ASUS
  from 2008 has none; on NVIDIA DDC/CI needs the driver's software I2C: `owneet-nvidia-i2c.conf`,
  ddcutil's recommended setting). **Intel iGPUs had never been tested before:** to cover in 7.4.
  owneetd 0.10.2, owneet-session 0.0.15, owneet-base 0.0.18, owneet-hardware 0.0.3.
- **Hardware test 4 (2026-10-10, desktop):** HP → ASUS (Intel) works with `noccs`. ASUS → HP: the
  console was up on the HP after 2-3 s, but the HP never showed a picture before the 15 s ran out
  (a monitor coming out of standby can take long). Decided with the owner: **30 s** for a move to
  another screen, counted once the console is up there, and a warning window before moving.
  Fixed: at the interface's start, the first selection on the home screen could take the focus
  from an already open "Keep this?" window. No brightness: neither monitor answers DDC/CI (the
  HP 24o has no on-screen menu at all). The Pro Controller did not pair this time (pairing
  "Authentication Timeout", then "page timeout": on the controller's side; the Bluetooth and
  controller code has not changed in 3.9). owneetd 0.10.3, owneet-frontend 0.10.1, owneet-base
  0.0.19 (DPMS state in the test report).
- **Hardware test 5 (2026-10-10, desktop):** moving between the two monitors works both ways,
  the Pro Controller pairs again. Owner's notes, done: after a move (and after going back) the
  interface opens again on Settings → Display instead of the home screen; the "Keep this?"
  window has a fixed width (the countdown no longer resizes it). Found and fixed meanwhile: a
  window opened right at the interface's start had no selected button (its buttons are created a
  moment later), so A did nothing there. owneet-frontend 0.10.2.
