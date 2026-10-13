---
type: best-practice
scope: project
tags: [best-practice, ux]
---
# UI patterns

Recurring interface rules, each from an approved demo or decision.

- **Pickers instead of button rows** for choices that can grow (palette, language): one compact row
  showing the current value opens a window with the full list. ([[design-direction]])
- **Overflow opens the full list:** when a list has more items than its place on screen, the last
  place opens the complete list ("All games", "All apps", the disks summary).
  ([[home-and-library]])
- **Confirmations select Cancel first** (Close game, Sleep / Restart / Shut down, Forget,
  Disconnect). ([[settings-screens]], [[quick-menu-and-startup]])
- **What the user just did is not news:** no notification after an action the user just took
  (turning a controller off, connecting a network). ([[notifications]])
- **One sound per button press**, the most specific one ([[sound-files]]).
- **Scrolling lists and grids keep room** for the focus ring and its lift at both ends.
- **Navigation groups remember** their last selection (hero, apps column, row of games).
- Windows have round buttons in a centred row, navigated left / right.
- Up / down go to the nearest row first, so a row of buttons is never skipped.
- A button with no use on a screen does nothing (and plays the "edge" sound).
- Anything time-based (countdowns, banners) runs on the clock, not on frames drawn ([[qml]]).
- Every new pattern comes from an owner-approved demo ([[demo-before-code]]).
