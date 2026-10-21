---
type: known-solution
description: "In a web app LT / RT and the D-pad do nothing (the left stick, A and B work), and the right stick scrolls oddly: Brave reports the controller with no layout (mapping \"\"), in the Linux driver's order."
status: open
seen: 2026-10-22
updated: 2026-10-22
tags: [known-solution, extension, controllers, brave]
---
# A controller without the standard layout in Brave

## Symptom

- Inside a web app ([[step-5.4-netflix]]): **LT / RT do nothing**, and **the D-pad does nothing**
  (navigation works with the left stick, so it can go unnoticed); A and B work. The right stick
  scrolls the wrong way (its left / right scroll up / down; a pressed LT counts as the right stick
  pushed sideways).
- The same controller works everywhere in the console's own interface (which reads controllers
  through SDL and its mapping database).

## Cause

The Gamepad API gives the standard layout (`mapping: "standard"`: D-pad on buttons 12–15, LT / RT
on buttons 6 / 7, right stick on axes 2 / 3) only for controllers Brave knows. Others come with
`mapping: ""`, in the Linux driver's order. The Nacon GC-100 (`Vendor: 3285 Product: 0607`), an
Xbox-style controller on the xpad driver: 11 buttons (A B X Y LB RB View Menu Guide LS RS), 8 axes
(left stick 0 / 1, LT 2, right stick 3 / 4, RT 5, D-pad 6 / 7; triggers from −1 released to +1
pressed, and 0 until they first move). The extension read only the standard layout.

## Solution

`extension/content/pad.js` (owneet-base 0.0.49; to verify in the test VM): a controller with no
standard layout and that shape (11 buttons, 8 axes) is translated into the standard layout before
anything reads it; Guide (button 8 there) is never passed on. Other unknown layouts are read as
they come: if one shows up, the next step is owneetd telling the extension the controller's layout
from SDL's mapping database, which owneetd already has.

## How we found it

1. Everything worked except LT / RT; the owner navigated with the left stick, so the D-pad had
   never been tried in Brave.
2. A probe of the test VM only (`vm/run/probe-5.4d/`) showed what Brave reports: the controller's
   name, its `mapping`, the number of buttons and axes, and every button or axis that changed
   while the owner pressed LT, RT and the D-pad in a known order.

## Watch out

- Test web apps **with the D-pad**, not only the left stick.
- A new controller that misbehaves only in web apps: run the probe first (its name and `mapping`).
