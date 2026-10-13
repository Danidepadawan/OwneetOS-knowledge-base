---
type: guard
tags: [guard, environment]
---
# Guard: the developer's PC

- **Never damage the developer's PC or its installed OS** (host: Linux Mint).
  ([[development-environment]])
- **Never install anything on the host** without asking the owner at the moment of installation,
  every time. ([[development-environment]])
- **Never build ISOs or packages, or run root tools, on the host**: only in the Arch builder VM
  (or CI); boot ISOs only in the test VM or on the owner's test hardware.
  ([[development-environment]])
- **Never put files outside the project folder** (sources, VM disks, caches, build artefacts all
  stay inside it). ([[development-environment]])
- **Never test the installer on real disks**: virtual disks only. ([[installer-and-firmware]])
- **Never run VirtualBox and KVM VMs at the same time** (they cannot share recent kernels).
  ([[development-environment]])
