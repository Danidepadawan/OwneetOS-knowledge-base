---
type: functional-analysis
description: "The approved mockups and interactive demos (design/ in the code repository), one per screen."
legacy: "design/README.md"
tags: [functional-analysis, design]
---
# Mockups and demos

The approved look and behaviour of each screen, as HTML files in the code repository (`design/`).
Open them in a browser; they can be driven with the keyboard or a gamepad. Process:
[[demo-before-code]].

| File | Screen | Step |
|---|---|---|
| `design/mockups/wave1-mockups.html` | Approved Wave 1 mockups (first boot, home, library, settings) | [[step-0.2-wave-1-ui-mockups]] |
| `design/demos/3.3-theme-foundations.html` | Type scale, palette tokens with live contrast check, focus ring, components, text sizes, button prompts, TV safe area, palette picker, language list. Start state: `#pal=ember&glyphs=ps&lang=it&ts=1.2&safe=1` (add `&open=palette` or `&open=language`) | [[step-3.3-theme-foundations]] |
| `design/demos/3.3b-scrolling-text.html` | Long texts: the highlighted text that does not fit scrolls (pause, steady speed, pause, back to the start), the others end with "…"; on Settings with text size XL; speed and pauses to choose. Start state: `#lang=en&ts=1&at=panel`. Approved 2026-11-12 (open item 3s) | [[step-3.3-theme-foundations]] |
| `design/demos/3.3c-prompt-bar-fit.html` | A prompt bar that does not fit (the library, Italian, text size XL): only then the prompts on the right keep their buttons and lose their words; text size and language to change. Start state: `#lang=en&ts=1.2`. Approved 2026-11-12 (open item 3w b) | [[step-3.3-theme-foundations]] |
| `design/demos/3.6c-hero-card-fit.html` | The home's big card when its content does not fit (text size XL, a running game, a long title): buttons clipped and sliding to the selected one, the title on one line, scrolling while a button of the card is selected. Start state: `#at=2` (the third button). Approved 2026-11-13 (open item 3ab) | [[step-3.6-home-screen]] |
| `design/demos/3.7b-cover-title-scroll.html` | Covers' titles in the library on one line: "…" when they do not fit, scrolling while the cover is highlighted, so the badge never sits over them; "Before" shows today's covers (up to three lines) to compare. Start state: `#mode=before`, `#ts=1`, `#at=1`. Approved 2026-11-13 (open item 3ad) | [[step-3.7-library-screen]] |
| `design/demos/3.7c-library-resume-pointer.html` | The library's Options on the running game: "Resume", "Resume with the pointer" (the pointer's help the first time), the usual options; extras to choose: "Close game", the "Running" badge and A = "Resume". Start state: `#open=options`, `#close=1`, `#badge=1`, `#lang=en`. Approved 2026-11-13 with "Close game" (the extras dropped); built (open item 2) | [[step-3.7-library-screen]] |
| `design/demos/6.11-file-manager.html` | Settings → Advanced → File manager: places named for the user (games folders, Windows games' data, games' logs, Steam's leftovers), folders, Options → Delete with its question, the "may hold saves" question first for Windows data, Steam's leftovers only with Steam closed; second round (owner): folder icons in a grid with a status bar. Start state: `#at=places`, `windows`, `games`, `saves`, `steam`; `#lang=en`. Waits for the owner's approval (open item 3t) | [[step-6.11-simplified-file-manager]] |
| `design/demos/3.6-home.html` | Home: continue playing, apps, notices, recently played, sections on LB/RB; states "game running" and "no games yet" | [[step-3.6-home-screen]] |
| `design/demos/3.7-library.html` | Library: grid, filters, sort, favourites, disks and the Disks window (`#disks=1\|2\|4`) | [[step-3.7-library-screen]] |
| `design/demos/3.9-settings.html` | Settings: network, controllers and pairing, sound, display, appearance, language, disks, system | [[step-3.9-settings]] |
| `design/demos/3.9c-display-area.html` | Settings → Display → "Display area": the full-screen adjustment for TVs that cut the edges, on a simulated TV (its cut chosen below the picture). Start state: `#area=0.04&adjust=1&lang=en`. Approved 2026-11-12 (open item 3y) | [[step-3.9-settings]] |
| `design/demos/3.10-osk.html` | On-screen keyboard | [[step-3.10-on-screen-keyboard]] |
| `design/demos/3.11-notifications.html` | Banners, bell, notifications list | [[step-3.11-notifications]] |
| `design/demos/3.13-startup-power.html` | Start-up animation and quick menu | [[step-3.13-start-up-animation-and-power-options]] |
| `design/demos/4.2-library-add-games.html` | Library with "Add games" | [[step-4.2-steam-integration]] |
| `design/demos/4.3-games-on-disk.html` | Games on a USB stick or disk: the disk plugged in and out with its notice, its games in the library (folder's name, `cover.jpg`), "Which file starts the game?", Options → "Choose the file to start", the disk in the details (`#disk=0&open=choose\|options\|details`) | [[step-4.3-local-drm-free-games]] |
| `design/demos/4.5-windows-games.html` | Windows games on the disk listed like the others; the download they need the first time (home notices, Settings → System, banner when ready); a Windows game started before it is ready (progress, or connect to the internet); "Preparing {game}…"; GOG's info file or the usual question for the file to start; a Steam game whose Linux version does not start (`#win=waiting\|downloading\|ready&net=off&section=home\|settings&open=offline\|progress\|prep\|choose\|broken`) | [[step-4.5-windows-games-proton]] |
| `design/demos/4.2c-steam-library.html` | Every owned Steam game in the library, installing and uninstalling through Steam's confirmation, downloads, the display-errors notice, no internet (`#gpu=amd&net=off&first=1&open=install\|notice\|steam\|uninstall\|details\|offline\|store`) | [[step-4.2c-steam-without-its-interface]] |
| `design/demos/6.1-first-start.html` | The first start: pairing (as the mockup), language, network or later, time zone (suggested or a list of cities), the Xbox adapter's firmware with consent, ready | [[step-6.1-first-boot-flow]] |
| `design/demos/6.4-installer.html` | The installer: welcome, the internal disks, the console's name, the warning (Windows or BitLocker to confirm with a switch), A held three seconds to erase and install, progress, end, errors | [[step-6.4-installer-ui]] |
| `design/demos/6.6-moving-games.html` | Moving games between disks: the disks with their room, copy with Cancel, check, the original removed after; Steam's games moved by Steam; "Play from here / Copy to the console" | [[step-6.6-moving-games-and-media-between-disks]] |
| `design/demos/6.6b-choose-games-to-copy.html` | A plugged-in disk: "Which games to copy?", a switch per game and "All games", then the disk (approved 2026-11-09) | [[step-6.6-moving-games-and-media-between-disks]] |
| `design/demos/6.6c-move-single-games.html` | A plugged-in disk: "Copy" and "Remove the original" switches on each game, the originals removed only after the check; a read-only disk keeps them (approved 2026-11-10) | [[step-6.6-moving-games-and-media-between-disks]] |
| `design/demos/6.6d-check-progress.html` | "Check the copy" and the removal of the original with their own percentage and bar, as the copy; no step for a kept original; copying several games, "Stop?" offers "Stop this game" or "Stop all" (owner's corrections of 2026-11-10; approved 2026-11-10) | [[step-6.6-moving-games-and-media-between-disks]] |
| `design/demos/6.6e-copy-behind.html` | A copy that goes on behind: Guide (Home) closes its window and shows the home screen (only that window); the top bar shows the copy's step and percentage, the covers of its games their state, A on one shows the window again; one copy at a time; the end or a failure with the window closed in a notice (owner's report of 2026-11-10; approved 2026-11-10, corrected: Guide only on the copy's window) | [[step-6.6-moving-games-and-media-between-disks]] |

| `design/demos/7.8-website-home.html` | The website's home: one page whose sections snap (home, features carousel, requirements, open, info, download), English and Italian | [[step-7.8-website]] |

| `design/demos/7.8b-website-pages.html` | The website's pages: guide, FAQ, credits (the authors first), privacy, contributing; the gamepad "O" logo and its start-up animation | [[step-7.8b-website-pages]] |
| `design/demos/7.8m-website-header.html` | The website's header: the languages in a drop-down menu, the light / dark switch | [[step-7.8m-website-header]] |
| `design/demos/7.8n-website-home.html` | The website's much simpler home: five sections following the slogan, real screens of the console. |
| `design/demos/7.8d-website-not-found.html` | The website's not-found page: in the address's language (`/it/...` in Italian), the way home, the guide and the questions | [[step-7.8d-website-not-found-page]] |
| `design/demos/7.8e-website-favicon.html` | The website's favicon from the gamepad "O": three shapes, its colours, on light and dark tab bars, at 16 and 32 px, on a phone | [[step-7.8e-website-favicon]] |
| `design/demos/7.8f-website-sharing-picture.html` | The picture shown when a link to the website is shared: logo and slogan, or logo and the home's title; Dusk or Daylight; in link previews | [[step-7.8f-website-search-and-sharing]] |
| `design/demos/7.1-updates.html` | The updates in Settings → System: notice, "What's new", optional package details, install, restart now or later, going back to the previous or any version, the notice after a failed update | [[step-7.1-updates]], [[step-7.1b-going-back-to-any-version]] |

The demos play the interface sounds from `design/demos/sounds.js` ([[sound-files]]).
Fonts and wordmark: [[design-tokens]].
