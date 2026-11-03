# Device agent guide

This repository is the **miatoll** (Redmi Note 9S / 9 Pro / Note 10 Lite / POCO M2 Pro, SM7125)
board of UniXNU. Shared SM7125 facts live in UniXNU-sm7125-common; firmware DSC/FDF integration
lives in qdizax-w/uefi-miatoll.

Rules:

1. Every commit uses the identity `qdizax-w <345028194+qdizax-w@users.noreply.github.com>`.
2. Never commit Apple or Qualcomm binaries. Firmware inputs are listed in proprietary-files.txt.
3. `fastboot boot boot.img` is RAM-only and safe. Nothing may write the `userdata` partition
   without the owner's explicit consent: the iOS root lives there and Android data is wiped.
4. Keep drivers/ArmCpu and scripts/build-xnu-4k-baseline.sh as upstream plus the documented
   deviation; re-base them when the UniXNU pin moves.
