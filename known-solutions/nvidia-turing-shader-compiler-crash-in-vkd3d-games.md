---
type: known-solution
description: "A DirectX 12 Steam game (Cyberpunk 2077) closes a few seconds after starting on an NVIDIA Turing card (GTX 16xx, RTX 20xx): NVIDIA's shader compiler stops on \"Unsupported: extractelement <8 x i4>\" (exception 0xc000001d in libnvidia-gpucomp). Not ours: a fix waits in vkd3d-proton's shader translator."
status: open
seen: 2026-11-18
updated: 2026-11-18
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

**Open.** A fix is proposed in vkd3d-proton's shader translator (dxil-spirv pull request 344: the bit-reversal
written as a native bit-reverse); it reaches us with a Proton (Experimental) update, nothing to change in OwneetOS.
Then start the game again. The workaround people use (dump the shader, re-optimise it with `spirv-opt`, load it
with `VKD3D_SHADER_OVERRIDE` in the game's launch options) needs a terminal and files per game: not for the
console.

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
