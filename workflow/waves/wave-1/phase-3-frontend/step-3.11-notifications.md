---
type: step
description: "Notice area on home + transient toasts fed by daemon events."
phase: "[[phase-3-frontend]]"
step: "3.11"
status: done
legacy: "ROADMAP.md 3.11"
tags: [step, phase-3]
---
# 3.11 Notifications

Up: [[phase-3-frontend]] · Status: **done**

- **Deliverables:** notice area on home + transient toasts fed by daemon events.
- **Demo (2026-10-11, approved the same day with a sound of its own for attention notifications,
  `notify-error`):** `design/demos/3.11-notifications.html`. Proposals in
  it: **banners** at the top right, under the top bar (icon, title, one line of detail; at most
  three at a time, newest on top, gone after 5 s); two kinds: "attention" (accent border and icon,
  "notify-error" sound: battery low, controller disconnected, Wi-Fi lost, game closed unexpectedly, disk
  read only) and "info" ("notify" sound: controller connected, back online, update ready); a
  **bell** in the top bar counts the ones not seen yet; **Y on the home screen** (a page-level
  option, [[controller-input-map]]) opens the **Notifications** window: newest first, with the time and, where
  there is one, where A takes you (Controllers, Network, Play, Disks, Update); X removes one, Y
  clears all, B closes; opening it marks everything as seen. The list is kept until the console
  restarts (at most 30). **While a game is on screen nothing is drawn over it** (the overlay is
  Wave 2): notifications wait in the list and the bell counts them. Disks (6.5) and updates (7.1)
  only send theirs when those steps arrive.
- **Outcome (2026-10-11):** `foundation/Banners.qml`, `NotificationsSheet.qml` and the notification
  centre in the shell, fed by owneetd's events: controller connected (with battery), battery low
  (≤ 15 % or level low / critical, once until it charges again), controller disconnected, Wi-Fi
  lost or cable unplugged, back online (only after a "lost"), game closed unexpectedly (exit code,
  signal or crash, not when closed from the console; A plays it again). What the user just did is
  not news: no notice after turning a controller off or pairing it from Settings, after
  connecting, disconnecting or forgetting a network, or after turning Wi-Fi off. A starts the
  linked place (Settings → Controllers or Network, or the game). New sound `notify-error`
  ([[interface-sounds-spec]]: eleven sounds; a copy of `notify` until the owner's version). The banners'
  5 s run on the clock. The pretend owneetd takes events from preview steps (`event TYPE JSON`):
  `notifications.txt`. owneet-frontend 0.12.0.
