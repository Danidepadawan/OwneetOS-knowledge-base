---
type: step
phase: "[[phase-3-frontend]]"
step: "3.10"
status: done
legacy: "ROADMAP.md 3.10"
tags: [step, phase-3]
---
# 3.10 On-screen keyboard

Up: [[phase-3-frontend]] · Status: **done**

- **Deliverables:** gamepad OSK for frontend text fields (Wi-Fi passwords, search), layouts per language.
  Until then the Wi-Fi password is typed with a keyboard (3.9, part 2).
- **Demo (2026-10-10, approved 2026-10-11 with rows and columns both wrapping around):**
  `design/demos/3.10-osk.html`. Proposals in it: the
  keyboard opens by itself under a text field (the window moves up; its buttons hide, Done does
  the same); five rows: digits with delete, letters, shift and punctuation, then page key, cursor
  left / right, space, a show / hide key in password fields, and Done; the layout follows Settings
  → Language → Keyboard layout (Italian has è ò à ù on the letters page); pages of keys: letters,
  symbols, accented letters of other languages; shift once = next letter, twice = caps lock; the
  selection wraps around at every edge (left / right and up / down). **Buttons, as on Xbox and PlayStation keyboards (changes to [[controller-input-map]]
  inside the keyboard, approved):** A types the key, X deletes, Y types a space, LT / RT
  change the page of keys, Menu = Done, B closes the keyboard (B again closes the window). A
  keyboard plugged in keeps working at the same time. Every key plays the "click" ([[interface-sounds-spec]]).
- **Outcome (2026-10-11):** `foundation/Keyboard.qml`, as in the demo, types into any TextInput of
  the interface; used by the Wi-Fi password window, where it opens by itself (also after a wrong
  password) and A on the field opens it again; the window moves up and its buttons and prompts
  make room; Done connects. The layout follows Settings → Language → Keyboard layout (English US,
  Italian); a keyboard plugged in types, deletes and confirms (Enter) while it is open. Checked
  with `tools/frontend-preview` (`osk.txt`: typing, delete, space, pages, wrap-around, show /
  hide, physical keyboard, Done → connected; `settings-network.txt`). Apps (Brave) get their
  keyboard later, through owneetd's virtual keyboard (2.4) and the extension (5.2).
  owneet-frontend 0.11.0.
