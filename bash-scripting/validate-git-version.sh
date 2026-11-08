#!/usr/bin/env bash

APP_NAME="git"
MIN_VERSION="9.0.0"

echo "Checking $APP_NAME version compliance..."

if ! command -v "$APP_NAME" >/dev/null 2>&1; then
    echo "FAIL: $APP_NAME is not installed"
    exit 1
fi

INSTALLED_VERSION=$(git --version | awk '{print $3}')

echo "Installed version: $INSTALLED_VERSION"
echo "Required version:  $MIN_VERSION"

if dpkg --compare-versions "$INSTALLED_VERSION" ge "$MIN_VERSION"; then
    echo "PASS: Application meets minimum version"
    exit 0
else
    echo "FAIL: Application version is outdated"
    exit 1
fi
