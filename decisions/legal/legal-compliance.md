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
    release's folder on SourceForge. Arch's packages: the exact `.src.tar.gz` of **every** package
    version shipped, whatever its licence, **copied to SourceForge** (a `sources/` folder shared by
    every release, so each release uploads only new versions): the obligation is ours, and stays
    met even if Arch or an upstream removes them. A release missing any source publishes nothing.
  - **Where Arch's archives come from (owner, 2026-10-28):** `sources.archlinux.org` keeps only a
    small subset (33 of the 518 the first ISO needs). The archive is taken from there when it
    exists; otherwise it is made the way Arch makes it: the package's PKGBUILD at the tag of that
    exact version in Arch's packaging repository, with every upstream source downloaded and
    checked against the PKGBUILD's checksums (`makepkg --allsource`). Every package, not only the
    copyleft ones (owner: the users see no difference, and we depend less on Arch).
  - **Generated patches (owner, 2026-10-28, option 1):** a patch that GitHub or GitLab generates
    from a commit or a pull request can change its header lines over time, so its checksum stops
    matching Arch's PKGBUILD while the change to the code is the same. Only when every file that
    failed is such a patch is the archive made with the files just downloaded, and the difference
    is written in a notes file next to it. Any other failed checksum stops the release.
- **Licence notices:** every package keeps its licence files (`/usr/share/licenses`); the ISO and
  the UI ("About → Licences", later) list the licences of what OwneetOS ships.
- **Proprietary but redistributable components** (NVIDIA driver, device firmware, CPU microcode)
  are shipped only as their licences allow, unmodified, with their licence texts.
- **Widevine consent (owner, 2026-10-19):** Brave downloads Widevine with "By installing, you'll
  agree to Google's terms of use", so the **console asks for the user's consent** (once per user,
  at the first opening of a web app; *Read the terms* opens Google's live page, never a copy) and
  **again at every new Widevine version**
  (owneetd sees the version in each web app's profile, `WidevineCdm/<version>`), replacing 5.1's
  silent opt-in; in [[step-5.4-netflix]] (demo first). Brave's own question is turned off: it is a
  window of Brave's that the controller cannot reach. A change of Google's terms without a new
  Widevine version cannot be seen by the console without asking a server: to the legal review
  ([[step-7.5-legal-review-before-the-public-launch]]).
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
- **The extension against the terms (checked 2026-10-18, owner):** it only moves a selection ring,
  clicks, scrolls and types in answer to the user's buttons; it changes no content, scrapes
  nothing, blocks no ads and changes no user agent (the extension itself: Brave blocks ads, and
  owneetd starts YouTube with a TV user agent, see below). Its scripts are content scripts loaded by
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
    [[step-5.3-youtube]]. **TV user agent (owner, 2026-10-18):** YouTube opens its TV interface
    with a TV user agent set by owneetd (brand-neutral first). The owner's view: allowed, since the
    terms allow the modes the service makes available, the TV interface is one of them, and a user
    agent alters neither the app nor its content; it still **goes to the legal review**
    ([[step-7.5-legal-review-before-the-public-launch]]). On the TV interface the extension only
    sends the keys a remote or a keyboard would (arrows, Enter, Escape), each on the user's button,
    and shows nothing in the page (2026-10-19).
  - **Spotify** (Terms of Use §3, User Guidelines): no bot, script or automated process (about
    inflating plays), no modifying or altering the Services, no ad blocking. Nothing applies to
    the extension.
- **Brave's ad blocking (found 2026-10-18):** Brave's Shields block ads by default and the managed
  policies (`packages/owneet-base/brave-policies.json`) do not turn them off, so YouTube's and
  Spotify's ads are blocked in the web apps (Spotify's terms forbid ad blocking; YouTube's forbid
  circumventing). **Kept as it is** (owner, 2026-10-18); **goes to the legal review**
  ([[step-7.5-legal-review-before-the-public-launch]]), which decides whether the policies turn
  ad blocking off for the web apps.
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
| 2026-10-18 | YouTube opens its TV interface with a **TV user agent** set by owneetd from the catalogue, brand-neutral first; the owner holds it allowed (the TV interface is a mode the service makes available; a user agent alters neither the app nor its content), and it goes to the legal review of step 7.5. **Brave's Shields block the web apps' ads** by default (no policy turns them off): kept as it is, to the legal review of 7.5. |
| 2026-10-19 | **Widevine consent:** the console asks for the user's consent to Google's terms (once at the first web app, and at every new Widevine version) instead of 5.1's silent opt-in, in step 5.4; Brave's own question turned off (unreachable with the controller). A change of Google's terms alone cannot be detected without a server: to the legal review of 7.5. |
| 2026-10-19 | Widevine consent: once **per user**, at the first opening of a web app; *Read the terms* shows **Google's live page** in the web apps' window (Google's terms are never copied into the console: no free licence, and a copy goes stale); a QR code rejected. |
| 2026-10-25 | The OwneetOS trademark is not registered (the authors: too costly for its worth). The preliminary search of 2026-10-24 found no conflicting mark; the project only makes sure everything it does is legal. |
| 2026-10-28 | Source archive (step 7.2, option a): our packages' PKGBUILDs and sources per release; every Arch package's exact `.src.tar.gz` copied from `sources.archlinux.org` to a shared `sources/` folder on SourceForge; a release missing any source publishes nothing. |
| 2026-10-28 | Arch's source archives: `sources.archlinux.org` keeps only a subset (33 of 518), so the missing ones are made like Arch makes them (PKGBUILD at the version's tag in Arch's packaging repository, upstream sources checked, `makepkg --allsource`); every package, whatever its licence. |
| 2026-10-28 | A generated patch (GitHub or GitLab, from a commit or a pull request) whose checksum drifted is accepted and noted next to its archive; any other failed checksum stops the release. |
