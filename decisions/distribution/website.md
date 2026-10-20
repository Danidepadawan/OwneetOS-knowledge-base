---
type: decision
description: "The project's website: Angular, static on GitHub Pages, own repository and folder, its pages, English and Italian, no data collected, download as a redirect."
area: distribution
status: active
decided: 2026-10-20
updated: 2026-10-20
tags: [decision, distribution, website]
---
# Website

Agreed with the owner on 2026-10-20, before the release; built in [[step-7.8-website]].

- **Angular**, prerendered to a **static site** and published on **GitHub Pages** with the
  project's `.org` domain ([[distribution-and-updates]]; the name depends on the domain found,
  e.g. `owneet-os.org`, created by the owner). No server of our own ([[online-and-chat]]).
- **Its own project and repository:** the folder `OwneetOS-website/` next to `OwneetOS/` and this
  vault (inside the project folder), the repository `fancy-dino/OwneetOS-website`, created by the
  owner and shared with Danidepadawan. Everything known about the website (decisions, steps)
  stays in this vault.
- **Pages:** home (what OwneetOS is, pictures, who it is for), features, system requirements,
  download, installation guide, FAQ, credits and licences, privacy, how to contribute and
  translate.
- **The home is one page** (owner, 2026-10-20): each section fills the screen and the scrolling
  snaps from one to the next; the address follows the section on screen (`#features`,
  `#requirements`, ...) and opening it scrolls there. Little text: short titles and one short
  line; the features in a carousel showing one card at a time, the next one half a screen away
  (no fade or blur of side cards, owner, 2026-10-20). It plays by itself every 5 s and loops
  (after the last card comes the first, going on in the same direction), with arrows and dots;
  it stops only while the pointer is on it (or it has focus from the keyboard) and while it is
  off screen. No pause button (owner, 2026-10-20: it was tried; WCAG 2.2.2 asks for one on moving
  content, the owner chose without).
- **English and Italian**, the texts in translation files, never written in the code (as in the
  console, [[ui-text-and-i18n]]).
- **Look:** the console's tokens and fonts (Bricolage Grotesque, Lexend, the palettes,
  [[design-tokens]]) and its logo ([[step-7.6-final-logo-and-brand]]).
- **No data collected:** no analytics, no cookies, no forms, no newsletter, **no third-party
  requests**: the fonts are served by the site itself (never from Google Fonts or another CDN,
  which would see the visitor's address). The privacy page says so.
- **Download:** only a redirect to the ISO on SourceForge ([[distribution-and-updates]]), once
  releases are published with their GPL source archive and signed (steps 7.2, 7.4,
  [[legal-compliance]], [[package-signing]]); until then the page says "coming soon".
- **Licence:** GPL-3.0-or-later for the website's code, like OwneetOS ([[repository]]); its texts
  CC BY-SA 4.0.
- **Node on the host:** the owner's Node (installed with nvm in the home folder) is used on the
  host; the website's dependencies stay in its folder (no global installs), and every
  installation is asked first ([[development-environment]], [[host-safety]]).
- Like every screen, its pages get a mockup and an interactive demo approved before their code
  ([[demo-before-code]]).

## Why

The vault already had "website on GitHub Pages with a `.org` domain" (2026-10-11); the owner chose
Angular and a repository of its own shared with Danidepadawan. Node on the host (option a) instead
of the builder VM: a website build is not an ISO or a package, and the dependencies stay in the
project folder. No data collected keeps the site free of consent banners and GDPR duties.

## Creates

- Guards: none new ([[host-safety]], [[legal]], [[product-invariants]] apply).
- Best practices: none yet.
- Steps: [[step-7.8-website]].

## History

| Date | Decision |
|---|---|
| 2026-10-20 | Website agreed: Angular, static on GitHub Pages, own folder and repository (shared with Danidepadawan), the pages, English and Italian, the console's look, no data collected, download as a redirect to SourceForge, GPL code and CC BY-SA texts, Node on the host (option a); new step 7.8, started at the owner's request while phase 5 is with Danidepadawan. |
| 2026-10-20 | Home demo feedback: one page whose sections snap, the address following the section on screen; less text; the features in a carousel showing one card at a time with arrows and dots (fading, then blurred side cards were tried and rejected), playing by itself and looping, stopping only while pointed at (a pause button was tried and removed); the console picture to follow the real home screen (generic apps instead of service names), refined later with Danidepadawan's changes. Fonts served by the site itself, no third-party requests. |
