---
type: step
description: "hreflang links between the languages, sitemap.xml, robots.txt and the picture shown when the site is shared. Before the merge."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.8f"
status: done
tags: [step, phase-7, website]
---
# 7.8f Website search engines and sharing *(added 2026-10-23)*

Up: [[phase-7-updates-and-first-release]] · Status: **done** · Part of the website: [[step-7.8-website]]

- **Deliverables:** `hreflang` links between the English and Italian pages (and canonical
  addresses), `sitemap.xml`, `robots.txt`, the description and the preview picture shown when a
  link is shared (Open Graph), all generated with the site, no third-party service.
- **Done when:** the published pages carry them and a shared link shows the preview.
- **Progress (2026-10-24):** demo of the sharing picture `design/demos/7.8f-website-sharing-picture.html`
  (1200 x 630): A the logo and the slogan "Plug it. Play it. Own it!" in the middle, inside the
  middle square that some apps cut (one picture for every language), or B the logo, the home's
  title and line in the page's language and the gamepad "O" large at the right (one per
  language); Dusk or Daylight; shown whole and in two plain link previews (large, and cut to a
  square). The owner chose A in Dusk (2026-10-24).
- **Code (2026-10-24, website commit 4a6b49e):** `core/services/head/` sets each page's
  head: title and description, the canonical address and `hreflang` (en, it, x-default; the
  addresses end with "/" as the published folders), Open Graph (title, description, address,
  locale, `share-picture.png` 1200 x 630 with its alt text) and `twitter:card`; the not-found page
  only `noindex`. `scripts/sitemap.mjs` writes `sitemap.xml` (12 addresses with their languages)
  and `robots.txt` after the build; `scripts/make-share-picture.mjs` makes the picture with a
  Chromium already on the computer, from the logo, the site's font and the Dusk tokens. The
  site's address is `SITE_URL` (`define` in `angular.json`; the Pages workflow passes the address
  GitHub gives, so the domain changes nothing here). Long dashes removed from the site's texts
  (owner, [[writing-for-users]]). `robots.txt` only counts at a domain's root: it takes effect
  with [[step-7.8h-website-domain]]. **Open:** a shared link checked after the merge.
- **Outcome: approved by the owner on 2026-10-24** after the merge into `main`: the published pages carry the complete canonical and `hreflang` addresses; `sitemap.xml`, `robots.txt` and the sharing picture are online; the owner saw the preview in a chat.
