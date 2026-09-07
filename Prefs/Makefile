TARGET = iphone:clang:16.5:15.0
ARCHS = arm64 arm64e

include $(THEOS)/makefiles/common.mk

BUNDLE_NAME = AtriaPrefs
AtriaPrefs_FILES = $(shell find src -type f -name '*.m')
AtriaPrefs_CFLAGS = -fobjc-arc -Wno-deprecated-declarations -include $(CURDIR)/BuildInfo.h
AtriaPrefs_FRAMEWORKS = Foundation UIKit
AtriaPrefs_PRIVATE_FRAMEWORKS = Preferences
AtriaPrefs_LIBRARIES = colorpicker
AtriaPrefs_INSTALL_PATH = /Library/PreferenceBundles
AtriaPrefs_RESOURCE_DIRS = Resources

include $(THEOS_MAKE_PATH)/bundle.mk
