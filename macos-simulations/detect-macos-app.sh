#!/usr/bin/env bash

APP_NAME="ExampleApp"
APP_PATH="$HOME/endpoint-scripting-lab/mock-macos/Applications/${APP_NAME}.app"

echo "Checking macOS-style application bundle..."

if [ -d "$APP_PATH" ]; then
    echo "PASS: $APP_NAME application bundle detected"
    echo "Path: $APP_PATH"
    exit 0
else
    echo "FAIL: $APP_NAME application bundle not found"
    exit 1
fi
