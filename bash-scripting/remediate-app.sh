#!/usr/bin/env bash

APP_NAME="git"
MIN_VERSION="2.40.0"
LOG_FILE="$HOME/endpoint-scripting-lab/remediation.log"

log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') | $1" | tee -a "$LOG_FILE"
}

log_message "Starting endpoint remediation assessment"

if ! command -v "$APP_NAME" >/dev/null 2>&1; then
    log_message "FAIL: Application is not installed"
    exit 1
fi

INSTALLED_VERSION=$("$APP_NAME" --version | awk '{print $3}')

log_message "Installed version: $INSTALLED_VERSION"
log_message "Required version: $MIN_VERSION"

if dpkg --compare-versions "$INSTALLED_VERSION" ge "$MIN_VERSION"; then
    log_message "PASS: No remediation required"
    exit 0
else
    log_message "NONCOMPLIANT: Application version below requirement"
    log_message "DRY RUN: Would schedule an approved application update"
    log_message "No software changes performed"
    exit 2
fi
