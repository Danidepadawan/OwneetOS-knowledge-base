---
type: step
description: "Widevine verified, browse / play / pause / seek on the gamepad."
phase: "[[phase-5-streaming-apps-and-media]]"
step: "5.4"
status: in-progress
legacy: "ROADMAP.md 5.4"
tags: [step, phase-5]
---
# 5.4 Netflix

Up: [[phase-5-streaming-apps-and-media]] · Status: **in progress**

- **Deliverables:** Widevine verified, browse / play / pause / seek on the gamepad.
- **To do here (owner, 2026-10-19, from [[step-5.3-youtube]]):** the **console's consent to
  Google's Widevine terms**, replacing 5.1's silent opt-in ([[legal-compliance]]): asked once when
  the user installs the first web app ([Read] [Continue]), and **again at every new Widevine
  version** (owneetd compares the version in each web app's profile, `WidevineCdm/<version>`, with
  the one the user agreed to). New console UI: **demo first** ([[demo-before-code]]). Also: a
  freshly downloaded Widevine works only after Brave restarts (Linux), so the first protected
  video of a new profile may fail until the web app is opened again: to be solved here. Brave's own
  question ("Restart browser to enable Google Widevine") is already turned off by owneetd (5.3).
- **Next hardware test** (owner, 2026-10-19): on FrankenPC after this step is closed at the
  earliest, with the open hardware checks of [[step-5.1-brave-in-the-os]],
  [[step-5.2-extension-core]] and [[step-5.3-youtube]].
- **No TV interface for Netflix (2026-10-19, checked from the developer's PC with `curl`):**
  `netflix.com/tv` is a 404 and a TV user agent gets the same redirects as a desktop browser;
  Netflix's TV app runs on Netflix's own platform, not as a web page. The desktop site stays.
- **Agreed (owner, 2026-10-19):**
  - **The ring of 5.2 for browsing**, profiles and signing in. **In the player** the D-pad / stick
    keep moving the ring through Netflix's control bar (settings, subtitles…), and **LT / RT seek
    by 10 s**, sent as Netflix's own seeking keys (to be checked with a probe, then written into
    [[controller-input-map]] before any code).
  - **The Widevine consent first**, so that every later Netflix test goes through it live.
- **Sub-steps** (one per prompt, each tested by the owner):
  1. **Widevine consent: facts, then the demo** (`design/demos/5.4-widevine-consent.html`): the
     terms that come with Widevine; the consent in a web app's install confirmation, on the
     pattern of the games' licences ("By installing you accept …" [Read] [Install]); asked again
     at a new Widevine version; how [Read] shows the terms; what declining does. No code before
     the owner approves the demo.
  2. **Widevine consent: code** (owneetd: the consent and the version agreed to, `widevine_opted_in`
     set before every opening from it, the installed version read from the profiles, an endpoint;
     the interface: the approved dialog).
  3. **The first-session restart:** checked in the test VM, then fixed with the owner (likely one
     Widevine folder kept by owneetd for every profile).
  4. **Netflix's controls: a probe in the test VM**, then the "Inside Netflix" bindings (vault
     only): the seeking keys, the ring on the control bar, the cookie banner (a known limit of
     5.2), the profile picker, signing in, Widevine playback.
  5. **Netflix's controls: code** (`extension/content/netflix.js`: LT / RT in the player).
  6. **Close:** terms of service (Netflix §1.8(vi) stays with 7.5), known limits, outcome.
