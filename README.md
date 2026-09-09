# Atria iOS 17
Unofficial port of Atria to iOS 17 versions.

iOS 18-26 currently not supported, will crash to safe-mode.

Open this in browser to add my repo: https://s-gdn.github.io/repo.html

## Building

This fork includes a GitHub Actions workflow for building Atria
using Theos on a macOS runner.

To build your own copy:

1. Fork this repository.
2. Open the Actions tab and enable workflows.
3. Run the build workflow.
4. Download the generated `.deb` from the workflow artifacts.

The resulting package is intended for rootless / roothide jailbreaks.
Compatibility has only been confirmed on iOS 17.1.1 - 17.3.1
