---
type: step
description: "Virtual keyboard and mouse devices for the system-wide on-screen keyboard and for apps that need key presses."
phase: "[[phase-2-system-daemon]]"
step: "2.4"
status: done
legacy: "ROADMAP.md 2.4"
tags: [step, phase-2]
---
# 2.4 Virtual input (uinput)

Up: [[phase-2-system-daemon]] · Status: **done**

- **Deliverables:** virtual keyboard and mouse devices for the system-wide on-screen keyboard and
  for apps that need key presses.
- **Outcome:** `internal/vinput`: virtual keyboard and mouse created at startup; text typed with
  layout tables for US and Italian (accented letters, AltGr symbols; unsupported characters
  rejected before anything is typed); special keys with modifiers; pointer move, scroll, click.
  API: `/v1/input/text`, `/key`, `/pointer`, `/click`, `/layout`. `/dev/uinput` granted to the
  console session by a udev `uaccess` rule (owneetd stays unprivileged), `uinput` loaded at boot.
  Integration test reads back the key events of the real virtual keyboard (Italian "a@" + Enter).
