#!/usr/bin/env bash

APP_NAME="git"
MIN_VERSION="9.0.0"
LOG_FILE="$HOME/endpoint-scripting-lab/endpoint-audit.log"

log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') | $1" | tee -a "$LOG_FILE"
}

log_message "Starting endpoint application audit"

if ! command -v "$APP_NAME" >/dev/null 2>&1; then
    log_message "FAIL: $APP_NAME is not installed"
    exit 1
fi

INSTALLED_VERSION=$("$APP_NAME" --version | awk '{print $3}')

log_message "Application: $APP_NAME"
log_message "Installed version: $INSTALLED_VERSION"
log_message "Required version: $MIN_VERSION"

if dpkg --compare-versions "$INSTALLED_VERSION" ge "$MIN_VERSION"; then
    log_message "PASS: Application meets minimum version"
    exit 0
else
    log_message "FAIL: Application is outdated"
    exit 1
fi
