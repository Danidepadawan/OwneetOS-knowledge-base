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
| `design/demos/3.6-home.html` | Home: continue playing, apps, notices, recently played, sections on LB/RB; states "game running" and "no games yet" | [[step-3.6-home-screen]] |
| `design/demos/3.7-library.html` | Library: grid, filters, sort, favourites, disks and the Disks window (`#disks=1\|2\|4`) | [[step-3.7-library-screen]] |
| `design/demos/3.9-settings.html` | Settings: network, controllers and pairing, sound, display, appearance, language, disks, system | [[step-3.9-settings]] |
| `design/demos/3.10-osk.html` | On-screen keyboard | [[step-3.10-on-screen-keyboard]] |
| `design/demos/3.11-notifications.html` | Banners, bell, notifications list | [[step-3.11-notifications]] |
| `design/demos/3.13-startup-power.html` | Start-up animation and quick menu | [[step-3.13-start-up-animation-and-power-options]] |
| `design/demos/4.2-library-add-games.html` | Library with "Add games" | [[step-4.2-steam-integration]] |
| `design/demos/4.3-games-on-disk.html` | Games on a USB stick or disk: the disk plugged in and out with its notice, its games in the library (folder's name, `cover.jpg`), "Which file starts the game?", Options → "Choose the file to start", the disk in the details (`#disk=0&open=choose\|options\|details`) | [[step-4.3-local-drm-free-games]] |
| `design/demos/4.5-windows-games.html` | Windows games on the disk listed like the others; the download they need the first time (home notices, Settings → System, banner when ready); a Windows game started before it is ready (progress, or connect to the internet); "Preparing {game}…"; GOG's info file or the usual question for the file to start; a Steam game whose Linux version does not start (`#win=waiting\|downloading\|ready&net=off&section=home\|settings&open=offline\|progress\|prep\|choose\|broken`) | [[step-4.5-windows-games-proton]] |
| `design/demos/4.2c-steam-library.html` | Every owned Steam game in the library, installing and uninstalling through Steam's confirmation, downloads, the display-errors notice, no internet (`#gpu=amd&net=off&first=1&open=install\|notice\|steam\|uninstall\|details\|offline\|store`) | [[step-4.2c-steam-without-its-interface]] |

| `design/demos/7.8-website-home.html` | The website's home: one page whose sections snap (home, features carousel, requirements, open, info, download), English and Italian | [[step-7.8-website]] |

| `design/demos/7.8b-website-pages.html` | The website's pages: guide, FAQ, credits (the authors first), privacy, contributing; the gamepad "O" logo and its start-up animation | [[step-7.8b-website-pages]] |
| `design/demos/7.8d-website-not-found.html` | The website's not-found page: in the address's language (`/it/...` in Italian), the way home, the guide and the questions | [[step-7.8d-website-not-found-page]] |
| `design/demos/7.8e-website-favicon.html` | The website's favicon from the gamepad "O": three shapes, its colours, on light and dark tab bars, at 16 and 32 px, on a phone | [[step-7.8e-website-favicon]] |

The demos play the interface sounds from `design/demos/sounds.js` ([[sound-files]]).
Fonts and wordmark: [[design-tokens]].
