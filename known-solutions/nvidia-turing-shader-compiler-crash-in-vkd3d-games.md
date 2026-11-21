---
type: known-solution
description: "A DirectX 12 Steam game (Cyberpunk 2077) closes a few seconds after starting on an NVIDIA Turing card (GTX 16xx, RTX 20xx): NVIDIA's shader compiler stops on \"Unsupported: extractelement <8 x i4>\" (exception 0xc000001d in libnvidia-gpucomp). Not ours: a fix waits in vkd3d-proton's shader translator."
status: open
seen: 2026-11-18
updated: 2026-11-20
tags: [known-solution, steam, proton, nvidia]
---
# A DirectX 12 game closes at once on an NVIDIA Turing card

## Symptom

A Steam game made for DirectX 12 starts (Cyberpunk 2077: its launcher, then "Play"), shows nothing or a black
window for a few seconds, and closes; Steam says it ended normally, the console goes back home. FrankenPC
(GeForce GTX 1660 SUPER, NVIDIA driver 615.71.09), 2026-11-18, [[open-items]] 13.

- The journal, from Steam's children, just before the end: `Unsupported: %… = extractelement <8 x i4> …`.
- Proton's log (testers' switch `owneet.debug.windows_log=on`, `<log>.games/proton-steam-APPID.log`):
  `Exception 0xc000001d at …: …/libnvidia-gpucomp.so.615.71.09` and
  `err:vulkan:vkCreateComputePipelines Exception 0xc000001d in Unix call.`

## Cause

A bug of NVIDIA's shader compiler on Turing GPUs (GTX 16xx, RTX 20xx; also reported on other series): one compute
shader of the game (Cyberpunk 2077 2.5, shader `2169eb1a6850d504`), translated by vkd3d-proton, packs a 4-bit
bit-reversal into an `<8 x i4>` vector the driver cannot handle, and the driver stops on an illegal instruction
(`ud2`, exception 0xc000001d). Not OwneetOS, not the controller, not the launcher. Reported for drivers 610, 615
and 620; other games are hit too.

## Solution

**Open.** The fix is NVIDIA's: the change proposed in vkd3d-proton's shader translator (dxil-spirv pull request 344)
was closed unmerged on 2026-11-02 by its maintainer ("This will be fixed in NV driver where it belongs"); the same day
an NVIDIA engineer said they have a fix (NVIDIA bug 7014466). So the cure is a newer NVIDIA driver: OwneetOS ships it
with an update of its pinned packages as soon as a driver with the fix is out (615.78.08 and 620.70.06 were still
reported broken). Meanwhile, for Cyberpunk 2077: Steam's own beta "2.31" of the game (Steam → the game's properties →
Betas, with the controller) is reported to avoid the crash, but an older version of the game may not open saves made
with a newer one. The workaround people use (dump the shader, re-optimise it with `spirv-opt`, load it
with `VKD3D_SHADER_OVERRIDE` in the game's launch options) needs a terminal and files per game: not for the
console.

## Research of 2026-11-19

- No NVIDIA driver with the fix yet: 620.70.06 (2026-11-04, the R620 branch's first) lists no such fix, and users
  report Cyberpunk 2077 still closing with it ([NVIDIA's 620 thread](https://forums.developer.nvidia.com/t/620-release-feedback-discussion/388030)).
- The bug is wider than Turing: vkd3d-proton issue 3405 has it on 615.71.09, 615.78.08, 620.70.06 and on an RTX 5090
  with 595.112.07; Proton issue 4450 on an RTX 4060 (Ada, 595.99.02) with Proton Experimental 20261112 only
  (proton-11.0-2e works there). Proton 9.0-4 still crashes on an RTX 2060 (2026-10-31).
- dxil-spirv pull request 344 (the translator's rewrite of the 4-bit bit reversal) made pipeline creation work on a
  Turing card (RTX 2070, 615.78.08); it is not merged. The shader override works for users (2026-11-15) but needs a
  copy of the game's own shader: OwneetOS cannot ship it ([[legal]]: no game content redistributed).
- Ways in OwneetOS's hands were proposed (2026-11-19); **the owner dropped the matter (2026-11-20): a fault of NVIDIA's
  driver on that card, not of OwneetOS.** Nothing is built for it; a newer NVIDIA driver in a pinned-packages update
  may fix it.

## How we found it

1. owneetd's log: the game's processes (`REDprelauncher.exe`, then the launcher, then the game) all ended within
   a second of the game's start, Steam saying "success". Not enough.
2. Proton's log for Steam's games did not exist: the testers' switch now turns it on (owneetd 0.25.34,
   owneet-base 0.0.80).
3. Proton's log: the exception in `libnvidia-gpucomp` during `vkCreateComputePipelines`; the journal's
   "extractelement <8 x i4>" line; searching both found vkd3d-proton issue 3405 and NVIDIA's forum reports.

## Watch out

- A DirectX 12 game that closes at its start on an NVIDIA card: look for `0xc000001d` and `libnvidia-gpucomp` in
  Proton's log first.
- After a Proton update, try Cyberpunk 2077 again and close this note (`status: solved`).
