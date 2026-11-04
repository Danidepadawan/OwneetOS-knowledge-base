---
type: step
description: "The final OwneetOS logo and wordmark (the current wordmark is provisional), checked not to imitate others' logos; boot…"
phase: "[[phase-7-updates-and-first-release]]"
step: "7.6"
status: in-progress
legacy: "ROADMAP.md 7.6"
tags: [step, phase-7]
---
# 7.6 Final logo and brand

Up: [[phase-7-updates-and-first-release]] · Status: **in-progress**

- **Deliverables:** the final OwneetOS logo and wordmark (the current wordmark is provisional),
  checked not to imitate someone else's logo or a real controller's shape ([[legal-compliance]];
  OwneetOS's own trademark is not registered, 2026-10-25); boot splash, interface and documents updated;
  the website takes it in [[step-7.8i-website-final-logo]].
- **Draft (owner, 2026-10-19, outside the roadmap; nothing adopted yet):**
  `design/demos/logo-gamepad-o.html`. The wordmark stays "OwneetOS" (Bricolage Grotesque, "OS" in
  the second colour; the font may change later). The first "O" becomes a filled circle in the
  colour of "OS", 125 % of the old "O" and centred on it, with a generic gamepad cut out of it as
  a hole: one straight top edge with corners as round as the grips, two round ends below it as
  short grips, a narrower middle; D-pad and four buttons back in the circle's colour, no
  thumbsticks; the "Large" gamepad. Kept away from any real controller's outline (checked in this
  step, [[legal-compliance]]). Boot splash (still, on black):
  white letters, the "O" and "OS" `#B0B0B0`. Start-up animation, in the palette's colours,
  simplified on 2026-10-23 (owner) into **four beats**: 1, the whole logo appears over the whole first
  beat, 2 s long, in two variants: for the **website** from transparent, for the **distro** from the boot
  splash's colours (white letters, the "O" and "OS" `#B0B0B0`, already on screen) to the
  palette's; 2, "Plug it." at 2 s; 3, "Play it." at 2.5 s; 4, "Own it!" at 3 s
  (0.5 s apart) (the website's opening line), each
  word at once, no fade, already in its place 32 px under the circle (on a 1600 × 900 screen;
  in the system from the message files, translated). Before: the letters came out of the "O" as
  one strip, then "don't worry, it's yours!" faded in. Tried and
  rejected: the circle in the letters' colour with the gamepad in the second colour; a glow; a
  more intense colour; neon (soft and sharp); the three letters pulsing.
- **Started (owner, 2026-11-04):** friends, family and acquaintances all read the gamepad "O" draft
  as "wneetOS", so **the wordmark gets its letter "O" back** ("OwneetOS", the current outlines, "OS"
  in the second colour) and **the gamepad stays as a symbol of its own** (the same disc with the
  gamepad cut out, in the colour of "OS"). The draft's "O" above is given up.
- **Demo, first round (2026-11-04, code commit 83f473a on `feature/phase7`):**
  `design/demos/7.6-logo.html`: the two layouts the owner asked to compare, the symbol on the left
  and the symbol above, large, on the boot splash (white letters, the symbol and "OS" `#B0B0B0`)
  and in the top bar, the symbol alone from 192 to 16 px, every palette.
- **Owner's choice (2026-11-04):** less space between the symbol and the word (150 units on the left,
  100 above, in the outlines' units; proportions kept: the symbol 960 units wide on the left, 1250
  above, the letters 684 high); **the symbol above on the full screen, the symbol on the left in the top
  bar**. The slogan "Plug it. Play it. Own it!" under the full-screen logo, never translated ([[website]]),
  as far from the word as the symbol looks (the symbol's bottom to the small letters under it: about
  58 units of a 1600 x 900 screen; owner, code commit d9167a0). The demo shows this combination (code commit
  19ed391). The demo also plays both start-up animations with the new logo (code commit 0322d51), in the
  approved four beats; the boot splash keeps the slogan's room, so the logo stays in place when the
  console's animation starts.
