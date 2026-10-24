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
- **The home is one page** (owner, 2026-10-20): home, features, requirements, open, info (the
  guide and the FAQ), download; each section fills the screen and the scrolling
  snaps from one to the next; the address follows the section on screen (`#features`,
  `#requirements`, ...) and opening it scrolls there. Little text: short titles and one short
  line; the features in a carousel showing one card at a time, the next one half a screen away
  (no fade or blur of side cards, owner, 2026-10-20). It plays by itself every 5 s and loops
  (after the last card comes the first, going on in the same direction), with arrows and dots;
  it stops only while the pointer is on it (or it has focus from the keyboard) and while it is
  off screen. No pause button (owner, 2026-10-20: it was tried; WCAG 2.2.2 asks for one on moving
  content, the owner chose without).
- **The slogan "Plug it. Play it. Own it!" is never translated** (owner, 2026-10-24: more
  iconic): the same in every language's file and in the start-up animation (it replaces the
  Italian "Collegalo. Giocaci. Fallo tuo!" of 2026-10-20).
- **The credits open with the authors** (owner, 2026-10-24): Marco De Franco (fancy-dino) and
  Daniele De Padova (Danidepadawan), side by side at the same level on every screen; Daniele
  agreed to have his full name on the site (told by the owner, 2026-10-24).
- **English and Italian**, the texts in translation files, never written in the code (as in the
  console, [[ui-text-and-i18n]]): **one JSON file per language in the console's format**
  (`src/i18n/en.json`, `it.json`) read by the site's own `I18nService`, not Angular's XLIFF i18n
  (owner, 2026-10-20). Each language has its own address, prerendered: English at `/`, Italian
  at `/it` (more languages: a file and a path).
- **Look:** the console's tokens and fonts (Bricolage Grotesque, Lexend, the palettes,
  [[design-tokens]]) and its logo ([[step-7.6-final-logo-and-brand]]): for now the current
  provisional wordmark (owner, 2026-10-20), replaced in one place by the final logo of 7.6. The
  demo of the pages (2026-10-24) shows the gamepad "O" draft, and the site opens with the logo's
  start-up animation (website variant: from transparent), the site showing only after it.
