---
type: known-solution
description: "The test VM's screenshots stay 640×480 (or the old size) after enlarging QEMU's window; web pages look cramped: the console's screen takes its size only when cage starts."
status: solved
seen: 2026-10-26
updated: 2026-10-31
tags: [known-solution, vm, test]
---
# The test VM's screen stays small

## Symptom

- `vm/test.sh screenshot` gives **640×480** (or 806×556, the window's old size) although QEMU's
  window was made larger; the home screen and web pages look cramped.
- Web apps lay out as on a small screen: Spotify folds its own sidebars, Brave's zoom for Spotify
  stays at 100 % (it never goes below), the navigation is hard to judge.

## Cause

QEMU offers the VM its window's size as the preferred screen size, but **cage (the console's
compositor in the VM) takes that size only when it starts**. Enlarging the window later changes
the size on offer, not the running screen. QEMU's own zoom scales the picture without changing the
size at all. After every VM start the window is small again.

## Solution

1. QEMU's window in **full screen** (Ctrl+Alt+F, or *View → Fullscreen*).
2. With the window still full screen, restart cage (the session loop starts it again within a
   second):
   ```sh
   vm/test.sh run 'head -1 /sys/class/drm/card*-Virtual-*/modes; pkill -x cage; sleep 6; pgrep -x cage >/dev/null && echo restarted' 30
   ```
   The first line is the size on offer (the window's); the next screenshot has it.

## How we found it

1. `head -3 /sys/class/drm/card*-Virtual-*/modes` printed the size on offer first: it followed the
   window (640×480, then 939×578, then 806×556), so QEMU passes the size.
2. The screenshot after restarting cage had that size (806×556), so cage takes it only at start.
3. In full screen the offer was the monitor's size (2327×1223 on the owner's host).

## Watch out

- Check the screenshot's size before judging a layout (`vm/test.sh screenshot`, then the PNG's
  size).
- Restarting cage closes any open app and restarts the interface: close web apps first.
- `vm/test.sh run` commands must not contain `exit` ([[vm-run-hangs-after-exit]]).
