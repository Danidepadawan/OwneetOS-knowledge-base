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
  confirmed); Guide and FAQ leave the header for a new "Info" section of the home ("Need
  help?", two cards leading to the guide and the FAQ). The hand-drawn icons replaced by Lucide's
  ([[website]]).
- **Home demo approved (owner, 2026-10-20):** `design/demos/7.8-website-home.html` (one page:
  home, features carousel, requirements, open, info, download; English and Italian; Lucide's
  icons, credited in `CREDITS.md`). The console picture is refined later with Danidepadawan's
  home screen changes. Next: the Angular project, its downloads approved by the owner first.
- **Angular project created (owner's approval of the downloads, 2026-10-20):**
  `OwneetOS-website/`, its own git repository on `feature/step7_website` (first commit 47147be;
  the owner creates `fancy-dino/OwneetOS-website` on GitHub, shares it with Danidepadawan and
  pushes). Angular CLI 22.2.1 run once with `npx`, dependencies installed with
  `npm install --before=2026-10-06` (all `@angular/*` 22.2.1, TypeScript 6.0.3, Vitest 5.0.3; 281
  packages, 306 MB in `node_modules`), npm's cache in `OwneetOS/out/npm-cache`: nothing written
  outside the project folder (checked). The CLI's usage statistics off (`NG_CLI_ANALYTICS=false`,
  `"analytics": false`). SCSS, routing, zoneless, `outputMode: static` (every page prerendered,
  the Express server removed). npm 11 blocked the install scripts of esbuild, lmdb,
  msgpackr-extract and @parcel/watcher: left blocked, the build works without them. Angular's
  welcome page and favicon (its logo) removed; SPDX headers, GPL-3.0 `LICENSE`, `README.md`,
  `CREDITS.md`. Checked: `ng build` prerenders the page, `ng test` passes. Next: the approved home
  in Angular components (texts in translation files, fonts and Lucide served by the site).
- **Repository and CI (2026-10-20):** the owner created `fancy-dino/OwneetOS-website` (public),
  invited Danidepadawan (personal repository: collaborators have no roles to choose) and pushed.
  The `main` ruleset copied from OwneetOS required its Lint and ISO checks, which never run here:
  removed. `.github/workflows/ci.yml` (check **Build**) builds and tests, checked on a clean copy
  (`npm ci`, `ng build`, `ng test`); once it has run on GitHub, "Build" becomes required.
- **The home in Angular (2026-10-20, website commit ea9470f):** the owner chose the texts in JSON
  files like the console's (English at `/`, Italian at `/it`) and the current wordmark. A first
  version with short file names was rejected: the owner asked for a real Angular structure
  ([[angular]]: `core/services`, `shared/components`, `components`, `pages`; `.component.ts`,
  `.service.ts`; models in `.model.ts`). Components: header, home (sections, dots), console
  screen, features carousel, icon (Lucide), wordmark; the console's fonts in `public/fonts/` with
  their OFL licences, credited. Checked: `ng build` prerenders `/` and `/it` (`lang` and title of
  each), `ng test` 4 tests (the app, both languages, the same keys in every language, `{n}`),
  screenshots of every section in English (1280 px) and Italian (390 px) matching the demo.
  Then, at the owner's request, every component moved under `core/components/` next to
  `core/services/` (no `pages`, no nested `components`); build and tests passed again.
- **The Angular home approved (owner, 2026-10-20):** tried with `ng serve`; the only change asked:
  no "Signed, with its source code." under "Coming soon" (it says nothing to users; the
  releases stay signed and with their sources, [[package-signing]], [[legal-compliance]]).
  Still to do in 7.8: the other pages (guide, FAQ, credits, privacy, contributing), each with its
  demo first, and the publication on GitHub Pages.
- **`.npmrc` (owner, 2026-10-23):** the site's `.npmrc` keeps npm's cache and logs in
  `OwneetOS-website/.npm-cache/` (ignored by git): `npm start` is all the owner needs (checked:
  nothing written to `~/.npm`).
