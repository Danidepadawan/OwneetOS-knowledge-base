---
type: functional-analysis
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

The demos play the interface sounds from `design/demos/sounds.js` ([[sound-files]]).
Fonts and wordmark: [[design-tokens]].
