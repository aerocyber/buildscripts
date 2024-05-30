#!/usr/bin/bash

ARCH=$(arch)

# read -p "ENTER PLATFORM: "  SITEMARKER_PLATFORM
read -p "ENTER VERSION: " VERSION
read -p "ENTER BUILD NUMBER: " BUILDNO

cd sitemarker
# flutter build $SITEMARKER_PLATFORM --release --tree-shake-icons --build-name $VERSION --build-number $BUILDNO --split-debug-info $VERSION-$SITEMARKER_PLATFORM-DEBUGINFO --no-obfuscate
flutter build linux --release --tree-shake-icons --build-name $VERSION --build-number $BUILDNO --split-debug-info $VERSION-$SITEMARKER_PLATFORM-DEBUGINFO --no-obfuscate

cp -r build/linux/x64/release/bundle/ ..
mv ../bundle ../sitemarker-$VERSION-$ARCH-$SITEMARKER_PLATFORM

cd ../sitemarker-$VERSION-$ARCH-$SITEMARKER_PLATFORM/lib
patchelf --set-rpath '$ORIGIN' liburl_launcher_linux_plugin.so
patchelf --set-rpath '$ORIGIN' libsqlite3_flutter_libs_plugin.so

cd ../..
tar --create --file sitemarker-$VERSION-$ARCH-$SITEMARKER_PLATFORM.tar.gz sitemarker-$VERSION-$ARCH-$SITEMARKER_PLATFORM