- **Code structure:** a real Angular application ([[angular]], owner, 2026-10-20).
- **Icons: [Lucide](https://lucide.dev)** (owner, 2026-10-20; ISC License, some icons derived
  from Feather, MIT), instead of icons drawn by hand: every icon of the site, at a pinned version
  older than two weeks (`lucide-static` 1.52.0, checked against npm's SHA-512), credited in
  `CREDITS.md`. Tabler Icons and Phosphor (MIT) were the alternatives.
- **No data collected:** no analytics, no cookies, no forms, no newsletter, **no third-party
  requests**: the fonts are served by the site itself (never from Google Fonts or another CDN,
  which would see the visitor's address). The privacy page says so.
- **Download:** only a redirect to the ISO on SourceForge ([[distribution-and-updates]]), once
  releases are published with their GPL source archive and signed (steps 7.2, 7.4,
  [[legal-compliance]], [[package-signing]]); until then the page says "coming soon".
- **Licence:** GPL-3.0-or-later for the website's code, like OwneetOS ([[repository]]); its texts
  CC BY-SA 4.0.
- **Project setup** (owner, 2026-10-20): Angular 22 with **SCSS**, routing, zoneless,
  `outputMode: static` (prerendered files only, no server); new dependencies only at versions
  published at least two weeks earlier (`npm install --before=<date>`), npm's cache inside the
  project folder (the site's `.npmrc`: `.npm-cache/`, owner, 2026-10-23, so `npm start` is enough); the Angular CLI's usage statistics **always off** (mandatory: no telemetry,
  [[product-invariants]]).
- **CI** (owner, 2026-10-20): GitHub Actions builds and tests every pull request and every push
  to `main` (check **Build**: Node 24.21.0, `npm ci`, `ng build`, `ng test`), actions pinned by
  commit hash, nothing published; the check is required in `main`'s ruleset once it has run.
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
- Steps: [[step-7.8-website]]; before the merge [[step-7.8b-website-pages]],
  [[step-7.8c-website-publishing]], [[step-7.8d-website-not-found-page]],
  [[step-7.8e-website-favicon]], [[step-7.8f-website-search-and-sharing]],
  [[step-7.8g-website-lighter-fonts]]; after the merge [[step-7.8h-website-domain]],
  [[step-7.8i-website-final-logo]], [[step-7.8j-website-console-picture]],
  [[step-7.8k-website-more-languages]]; at the release [[step-7.8l-website-download-link]].

## History

| Date | Decision |
|---|---|
| 2026-10-20 | Website agreed: Angular, static on GitHub Pages, own folder and repository (shared with Danidepadawan), the pages, English and Italian, the console's look, no data collected, download as a redirect to SourceForge, GPL code and CC BY-SA texts, Node on the host (option a); new step 7.8, started at the owner's request while phase 5 is with Danidepadawan. |
| 2026-10-20 | Home demo feedback: one page whose sections snap, the address following the section on screen; less text; the features in a carousel showing one card at a time with arrows and dots (fading, then blurred side cards were tried and rejected), playing by itself and looping, stopping only while pointed at (a pause button was tried and removed); the console picture to follow the real home screen (generic apps instead of service names), refined later with Danidepadawan's changes. Fonts served by the site itself, no third-party requests. |
| 2026-10-20 | Project setup: Angular 22 with SCSS (not CSS), static output, dependencies at least two weeks old, npm's cache in the project, the CLI's usage statistics always off. |
| 2026-10-20 | Repository `fancy-dino/OwneetOS-website` created by the owner (Danidepadawan invited as a collaborator); CI "Build" on pull requests and `main`, to be required by `main`'s ruleset (OwneetOS's Lint and ISO checks do not apply here). |
| 2026-10-20 | Texts in one JSON file per language in the console's format, the site's own service (not Angular's XLIFF); English at `/`, Italian at `/it`; the current wordmark until 7.6; Angular structure and file names ([[angular]]). |
| 2026-10-20 | Icons: Lucide (ISC), pinned and checked, credited in `CREDITS.md`; Tabler Icons and Phosphor were the alternatives. |
| 2026-10-23 | The rest of the website split into steps 7.8b–7.8l: before the merge the pages, publishing on GitHub Pages, a not-found page, a favicon, search engines and sharing, WOFF2 fonts (optional, confirmed); after the merge the domain, the final logo, the console picture (and "Local pictures"), more languages; at the release the download link. |
| 2026-10-24 | Pages demo (7.8b, started before 7.8 is approved, the author's exception): guide, FAQ, credits, privacy, contributing; the gamepad "O" draft as the site's logo and its start-up animation before the site (website variant), in the demo; step 7.6 stays open. |
| 2026-10-24 | Pages demo approved. The slogan "Plug it. Play it. Own it!" is never translated (replaces the Italian "Collegalo. Giocaci. Fallo tuo!"); the credits open with the authors, Marco De Franco and Daniele De Padova. |
| 2026-10-24 | Not-found page demo approved (7.8d): a big "404", "This page is not here", the way home, the guide and the questions; in the language the address names (`/it/...` in Italian, else English); never listed by search engines. Built as the prerendered `/404` turned into `404.html` (Angular never prerenders catch-all routes). |
| 2026-10-24 | Favicon (7.8e): the whole gamepad "O" mark in the accent, following the device like the site (`favicon.svg`: Dusk orange, Daylight blue when light); `favicon.ico` (16, 32 px) and the phone's `apple-touch-icon.png` (180 px, on a square Dusk tile) in Dusk, the site's default palette. Made by `scripts/make-favicon.mjs` from the logo's data and the palette tokens. |
| 2026-10-24 | Search engines and sharing (7.8f): `hreflang` and canonical addresses, `sitemap.xml` and `robots.txt`, Open Graph with the sharing picture A (the logo and the slogan, in Dusk, one for every language), all generated with the site from its address (`SITE_URL`, given by GitHub in the Pages workflow). No long dashes in the site's texts. |
