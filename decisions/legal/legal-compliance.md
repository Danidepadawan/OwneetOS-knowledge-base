---
type: decision
description: "GPL source archives, licence notices, never-redistributed components, trademarks, credits, asset licences, privacy."
area: legal
status: active
decided: 2026-10-07
updated: 2026-10-18
legacy: "PROJECT_RULES.md §12"
tags: [decision, legal]
---
# Legal compliance

These rules are not legal advice. Before the first public release meant for end users (v1.0), the
project is reviewed by someone experienced in open-source licensing ([[step-7.5-legal-review-before-the-public-launch]]).

- **Source code for distributed binaries (GPL and similar licences).** Whoever distributes compiled
  GPL software (kernel, xone, many Arch packages, OwneetOS's own packages) must provide the
  corresponding source code. Every published ISO and package repository comes with a **source
  archive** (PKGBUILDs and the exact sources of every package it contains) or a valid written
  offer. Until the release pipeline does this (roadmap step 7.2), **CI does not publish
  downloadable ISOs or packages**: ISOs built in CI are checks only; test ISOs are built locally.
- **Licence notices:** every package keeps its licence files (`/usr/share/licenses`); the ISO and
  the UI ("About → Licences", later) list the licences of what OwneetOS ships.
- **Proprietary but redistributable components** (NVIDIA driver, device firmware, CPU microcode)
  are shipped only as their licences allow, unmodified, with their licence texts.
- **Never redistributed:** Widevine, the Xbox wireless dongle firmware, Steam's runtime, games and
  store content. They are downloaded by the user's own system, with consent where required.
- **Trademarks:** third-party names (Xbox, PlayStation, Netflix, Steam…) only to say what works
  with OwneetOS; no third-party logos; never imply endorsement. "Based on Arch Linux" is allowed;
  the Arch logo is not used. The name **OwneetOS** gets a trademark search (EUIPO, Italian
  register) before the public launch.
- **Credits:** the projects OwneetOS is built on are credited by name, author and licence in
  `CREDITS.md` (shipped in the image at `/usr/share/doc/owneetos/CREDITS.md`, shown in the UI under
  "About → Credits and licences" with the full list of installed packages). Every new third-party
  component is added there when it is introduced.
- **Licences of assets:** only free licences that allow commercial use and redistribution (e.g.
  GPL, LGPL, MIT, BSD, Apache, Zlib, OFL, CC0, CC BY, CC BY-SA). Assets under "NonCommercial" or
  "NoDerivatives" terms (e.g. CC BY-NC-SA) are never shipped.
- **Pegasus Frontend fork:** see [[frontend-fork]].
- **Third-party services:** only official clients and web apps; no circumvention of DRM or content
  protection; the Brave extension and any user-agent change are checked against each service's
  terms of service before they ship (roadmap step 5.2).
- **The extension against the terms (checked 2026-10-18, owner):** it only moves a selection ring,
  clicks, scrolls and types in answer to the user's buttons; it changes no content, scrapes
  nothing, blocks no ads and changes no user agent. Its scripts are content scripts loaded by
  Brave from the extension's folder and run in Chromium's isolated world (nothing goes into the
  site's code); the one thing added to the page is the ring, an `<owneet-ring>` element with a
  closed shadow root.
  - **Netflix** (Terms of Use §1.8): (vi) "insert any code or product or manipulate the content of
    the Netflix service in any way" is the clause at risk (the ring element); (iv) "robot, spider,
    scraper or other automated means" does not fit (every action follows the user's input).
    **Goes to the legal review** ([[step-7.5-legal-review-before-the-public-launch]]); if needed
    the ring can leave the page (drawn by the console in its gamescope overlay).
  - **YouTube** (Terms of Service, access rights and restrictions): no altering or modifying the
    Service, no circumventing or interfering, no automated means. The extension alters nothing of
    YouTube's; the TV interface (`youtube.com/tv`) and any TV user agent are checked in
    [[step-5.3-youtube]].
  - **Spotify** (Terms of Use §3, User Guidelines): no bot, script or automated process (about
    inflating plays), no modifying or altering the Services, no ad blocking. Nothing applies.
- **Local data first:** game metadata comes from local files; no scraping or undocumented store
  APIs (Pegasus's Steam store, GOG API and Play Store downloads are disabled).
- **Privacy:** no telemetry. Any collection of personal data (e.g. opt-in crash reports) needs
  explicit consent and a privacy notice compliant with the GDPR.

Guard: [[legal]]. Practice: [[dependencies]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-07 | Legal compliance rules adopted ([[legal-compliance]]). CI stops publishing the ISO as a download until releases ship a GPL source archive (option A). |
| 2026-10-08 | Legal check before phase 3: the frontend fork is named `owneet-frontend` (Pegasus's trademark terms); Pegasus's CC BY-NC-SA theme, logo, Roboto fonts and button images are not used; its online metadata downloads are disabled. `CREDITS.md` credits every project OwneetOS builds on and ships in the image ([[legal-compliance]]). Step 2.9 approved. |
| 2026-10-18 | The Brave extension checked against the terms of Netflix, YouTube and Spotify: an input method acting only on the user's buttons, content scripts in Chromium's isolated world, one ring element in a closed shadow root. Netflix §1.8(vi) ("insert any code or product…") goes to the legal review of step 7.5; the YouTube TV interface and user agent are checked in step 5.3. |
