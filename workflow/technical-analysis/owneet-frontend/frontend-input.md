---
type: technical-analysis
description: "How gamepad input reaches QML and how Pegasus keys map to the OwneetOS input map."
component: owneet-frontend
legacy: "docs/frontend-architecture.md §3 Input"
tags: [technical-analysis, frontend]
---
# owneet-frontend: input

Up: [[frontend-architecture]]

SDL2 reads the gamepads and turns buttons into key events for QML (A = accept, B = back,
X = details, Y = filters, L1/R1 = previous/next page, L2/R2 = page up/down, Start = Pegasus's main
menu). **Guide is also turned into a key** (not bound to anything by default).

OwneetOS (3.2, 3.5): Guide is removed; the keys keep Pegasus's names but follow the OwneetOS
input map ([[controller-input-map]]): `prevPage/nextPage` = LB/RB (sections),
`pageUp/pageDown` = LT/RT (filters), `filters` = Y (page option), `details` = X, `menu` = Menu;
new `scrollUp/scrollDown` = right stick (fast scrolling). The theme never reads them directly: it
uses `Nav.action(event)`.
