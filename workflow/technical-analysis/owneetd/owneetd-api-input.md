---
type: technical-analysis
description: "API for the virtual keyboard and mouse used by the on-screen keyboard; keyboard layouts."
component: owneetd
legacy: "docs/daemon-design.md §4 Virtual input (on-screen keyboard)"
tags: [technical-analysis, owneetd, api]
---
# owneetd API: Virtual input (on-screen keyboard) — implemented (2.4)

Up: [[owneetd-design]] · Conventions: [[owneetd-design#4. API v1 (draft)]]

| Method | Path | Purpose |
|---|---|---|
| POST | `/v1/input/text` | `{"text": "…"}` — typed into the focused app. If one character is not available in the keyboard layout nothing is typed: `422 input.unsupported_character` |
| POST | `/v1/input/key` | `{"key": "enter", "modifiers": ["ctrl"]}` — keys: enter, backspace, tab, escape, space, delete, home, end, up, down, left, right, pageup, pagedown; modifiers: ctrl, shift, alt, meta |
| POST | `/v1/input/pointer` | `{"dx": 10, "dy": -5, "wheel": 0}` — move the pointer / scroll |
| POST | `/v1/input/click` | `{"button": "left"}` (left, right, middle) |
| GET / PUT | `/v1/input/layout` | `{"layout": "it"}` — keyboard layout used to type text (`us`, `it`) |

A virtual keyboard sends **keys, not characters**: the character depends on the XKB layout of the
console session. `owneetd` therefore keeps its own layout tables (US and Italian for Wave 1) and
must use the same layout as the session (setting `keyboard_layout`, later driven by the language
chosen at first boot). Access to `/dev/uinput` is granted to the console session by a udev
`uaccess` rule, so owneetd stays unprivileged.
