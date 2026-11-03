#!/usr/bin/env python3
"""Firmware preflight: put the boot image's device tree where [bootimg] dtb names it.

The stock miatoll ABL boots Mu-Silicium with the appended device tree Mu-Silicium ships
(Resources/DTBs/miatoll.dtb of the firmware checkout); it carries the msm-id/board-id the ABL
matches and the cont_splash_region the ABL needs to keep the panel lit. This script copies it,
checked, to build/miatoll/miatoll.dtb of the build tree.
"""
import hashlib
import os
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[1]
uefi = os.environ.get('UNIXNU_UEFI')
if not uefi:
    raise SystemExit('UNIXNU_UEFI is not set: run through ./unixnu build firmware --uefi <uefi-miatoll>')
source = Path(uefi) / 'Resources/DTBs/miatoll.dtb'
data = source.read_bytes()
if data[:4] != b'\xd0\x0d\xfe\xed':
    raise SystemExit(f'{source}: not a flattened device tree')
if struct.unpack_from('>I', data, 4)[0] > len(data):
    raise SystemExit(f'{source}: truncated')
if b'cont_splash_region' not in data:
    raise SystemExit(f'{source}: no cont_splash_region; the ABL would power the panel down')
out = ROOT / 'build/miatoll/miatoll.dtb'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(data)
print(f'miatoll dtb: {out} ({len(data)} bytes, sha256 {hashlib.sha256(data).hexdigest()})')
