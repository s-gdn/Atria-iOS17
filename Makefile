export THEOS_PACKAGE_SCHEME = rootless
TARGET = iphone:clang:16.5:15.0
ARCHS = arm64 arm64e
INSTALL_TARGET_PROCESSES = SpringBoard

include $(THEOS)/makefiles/common.mk

TWEAK_NAME = Atria
Atria_FILES = $(shell find src -type f \( -name '*.m' -o -name '*.xm' \) ! -name 'AtriaDiagnostic.xm')
Atria_CFLAGS = -fobjc-arc -Wno-deprecated-declarations
Atria_FRAMEWORKS = Foundation UIKit CoreText QuartzCore
Atria_LIBRARIES = substrate

include $(THEOS_MAKE_PATH)/tweak.mk
SUBPROJECTS += Prefs
include $(THEOS_MAKE_PATH)/aggregate.mk
