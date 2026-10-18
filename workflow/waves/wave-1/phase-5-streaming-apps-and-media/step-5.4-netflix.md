---
type: step
description: "Widevine verified, browse / play / pause / seek on the gamepad."
phase: "[[phase-5-streaming-apps-and-media]]"
step: "5.4"
status: todo
legacy: "ROADMAP.md 5.4"
tags: [step, phase-5]
---
# 5.4 Netflix

Up: [[phase-5-streaming-apps-and-media]] · Status: **todo**

- **Deliverables:** Widevine verified, browse / play / pause / seek on the gamepad.
- **To do here (owner, 2026-10-19, from [[step-5.3-youtube]]):** the **console's consent to
  Google's Widevine terms**, replacing 5.1's silent opt-in ([[legal-compliance]]): asked once when
  the user installs the first web app ([Read] [Continue]), and **again at every new Widevine
  version** (owneetd compares the version in each web app's profile, `WidevineCdm/<version>`, with
  the one the user agreed to). New console UI: **demo first** ([[demo-before-code]]). Also: a
  freshly downloaded Widevine works only after Brave restarts (Linux), so the first protected
  video of a new profile may fail until the web app is opened again: to be solved here. Brave's own
  question ("Restart browser to enable Google Widevine") is already turned off by owneetd (5.3).
