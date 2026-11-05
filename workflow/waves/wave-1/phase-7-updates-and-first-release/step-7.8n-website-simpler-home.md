---
type: step
description: "The website's home made much simpler: five sections (Home, Plug it., Play it., Own it!, Download), a carousel of real console screens, the slogan as the header's links. Demo first."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.8n"
status: done
tags: [step, phase-7, website]
---
# 7.8n Website simpler home *(added 2026-11-04)*

Up: [[phase-7-updates-and-first-release]] · Status: **done** · Part of the website: [[step-7.8-website]]

- **Why (owner, 2026-11-04):** during the last review of the site, before Danidepadawan's last
  changes: as it is, the site is hard to navigate. The new sections follow the slogan.
- **Deliverables:** the home with five sections ([[website]]):
  1. **Home**, reached with the name: a carousel, one sentence beside one screen of the console, no
     other text and no buttons; under it a link to the credits ("Made by two really fed-up players,
     thanks to a lot of amazing people."). The first slide is the home screen with "Turn your PC into
     a game console, with a lightweight OS."; six more say what the features carousel says now,
     rewritten by the owner (below).
  2. **Plug it.**: the guide and the FAQ (today's "Info").
  3. **Play it.**: a short guide to using OwneetOS once it is set up, not complete but appealing.
  4. **Own it!**: OwneetOS belongs to everyone (today's "Open").
  5. **Download**, reached by scrolling to the end or with "Get OwneetOS"; no Download link in the
     header.
- **Demo approved (owner, 2026-11-04):** `design/demos/7.8n-website-home.html`, its screens in
  `design/demos/7.8n-website-home/` (made with `tools/preview-steps/site-home.txt` and
  `site-home-game.txt`).
- **Built (2026-11-04, site branch `feature/step7_8k_languages`):** in the five languages (German,
  French and Spanish are drafts, checked in [[step-7.8k-website-more-languages]]); pictures in
  `public/home-pictures/`, the tour in `PlayTourComponent`. Beyond the demo, which has no start-up
  animation: what plays by itself waits for its end, or the first slide would be over as it ends. The
  old addresses (`#features`, `#requirements`, `#open`, `#info`) simply open the home. The drawn console
  picture left the site ([[step-7.8j-website-console-picture]]).
- **Approved (owner, 2026-11-04)** on the development server. Publishing is the owner's: it goes out with
  the merge of the site's branch into `main`, all of it ([[website]]).
- **In the approved demo:**
  - The header's links are "Plug it.", "Play it.", "Own it!", in every language like the slogan.
  - One sentence per slide.
  - "Play it.": four moves with their five buttons (LB / RB, A, Home, B); the console's screen follows
    the chosen one, and they take turns every 5 s by the carousel's rules. The Home line says that
    with Steam it is held for a second ([[guide-button]]).
  - "Own it!": the line becomes "OwneetOS belongs to everyone."
- **Owner's answers and corrections (2026-11-04):**
  - The Requirements section leaves the home: the requirements stay in the guide
    ([[step-7.3-user-guide]]). The dots on the right stay, one per section.
  - Seven slides: "Your controllers" (redundant) and "Light" leave; "lightweight" goes in the first.
    New sentences: "You only need a controller. Mouse and keyboard are optional."; "One library for
    all your games."; "Safe updates. Something wrong? Roll back to your version of choice."; "Your
    style: multiple palettes and languages."
  - Texts: "Five buttons and you're playing."; the quick menu's "power options and a quick tutorial";
    "Own it!": "Completely free and open source", "No forced telemetry, we respect your privacy",
    "We will NEVER force updates on you", "A community driven, ever growing project"; the download's
    title "Almost here!". In every language. Offline is left out: for DRM-free games it is obvious.
  - "Own it!"'s icons: Lucide's `globe-off` and `user-group` replace `wifi-off` and `users`. The site's
    `icon.data.ts` has them, and `house` for "Play it.", from `lucide-static` 1.52.0.
  - "No forced telemetry" stands: the crash reports sent only with consent are optional telemetry, in
    the owner's words ([[online-and-chat]], [[legal-compliance]]).
- **Before publishing:**
  - The screens are taken again after [[step-5.7-apps-page]] if it changes them, in each
    language (the preview needs a way to choose it, as for [[step-7.3-user-guide]]).
- **Renumbered (2026-11-05):** first called 7.8m by mistake: [[step-7.8m-website-header]] already had
  that number, on a branch not merged yet. The published site's comments (`home.component.ts`,
  `play-tour.component.ts`) still say 7.8m and the old demo name, until its next change.
