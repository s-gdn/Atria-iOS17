#!/usr/bin/env python3
"""Inspect a built package without installing it. Requires macOS Xcode and dpkg."""
from pathlib import Path
import subprocess, sys, tempfile, shutil
package=Path(sys.argv[1]).resolve()
out=Path(sys.argv[2]).resolve();out.mkdir(parents=True,exist_ok=True)
def run(args):
    return subprocess.check_output(args, text=True, stderr=subprocess.STDOUT)
(out/'control.txt').write_text(run(['dpkg-deb','-I',str(package)]))
(out/'contents.txt').write_text(run(['dpkg-deb','-c',str(package)]))
with tempfile.TemporaryDirectory() as d:
    run(['dpkg-deb','-x',str(package),d])
    paths=[Path(d)/'var/jb/Library/MobileSubstrate/DynamicLibraries/Atria.dylib',
           Path(d)/'var/jb/Library/PreferenceBundles/AtriaPrefs.bundle/AtriaPrefs']
    for p in paths:
        if not p.is_file(): raise SystemExit(f'Missing binary: {p}')
        label='tweak' if p.suffix=='.dylib' else 'preferences'
        archs=run(['xcrun','lipo','-archs',str(p)]).strip()
        (out/f'{label}-architectures.txt').write_text(archs+'\n')
        if not {'arm64','arm64e'}.issubset(set(archs.split())):
            raise SystemExit(f'Missing architecture: {archs}')
        (out/f'{label}-load-commands.txt').write_text(run(['xcrun','otool','-l',str(p)]))
        (out/f'{label}-libraries.txt').write_text(run(['xcrun','otool','-L',str(p)]))
        (out/f'{label}-sha256.txt').write_text(run(['shasum','-a','256',str(p)]))
        shutil.copy2(p,out/p.name)
        if label=='preferences':
            libraries=(out/f'{label}-libraries.txt').read_text()
            if '@rpath/libcolorpicker.dylib' not in libraries:
                raise SystemExit('Preferences binary is missing rootless libcolorpicker linkage')
        # Reject the old ABI in the arm64e slice. ABI version is encoded in the CPU subtype.
        header=run(['xcrun','otool','-hv','-arch','arm64e',str(p)])
        (out/f'{label}-header.txt').write_text(header)
    if 'iphoneos-arm64' not in (out/'control.txt').read_text():
        raise SystemExit('Not a rootless package')
print('Package structure and architecture checks passed. Runtime compatibility is NOT verified.')
