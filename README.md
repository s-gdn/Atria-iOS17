# Atria iOS 17 baseline build kit

This kit is intended for a fresh checkout of ren7995/Atria. It is a new, untested build configuration, not the original developer's missing Makefiles and not a verified source-to-binary reproduction. The user-provided official rootless 1.4.1 package is the known-working reference.

## Preparation

1. Preserve the existing modified WSL tree. Clone the original repository into a NEW directory and record its commit SHA.
2. Copy this kit's contents into that clean checkout, retaining the original src, Prefs/src, resources and injection filter.
3. Run `python3 tools/apply-build-fixes.py`. Inspect `git diff --check` and `git diff`. Do not copy AtriaDiagnostic.xm or other experimental files.
4. Commit the build configuration and the small initializer fixes separately if desired.
5. Create a private GitHub repository, push the baseline branch, and run the workflow manually from Actions.

## Build design

- macOS 15 / Xcode 16.4; native new-ABI arm64e, no allemande or oldabi.
- Theos and the patched 16.5 SDK are obtained in an isolated runner directory.
- The official rootless package's arm64/arm64e architecture set, SpringBoard filter, package identifier, dependency list, and Preferences libcolorpicker linkage are used as reference requirements.
- Original Objective-C implementation files and all eight Logos hook files are compiled. No runtime hooks are intentionally removed.
- The only source fix provided is for C++ narrowing and initializer order. Deprecated UIKit declarations are warnings rather than rewriting runtime behaviour merely to compile.
- PACKAGE_VERSION and PACKAGE_TYPE are supplied by a local header without editing the original Preferences source.
- The output version is 1.4.1-17baseline1, so it cannot be confused with the official release.

## Important limitations

The full original source tree and missing original build files were not available to the kit generator. This configuration is reconstructed from the user's source tree, compiler errors, and uploaded official package. It has not been executed on GitHub Actions or tested on an iPhone. A successful CI build is not a safety guarantee. Do not install the artifact until its contents and runtime changes have been reviewed. Preserve the working official package and a no-injection recovery method.

If the build fails, collect the FIRST compiler or linker error and the relevant source. Do not add broad ABI compatibility dependencies or modify global Theos rules to get past it.
