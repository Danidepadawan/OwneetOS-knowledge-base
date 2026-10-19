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
- **Sub-step 1, the facts (2026-10-19, test VM):**
  - Widevine comes per profile as `WidevineCdm/4.10.3112.0/` (`manifest.json`, `LICENSE`, the
    library under `_platform_specific/linux_x64`) and `latest-component-updated-widevine-cdm`
    (`{"Path": …}`): owneetd can read the installed version there.
  - Its **`LICENSE`** says, in full: Google owns the content decryption module and its
    documentation; "You may not use, modify, sell, or otherwise distribute the Software without a
    separate license agreement with Google. The Software is not open source software. If you are
    interested in licensing the Software, please contact www.widevine.com".
  - Brave's program links **no terms**: only its help page "How do I view DRM protected
    content?", which says that turning Widevine on means agreeing to **Google's Terms of Use** and
    accepting that Brave is not liable for Widevine; Widevine is off by default in Brave.
- **Demo** `design/demos/5.4-widevine-consent.html` (2026-10-19), built on the approved demo 5.0.0,
  **waiting for the owner's approval**: the consent in the install confirmation of the first web
  app (a fact "Protected videos: Google Widevine, downloaded from Google" and "By installing, you
  accept Google's terms of use for Widevine", with *Read the terms*; later installs do not ask);
  the terms window (what Widevine is, "OwneetOS is not responsible for Widevine", the address
  `policies.google.com/terms`, a QR code as a variant: V); asked again at opening after a Widevine
  update, and on a console installed before 5.4 (*Accept and open*, *Read the terms*, *Not now*:
  the web app does not open). The wording of the consent goes to the legal review.
