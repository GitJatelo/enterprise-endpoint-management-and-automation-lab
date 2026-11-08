#!/usr/bin/env bash

APP_PATH="/usr/bin"

echo "Checking application directory..."

if [ -d "$APP_PATH" ]; then
    echo "PASS: Directory exists at $APP_PATH"
    exit 0
else
    echo "FAIL: Directory not found at $APP_PATH"
    exit 1
fi
