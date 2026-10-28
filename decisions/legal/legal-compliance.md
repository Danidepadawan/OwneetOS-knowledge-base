---
type: decision
description: "GPL source archives, licence notices, never-redistributed components, trademarks (third parties'; ours not registered), credits, asset licences, privacy."
area: legal
status: active
decided: 2026-10-07
updated: 2026-10-28
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
  - **How (owner, 2026-10-28, option a of [[step-7.2-release-pipeline]]):** a full archive, never
    only a written offer. OwneetOS's own packages: their PKGBUILDs and exact sources, in the
    release's folder on SourceForge. Arch's packages: the exact `.src.tar.gz` of every package
    version shipped, taken from `sources.archlinux.org` and **copied to SourceForge** (a `sources/`
    folder shared by every release, so each release uploads only new versions): the obligation is
    ours, and stays met even if Arch removes them. A release missing any source publishes nothing.
- **Licence notices:** every package keeps its licence files (`/usr/share/licenses`); the ISO and
  the UI ("About → Licences", later) list the licences of what OwneetOS ships.
- **Proprietary but redistributable components** (NVIDIA driver, device firmware, CPU microcode)
  are shipped only as their licences allow, unmodified, with their licence texts.
- **Never redistributed:** Widevine, the Xbox wireless dongle firmware, Steam's runtime, games and
  store content. They are downloaded by the user's own system, with consent where required.
- **Trademarks:** third-party names (Xbox, PlayStation, Netflix, Steam…) only to say what works
  with OwneetOS; no third-party logos; never imply endorsement. "Based on Arch Linux" is allowed;
  the Arch logo is not used. The name **OwneetOS** is **not registered as a trademark** (the
  authors, 2026-10-25: it costs too much for what it gives); a preliminary search (step 7.5,
  2026-10-24) found no conflicting mark, so the name is used legally. What carries the project's
  name or logo never imitates someone else's mark, logo or product shape.
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
| 2026-10-25 | The OwneetOS trademark is not registered (the authors: too costly for its worth). The preliminary search of 2026-10-24 found no conflicting mark; the project only makes sure everything it does is legal. |
| 2026-10-28 | Source archive (step 7.2, option a): our packages' PKGBUILDs and sources per release; every Arch package's exact `.src.tar.gz` copied from `sources.archlinux.org` to a shared `sources/` folder on SourceForge; a release missing any source publishes nothing. |
