---
type: step
description: "The project's website (Angular, static on GitHub Pages, English and Italian, no data collected): demo of the pages first, then the code in its own repository."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.8"
status: in-progress
tags: [step, phase-7]
---
# 7.8 Website *(added 2026-10-20)*

Up: [[phase-7-updates-and-first-release]] · Status: **in-progress**

- **Deliverables:** the website of [[website]]: home, features, system requirements, download
  (a redirect to SourceForge, "coming soon" until releases are published), installation guide,
  FAQ, credits and licences, privacy, contributing and translating; English and Italian; built
  with Angular in `OwneetOS-website/`, prerendered, ready for GitHub Pages and the project's
  domain.
- **Done when:** the owner approved the demo of the pages, the site builds to static files in its
  own repository, works with the keyboard, the mouse and on a phone, and the owner approved it.
- **Started (owner, 2026-10-20)** while phase 5 is with Danidepadawan, before the release.
  Proposal agreed ([[website]]); first the home page's demo.
- **Home demo, first round (2026-10-20):** `design/demos/7.8-website-home.html`. The owner's
  feedback: one page with snapping sections and the address following them (snapping approved);
  too much text, not always right; the features in a carousel; the console picture to follow the
  real home screen with generic apps (Video streaming, Audio streaming, Local videos, Local music,
  Local pictures, All apps). Second round: the texts cut to a title and a short line each and
  corrected (English and Italian only, offline only for DRM-free games, the trademarks of the
  names used), the hidden notice no longer peeking at the bottom. The carousel's side cards
  were tried fading out, then blurred; the owner chose one card at a time with arrows and dots,
  the cards half a screen apart, then autoplay and a loop (checked in Chromium: one card every
  5 s, after the ninth the first again, going on forward); the pause button was removed: it
  stops only while pointed at. The home's opening line became "Plug it. Play it. It's yours!" (owner;
  Italian "Collegalo. Giocaci. È tuo!", confirmed). Third round of texts (owner): "You only need
  a controller"; "Supporting Steam and DRM-free games"; the "Steam built in" card removed (Steam
  will be optional, [[step-5.0-optional-apps]]); "Stream them or play your own"; "21 palettes,
  multiple languages supported" (the owner expects French and Spanish reviews before the
  release, maybe German: [[languages]] still lists Italian and English for Wave 1); "Runs on
  low-end PCs". "Credits" added to the header; below 1100 px the header shows the Menu button.
  Then: the opening line "Plug it. Play it. Own it!" (Italian "Collegalo. Giocaci. Fallo tuo!",
  to be confirmed); Guide and FAQ leave the header for a new "Info" section of the home ("Need
  help?", two cards leading to the guide and the FAQ). The hand-drawn icons replaced by Lucide's
  ([[website]]). The console picture waits for Danidepadawan's changes to the home screen.
