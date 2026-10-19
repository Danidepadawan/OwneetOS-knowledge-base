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
  Google's Widevine terms**, replacing 5.1's silent opt-in ([[legal-compliance]]): asked once
  (at the first opening of a web app, per user: see the owner's review below), and **again at every
  new Widevine version** (owneetd compares the version in each web app's profile, `WidevineCdm/<version>`, with
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
- **First version of the demo** (2026-10-19), built on the approved demo 5.0.0: the consent in the install confirmation of the first web
  app (a fact "Protected videos: Google Widevine, downloaded from Google" and "By installing, you
  accept Google's terms of use for Widevine", with *Read the terms*; later installs do not ask);
  the terms window (what Widevine is, "OwneetOS is not responsible for Widevine", the address
  `policies.google.com/terms`, a QR code as a variant: V); asked again at opening after a Widevine
  update, and on a console installed before 5.4 (*Accept and open*, *Read the terms*, *Not now*:
  the web app does not open). The wording of the consent goes to the legal review.
- **Owner's review of the demo (2026-10-19):** no QR code; **the terms shown directly**, with their
  address. Google's terms are not copied into the console (Google's text is under no free licence,
  [[legal]]; a copy goes stale) nor fetched and turned into console text (scraping): **Read the
  terms opens Google's live page** (`policies.google.com/terms`) in the web apps' full-screen
  window (right stick scrolls, B comes back to the question), and the question shows the address.
  That window comes with the first install, so **the question moves to the first opening of a web
  app** (the same window after a Widevine update and on consoles installed before 5.4: *Accept and
  open*, *Read the terms*, *Not now*); the install confirmation only says it will come. **One
  consent per user** (owner): today the console has one user, later every person on the console
  accepts for themselves. Demo `design/demos/5.4-widevine-consent.html` updated.
- **Demo approved (owner, 2026-10-19)** as it is. The legal questions it leaves stay with
  [[step-7.5-legal-review-before-the-public-launch]] (Widevine's licence and Brave's agreement with
  Google, the console's consent in place of Brave's window, the wording, a change of Google's terms
  without a new Widevine version). **Sub-step 1 is done.** Next: sub-step 2, the code.
- **Sub-step 2, implemented (2026-10-19), waiting for the owner's test:** owneetd 0.12.8
  (`internal/catalog/widevine.go`: the consent per user with its Widevine version, read from each
  profile's `WidevineCdm/latest-component-updated-widevine-cdm`; Open refused without it;
  `widevine_opted_in` set before every opening; Google's terms page as `web:widevine-terms`;
  [[owneetd-api-apps]]) and owneet-frontend 0.16.22 (`theme.qml`: the install confirmation's
  notice, the question at opening, Google's page and back to the question on B, Guide or its end;
  texts in `frontend/i18n`, English and Italian).
- **Owner's test of sub-step 2** (2026-10-19, test VM, cage): the install confirmation's notice
  overflowed its window, and after B on Google's terms page the question came back **without the
  selection** (the home page selects its hero a moment after the running app changes; the
  question had opened before the app list was refreshed): fixed in owneet-frontend 0.16.23 (the
  question opens once the list is updated; the notice sized to the window). A mouse click on the
  question then did nothing (the interface's buttons have no mouse support: fine, the console
  never needs a mouse) and the screen looked frozen; the interface's 137 % CPU was not a hang: it
  uses 189 % idle in the VM (software drawing). With 0.16.23, **with the controller, it works**:
  the question, Google's live page, B back to the question with the selection, *Accept and open*
  opens Netflix.
- **Sub-step 2 verified** (owner, 2026-10-19, test VM; owneetd 0.12.8, owneet-frontend 0.16.23):
  the consent is saved per user with the installed Widevine (`{"users": {"console": {"version":
  "4.10.3112.0", "accepted": …}}}` in `~/.local/state/owneetd/widevine.json`) and Netflix's profile
  has `widevine_opted_in` true; with an older accepted version (set by hand) opening Netflix asked
  again, and accepting recorded 4.10.3112.0 with a new date. **Sub-step 2 is done.** Next:
  sub-step 3, the first-session restart.
- **Sub-step 3, the check** (owner, 2026-10-19, test VM; a probe extension of the VM only,
  `vm/run/probe-5.4/`, asking for Widevine through the page's media keys every 5 s):
  - **A new profile cannot use Widevine in its first session:** Brave downloaded it 29 s after
    starting (4.10.3112.0), and the page still had no Widevine 110 s after loading; after
    reopening, available at once.
  - **A copy of another profile's Widevine** (with its `latest-component-updated-widevine-cdm`
    pointing into the new profile) is usable at the first start.
  - **A hidden start works:** Brave with no window (`--headless=new`, `--component-updater=fast-update`)
    in a new profile downloaded Widevine in **20 s**; the web app opened afterwards had it at once.
- **Decided (owner, 2026-10-19):** **each web app's first opening** (its profile has no Widevine)
  runs the hidden start in its own profile first, about 20 s, with no copies between profiles (to
  be refactored to "only the console's first opening, copies for the others" if testing shows the
  need); the wait **reuses the approved "Preparing…" screen** of Steam's first start, with texts
  for the web app ("the first time takes a few seconds"), so no new demo.
