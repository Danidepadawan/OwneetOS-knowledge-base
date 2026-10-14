---
type: best-practice
description: "QML conventions for the OwneetOS theme: foundation components, Nav/NavArea input, Tr, Theme, clock-based timers, file names."
scope: language
language: qml
tags: [best-practice, qml, frontend]
---
# QML (OwneetOS theme)

- The theme lives in `frontend/owneet-frontend/src/themes/owneet/`; shared building blocks in
  `foundation/` (`Theme`, `Nav`, `NavArea`, `Tr`, `Sheet`, `Dialog`…). Screens use them instead of
  re-implementing them.
- **Input:** never read keys directly; use `Nav.action(event)` and `NavArea` (spatial navigation,
  A / B, groups with memory). New bindings first go into the [[controller-input-map]].
- **Feedback and sounds:** report what happened with `Nav.feedback(kind)`; `UiSounds` plays it.
- **Text** only through `Tr` ([[ui-text-and-i18n]]); **colours and sizes** only through `Theme`
  ([[design-tokens]]).
- A QML `Timer` follows the frames drawn, not the clock: countdowns and timeouts compute from the
  clock (`Date.now()`).
- Request bodies to owneetd are plain JSON-able objects (a JavaScript object reaching C++ arrives as
  a `QJSValue`: covered by `test_Daemon`).
- Pegasus's `api.keys` names are kept but mapped to the OwneetOS meanings
  ([[frontend-input]]).
- File names: `PascalCase.qml` for components; pages end in `Page`, windows in `Sheet`.
- Property names never start with `on` + a capital letter (`onRunning`): QML reads them as signal
  handlers and the theme fails to load (step 5.1, 2026-10-15). Use another name (`runningInk`).
