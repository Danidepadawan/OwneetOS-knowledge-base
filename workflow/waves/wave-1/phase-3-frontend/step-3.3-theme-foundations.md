---
type: step
phase: "[[phase-3-frontend]]"
step: "3.3"
status: done
legacy: "ROADMAP.md 3.3"
tags: [step, phase-3]
---
# 3.3 Theme foundations

Up: [[phase-3-frontend]] · Status: **done**

- **Deliverables:** design tokens (palettes from [[design-direction]]), bundled fonts, 1280×720 scaling grid,
  safe area, focus ring, prompt bar with Xbox / PlayStation glyph sets.
- **Demo:** `design/demos/3.3-theme-foundations.html`, approved on 2026-10-08 after one review
  (the "Foundations" tab exists only in the demo; 21 palettes in a picker with live preview, Tide
  made vivid "minty" cyan, Ember, Espresso, Harbor and others added; language chosen from a list;
  Guide prompt "Home"; text sizes S/M/L/XL = 90/100/120/140 %, text only, columns scroll while the
  prompt bar and safe area never move; glyphs drawn for OwneetOS, no third-party logos, chosen
  automatically from the connected controller).
- **Outcome:** theme `owneet` (built-in default, replaces `owneet-minimal`) with its foundations
  in `src/themes/owneet/foundation/` ([[frontend-changes]]): `Theme` tokens and
  the 21 palettes, focus ring with lift, glyphs and prompt bar, picker window, settings rows.
  Bricolage Grotesque and Lexend bundled as static instances (`tools/branding/make-fonts`, OFL-1.1
  licence texts installed); Pegasus's Roboto fonts and button images removed. Until the home
  screen (3.6) the theme shows a plain game list; **Y opens a temporary Appearance window**
  (palette, text size, button prompts, reduce motion, TV safe area outline), saved in the theme's
  memory, which moves to Settings in 3.9. Language choice comes with 3.4. Checked in the builder VM
  (frontend under Xvfb, screenshots of every option) and in the test VM (choice kept when the
  frontend restarts). Owner test (2026-10-08): everything shown correctly, picker and options work;
  the choice is lost on reboot because the live USB has no persistent storage (checked again on the
  installed system, phase 6). Approved by the owner on 2026-10-08, with one addition: a
  **Nintendo-style** glyph set (L/R, ZL/ZR, "+"; letters as printed, since sdl2-compat follows the
  printed labels on Nintendo pads), chosen automatically for Switch controllers. Its hardware test
  (Switch Pro Controller) is deferred to the next hardware test, together with other checks.
