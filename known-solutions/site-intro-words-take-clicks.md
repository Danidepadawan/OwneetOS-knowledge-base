---
type: known-solution
description: "Buttons in the middle of the website do not react and show a text cursor: the start-up animation's invisible words stayed over the page, because a child's visibility: visible outlives the host's hidden."
status: solved
seen: 2026-11-04
updated: 2026-11-04
tags: [known-solution, website, css]
---
# The site's start-up animation takes the clicks

## Symptom

On the website, once the start-up animation has ended, buttons in the middle of the window are hard
to press: most clicks do nothing and the mouse shows a text cursor over them, while the same button
works from another point. It follows the window's middle and not the page: scrolling moves the
buttons in and out of the dead zone. DevTools still shows `app-intro` with its logo and words.

## Cause

`intro.component.scss` showed each word of the slogan with an animation to `visibility: visible`,
kept by `forwards`, and ended the host with `opacity: 0; visibility: hidden`. `visibility` is the one
property a child can override under a hidden parent: the words stayed `visible` and, under a host at
opacity 0, invisible, in a fixed layer over every page, taking clicks and the cursor. The logo, which
never set `visibility`, was hidden with the host and took nothing.

## Solution

The words appear with `opacity` and never set `visibility`, so the host's `hidden` holds for all of
it (site commit b3561ea on `feature/step7_8k_languages`).

## How we found it

The owner saw the text cursor over the buttons and pointed at the elements left in DevTools. Without
reduced motion, after the 4.2 s of the animation, `document.elementFromPoint` over a grid of the
window found only the three words' `span`s inside `app-intro`, and of 10 real clicks on the carousel's
buttons 9 reached a `span`. After the fix: no point of the window, and 10 of 10.

A first check had found nothing, and led to a wrong fix (larger targets for the dots, reverted):
it ran with `--force-prefers-reduced-motion`, which skips the animation altogether.

## Watch out

- **Test clicks on the site without reduced motion too**: with it, the start-up animation is
  `display: none` and whatever it does to the page cannot show.
- Never use `visibility: visible` on a child of something that hides itself with `visibility`.
- When a click test presses the carousel's dots, measure each one just before pressing it: the active
  dot is wider, so the others move after every click.
