---
type: decision
description: "Approved look: deep navy and coral, Bricolage Grotesque + Lexend, about twenty palettes, provisional wordmark."
area: ux
status: active
decided: 2026-10-03
updated: 2026-10-15
legacy: "PROJECT_RULES.md §9"
tags: [decision, ux, design]
---
# Design direction, palettes, wordmark

- **Original** design: minimal, clean, modern.
- **Approved direction (2026-10-03):** `design/mockups/wave1-mockups.html` — deep navy ground,
  coral accent, minimal UI, **Bricolage Grotesque** (titles) + **Lexend** (UI text), 1280×720
  design grid, 5% horizontal TV safe area. Palettes are **provisional** and may change.
- **User-customizable color palette**, implemented with design tokens (colors, radii, spacing).
- **Palettes (2026-10-08, demo 3.3):** about twenty, chosen in a picker window with live preview
  (Settings → Appearance shows only the current one): dark (Dusk, Tide in vivid "minty" cyan,
  Bloom, Ember, Espresso, Harbor navy/beige, Forest, Lagoon, Amethyst, Crimson, Synthwave, Amber,
  Olive, Graphite), light (Daylight, Arctic, Sand, Latte, Sakura), accessibility (high contrast
  dark and light). Every palette passes a contrast check ([[design-tokens]]).
- Baseline accessibility: high contrast, text scaling, color-blind-safe palettes.
- Open-source fonts only.
- **Wordmark (provisional, the final logo comes before the public launch, roadmap 7.6):** "Owneet"
  + "OS", Bricolage Grotesque 750 / width 80; in the interface "Owneet" in the text colour and "OS"
  in the accent; the boot splash's copy is all white on black (2026-10-15, [[boot-experience]]),
  generated as outlines by `tools/branding/make-wordmark` (`packages/owneet-branding/owneetos-wordmark.svg`).
- Button prompts: Xbox, PlayStation and Nintendo-style glyph sets, drawn for OwneetOS (no
  third-party logos), chosen automatically from the connected controller.

Practices: [[design-tokens]], [[ui-patterns]]. Approval process: [[demo-before-code]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-03 | Mockup direction approved; palettes provisional ([[design-direction]]). |
| 2026-10-05 | Boot splash approved by the owner with the wordmark "Owneet" + coral "OS" (as in the mockups page header) instead of "owneet." ([[design-direction]]). |
| 2026-10-15 | The boot splash is neutral (white on black) for every palette; the start-up animation brings the palette's colours ([[boot-experience]]). |
| 2026-10-08 | Demo 3.3 feedback: wordmark/logo provisional (final logo before the launch, roadmap 7.6); about twenty palettes (Tide in vivid "minty" cyan; new Ember, Espresso, Harbor and more) in a picker with live preview; language chosen from a list; the Guide prompt reads "Home" ([[design-direction]]). |
| 2026-10-08 | Step 3.3 approved. Button prompts also have a Nintendo-style set (chosen automatically for Switch controllers). Small hardware checks are batched with the next larger test instead of a new USB stick each. |