- **Demo approved by the owner (2026-11-04).** Added at the owner's request, to check the timing: the
  start-up sound with the animations (code commit c0d6b45; from "Play again" or Enter, browsers
  allow sound only after a press; without the silence before it, as the package removes it). The
  final `startup.wav` has its three hits at about 1.98, 2.48 and 2.98 s from its first sound, on the
  animation's words at 2.0, 2.5 and 3.0 s. The console's animation starts on the boot splash's black,
  which fades into the palette's background with the logo's colours over the first 2 s (owner, code
  commit b8a5d6f). **The symbol's D-pad and buttons in a colour of their own** (owner, 2026-11-04, code
  commit c27dcf1), for contrast in every palette: the opposite of the symbol's colour, at least 4.5:1 on the
  palette's background (Dusk `#6FD3FF`, Tide `#FF9E8A`, Bloom `#7FE8C8`, Ember `#7CCBFF`, Espresso
  `#8AD0E8`, Harbor `#8FC4F5`, Forest `#FFA8C8`, Lagoon `#FFC56B`, Amethyst `#FFD66B`, Crimson `#7FE3EE`,
  Synthwave `#6FE8FF`, Amber `#8CBEFF`, Olive `#CDB2FF`, Daylight and Arctic `#B8400B`, Sand and Latte
  `#0B6A85`, Sakura `#0A6F6A`). In the black and white versions (the boot splash, Graphite) they stay in
  the symbol's colour. The two high contrasts have each other's colour (owner, code commit d2a0321): High
  contrast's blue lighter, `#8AB4FF` (10.1:1), High contrast light's yellow darker, `#6E5200` (7.3:1), since
  as they are they would be 2.3:1 and 1.3:1. It becomes a palette token in the final version
  ([[design-tokens]]).
- **The whole design approved by the owner (2026-11-04)**, with the console's black fading into the
  palette over the first 2 s. **Left:** the check that the symbol imitates no one's logo or a real
  controller ([[legal-compliance]]), and the boot splash, interface, documents and website.
- **Check that the symbol imitates no one, first pass (2026-11-04, the assistant, web searches; not a
  professional's opinion, and no search by image in the trademark registers):**
  - **Super Famicom / Super Nintendo controller, the closest shape:** the same elements (a cross on the
    left, four buttons in a diamond on the right, no thumbsticks, two round ends and a narrower
    middle). Nintendo filed an image of that controller as a trademark in December 2016 and later its
    four-button layout; the sources found do not say where or for which goods. Differences: a straight top
    edge, no shoulder buttons, no Start and Select, one colour for the buttons, drawn as a hole in a disc.
  - **Discord's "Clyde", the closest logo:** a registered trademark, described as a rounded form that
    suggests a gamepad, with two round eyes; a similar silhouette with a notch below. Differences: a
    D-pad and four buttons instead of two eyes, the disc around it; the two come nearer at 16-24 px, where
    the buttons blur.
  - **Generic use:** a controller in a logo is common (stock logos and templates); no single brand found
    with a disc and a controller cut out of it.
  - **In the symbol's favour:** in 2025 the EUIPO's Board of Appeal found the GameCube controller's button
    layout within the sector's norms, so not distinctive without proof of use; that case is another
    controller and a different question.
  - **Outcome:** nothing found that stops the symbol; two resemblances go to the lawyer
    ([[step-7.5-legal-review-before-the-public-launch]]). Sources: patent and trademark news on Nintendo's
    filings (nintendowire.com, nintendosoup.com, mynintendonews.com), reddie.co.uk on the EUIPO's decisions,
    logotyp.us and discord.com/branding on Clyde.
- **Owner's decision (2026-11-04):** the symbol stays as it is; both resemblances go to the lawyer.
- **After "Own it!" (owner, 2026-11-04):** as on the website, 0.8 s and a fade of 0.4 s into the pages, with the
  logo already in the top bar; no flight (4.2 s in all).
- **On the console (2026-11-04, code commit 84746a3 on `feature/phase7`):** `tools/branding/make-logo`
  generates `packages/owneet-branding/owneetos-splash.svg` and `foundation/LogoData.qml` from the same
  outlines. owneet-branding 0.0.4: the logo in white and grey in the middle, with the slogan's room
  below it, at a fixed 800 pixels wide (Plymouth does not scale: 42 % of a 1080p screen, against the
  demo's 50 %; the same on the loading screen), the spinner at 92 % of the height. owneet-frontend
  0.35.0: `Intro.qml` as in the demo, `foundation/Logo.qml` in the top bar, the first start and the
  installer, `Theme.logoButtons` per palette, `Theme.splashAccent`, the slogan in the message files, the
  same in every language. The beats run on a timer, not on animations, which follow the screen's
  frames (three times too fast in the preview, without vsync), so the words stay with the sound.
  **Checked:** `tools/lint`; the preview; in the test VM, on the installed system, a real reboot: boot
  splash, loading screen, colours, the three words, the fade into the first start, the logo not moving.
  **Not checked here:** with the sound (the VM has none) and on real hardware (next hardware test).
  **Left:** documents and the website ([[step-7.8i-website-final-logo]]). Found on the way:
  [[build-chroot-emptied-by-systemd-tmpfiles]].
