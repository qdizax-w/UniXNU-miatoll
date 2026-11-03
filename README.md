# UniXNU-miatoll

[UniXNU](https://github.com/UniXNU/UniXNU) device repository for the Xiaomi **Redmi Note 9S /
9 Pro / Note 10 Lite / POCO M2 Pro** (`miatoll`: curtana, joyeuse, excalibur, gram), Qualcomm
**SM7125** (Snapdragon 720G), Adreno 618.

| | |
| --- | --- |
| Target | iPadOS 17.7.11 (21H461), iPad7,1 / J120AP, XNU 10063.141.1 (arm64; SM7125 has no PAC) |
| SoC layer | [UniXNU-sm7125-common](https://github.com/qdizax-w/UniXNU-sm7125-common) |
| Firmware | [uefi-miatoll](https://github.com/qdizax-w/uefi-miatoll): Mu-Silicium miatollPkg + UniXNU, UniXNUDxe, UniXNURamDiskDxe, DarwinBoot |
| Boot | stock ABL, `fastboot boot boot.img` (RAM only) |

## State

First-console stage: the configuration builds the kernel, payload and boot image; nothing is
verified on the phone yet.

| Area | State |
| --- | --- |
| UEFI -> UniXNU menu -> DarwinBoot -> XNU | built, not yet booted |
| CPUs / GIC / timer | ArmCpu with `armcpu-timer-intid=19` (SM7125 virtual timer is PPI 3) |
| Console | boot-progress panel on the GOP framebuffer |
| Storage (UFS root on userdata) | planned - **wipes Android data**, only with consent |
| Touch (FocalTech FT8756) | planned |
| GPU (Adreno 618) | planned: Adreno740 needs an a6xx (GMU/HFI, CP) port; Turnip already supports A618 |
| Wi-Fi (WCN3990 / ath10k-snoc) | planned: Ath12kWifi does not apply to this chip |
| Cellular (IPA v4.2) | planned: QcomBaseband's IPA v4.2 path matches SM7125 |

## Build

GitHub Actions: set the secret `UNIXNU_UNIQUE_CHIP_ID` (8 hex digits) and run **package**.
Locally, with UniXNU and uefi-miatoll checked out beside this repository on macOS with Xcode:

```sh
scripts/package.sh --os 17 --uefi ../uefi-miatoll
```

## Boot (RAM only)

```sh
fastboot boot boot.img
```

If the phone loops on the Mi logo, the Mu-Silicium base is the suspect: HakiOS found that
releases after Mu-Silicium 3.6 and images built with clang 23 do not boot miatoll.

## Provenance

`package/` and the three `scripts/build-*` kit builders come from UniXNU-rmx1971 / UniXNU-sirius
(the SDM710 ports, the same GIC and timer wiring), renamed for this board. `drivers/ArmCpu` is
UniXNU's ArmCpu plus the `armcpu-timer-intid` boot argument.
