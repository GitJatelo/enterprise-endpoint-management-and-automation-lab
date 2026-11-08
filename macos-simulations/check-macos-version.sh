#!/usr/bin/env bash

APP_PATH="$HOME/endpoint-scripting-lab/mock-macos/Applications/ExampleApp.app"
PLIST_FILE="$APP_PATH/Contents/Info.plist"

echo "Checking ExampleApp version..."

if [ ! -f "$PLIST_FILE" ]; then
    echo "FAIL: Info.plist not found"
    exit 1
fi

VERSION=$(python3 - "$PLIST_FILE" <<'PY'
import plistlib
import sys

with open(sys.argv[1], "rb") as f:
    data = plistlib.load(f)

print(data.get("CFBundleShortVersionString", "Unknown"))
PY
)

if [ "$VERSION" = "Unknown" ]; then
    echo "FAIL: Application version not found"
    exit 1
fi

echo "PASS: ExampleApp detected"
echo "Version: $VERSION"
exit 0
