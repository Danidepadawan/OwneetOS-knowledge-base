---
type: known-solution
description: "A window meant as a gamescope external overlay is treated as an ordinary window (not drawn over the app), or its picture stays on screen after it is hidden. Seen on real hardware only, not in the VM."
status: solved
seen: 2026-10-17
updated: 2026-10-17
tags: [known-solution, gamescope, frontend, x11]
---
# gamescope overlay window not drawn, or left on screen

## Symptom

- The console's keyboard over a web page (part 6 of [[step-5.2-extension-core]]) opens (its keys
  work) but is **not drawn over the app**; after Guide it shows over the home screen on a dark
  background. In the X probe the window has **no** `GAMESCOPE_EXTERNAL_OVERLAY` and is listed in
  `GAMESCOPE_FOCUSABLE_WINDOWS` as a home-screen window.
- Later, with the property in place: the keyboard is drawn over the app but **stays on screen
  after closing**, although the interface closed it (it could be opened again).
- In the test VM (headless gamescope) neither showed: only on FrankenPC (NVIDIA, gamescope 3.16.31,
  live USB).

## Cause

1. **The property never reached the window.** The interface set it on an X connection of its own
   right after `QWindow::create()`, without checking: the request most likely overtook Qt's own
   request that creates the window and failed unseen (one Xwayland server, same window id). The
   interface's log said "set"; the server's window had nothing.
2. **The last picture stayed.** Once the overlay window was unmapped, gamescope kept its last
   frame over a page that did not change (no repaint).

## Solution

owneet-frontend 0.16.19–0.16.20 (`platform/GamescopeTag_x11.cpp`, `owneet/Overlay.cpp`):

- The property is set only once the X server knows the window (asked with
  `xcb_get_window_attributes`), every request is checked (`xcb_*_checked` + `xcb_request_check`),
  the value is read back and logged, and it is set again 0.3 s and 1.5 s after the window is
  shown: gamescope reads every change of the property.
- Hiding: the window first turns fully transparent (`QWindow::setOpacity(0)`, i.e.
  `_NET_WM_WINDOW_OPACITY` 0: gamescope repaints on an overlay's opacity change and does not draw it
  at 0), and is unmapped 150 ms later. Showing sets the opacity back to 1 first.
- Verified on FrankenPC, 2026-10-17: the keyboard appears over YouTube, typing reaches the page, B
  and Done close it and it disappears.

## How we found it

With a single USB stick and no shell on the test PC:

1. **Logs on the OwneetOS stick itself** (`owneet-testlog`, [[step-5.2-extension-core]]): without
   an OWNEETLOG stick the live system writes to the stick's FAT partition `ARCHISO_EFI`, read
   afterwards on the developer's PC (`udisksctl mount -b /dev/sdX2`).
2. **The X probe every 10 s** (`owneet-xprobe`, installed with owneetd): the window's properties,
   `GAMESCOPE_FOCUSED_WINDOW` and `GAMESCOPE_FOCUSABLE_WINDOWS`. Comparing the window's properties
   with what the interface logged showed cause 1.
3. **Read-back logging** in the interface ("set / NOT set", X error codes), and the gamepad's keys
   and the window's showing and hiding logged: the keys reached the keyboard and it was closed,
   while its picture stayed (cause 2).
4. Facts about gamescope came from its source, `src/steamcompmgr.cpp` (external overlays: never
   focused, drawn above the app, forced to app id 0, opacity from `_NET_WM_WINDOW_OPACITY`, repaint
   on an opacity change).

## Watch out

- **A VM test does not prove what gamescope draws**: headless gamescope has no picture. Check the
  properties on the real server (the probe), not the interface's own log.
- Never set an X property from a second connection without checking it and reading it back.
- Anything drawn as an overlay must be hidden through opacity 0 first, or its last frame can stay.
