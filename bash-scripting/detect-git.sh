#!/usr/bin/env bash

APP_NAME="git"

echo "Checking installation of $APP_NAME..."

if command -v "$APP_NAME" >/dev/null 2>&1; then
    APP_PATH=$(command -v "$APP_NAME")
    APP_VERSION=$("$APP_NAME" --version)

    echo "PASS: $APP_NAME is installed"
    echo "Location: $APP_PATH"
    echo "Version: $APP_VERSION"

    exit 0
else
    echo "FAIL: $APP_NAME is not installed"
    exit 1
fi
