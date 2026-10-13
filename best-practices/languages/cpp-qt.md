---
type: best-practice
scope: language
language: cpp
tags: [best-practice, cpp, qt, frontend]
---
# C++ / Qt (owneet-frontend backend)

- Qt 5.15, CMake. OwneetOS's own classes live in `src/backend/owneet/`, in the `owneet` namespace
  (`owneet::Daemon`, `owneet::I18n`, `owneet::Storage`, `owneet::SystemInfo`), exposed to QML in
  lower camel case (`owneetd`, `i18n`, `storage`, `systemInfo`).
- **Small, targeted changes** to Pegasus's C++; everything the user sees is QML
  ([[frontend-changes]]).
- **Every OwneetOS change to the imported Pegasus code is its own commit**, so it can be compared
  with upstream. Upstream updates are applied one commit each, with the upstream commit id in the
  message ([[frontend-fork]]).
- `#pragma once`; `///` doc comments on public methods in headers; Qt types and containers where
  QML is involved.
- Unit tests in Pegasus's test tree (`test_I18n`, `test_Daemon`, `test_Steam`), run headless with
  `QT_QPA_PLATFORM=offscreen`.
- Unused upstream code (qmake project, other platforms) stays in the tree unless it gets in the way.
