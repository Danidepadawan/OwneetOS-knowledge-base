---
type: guard
tags: [guard, data]
---
# Guard: the user's disks and data

- **Never touch BitLocker partitions** automatically: detect them and guide the user to free space
  from Windows. ([[installer-and-firmware]])
- **Never erase anything without a clear warning and a final confirmation** in the installer.
  ([[installer-and-firmware]])
- **Never mount an NTFS volume left dirty by Windows** (Fast Startup, hibernation) read-write: mount
  it read-only and explain why. ([[disks]])
- **Never delete the original** when moving games or media between disks before the copy has been
  checked. ([[disks]])
- **Never move Steam games ourselves**: Steam moves them (its storage settings, opened from the
  console). ([[disks]])
