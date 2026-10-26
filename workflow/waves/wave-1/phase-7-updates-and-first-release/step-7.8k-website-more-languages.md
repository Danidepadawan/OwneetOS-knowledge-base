---
type: step
description: "The website in German, French and Spanish: a JSON file and an address per language, checked by people the authors know before publishing."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.8k"
status: in-progress
tags: [step, phase-7, website]
---
# 7.8k Website in more languages *(added 2026-10-23)*

Up: [[phase-7-updates-and-first-release]] · Status: **in-progress** · Part of the website: [[step-7.8-website]]

- **Deliverables:** the site's texts in **German**, **French** and **Spanish** (owner,
  2026-10-25), each a JSON file in `src/i18n/` and its address (`/de`, `/fr`, `/es`), with the
  language links in the header, the `hreflang` links and the sitemap; the slogan stays in English.
- **Review:** the translations are drafted, then checked by people the authors know who speak
  each language (owner, 2026-10-25); a language is published once its check is done.
- **Note:** [[languages]] still lists Italian and English for Wave 1; the console's languages are a
  separate decision with the owner.
- **When:** after the website's merge (owner, 2026-10-23); the merge was done on 2026-10-24.
- **Built (2026-10-26, website commit fc84483 on `feature/step7_8k_languages`, owner's branch for this
  step, merged into `main` only after the reviews):** `de.json` ("du"), `fr.json` ("vous", « »
  quotes), `es.json` ("tú", words valid in Spain and Latin America where possible); `/de`, `/fr`,
  `/es` with their not-found pages, `hreflang` (6 per page), sitemap (30 addresses) and
  `og:locale`; the slogan in English. On a phone (below 640 px) the five languages move into the
  menu. The requirements' figures moved from the code into the message files ("4 Go" in French,
  "64 bit" in Italian). 11 tests pass. **Open:** the reviews by people the authors know (no
  review material asked for yet, owner 2026-10-26), then the merge.
