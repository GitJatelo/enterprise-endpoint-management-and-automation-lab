from pathlib import Path
#!/usr/bin/env python3

import csv
from datetime import datetime

MIN_VERSION = (2, 4, 0)
TARGET_VERSION = "2.5.0"

def parse_version(version):
    return tuple(int(part) for part in version.split("."))

with open(Path(__file__).resolve().parent.parent / "sample-data" / "mac-inventory.csv", newline="") as file:
    devices = list(csv.DictReader(file))

print("JAMF POLICY DEPLOYMENT SIMULATION")
print("=" * 45)

with open("jamf-policy-results.log", "a") as log:
    for device in devices:
        installed = device["AppInstalled"] == "Yes"

        needs_deployment = (
            not installed
            or parse_version(device["AppVersion"]) < MIN_VERSION
        )

        if needs_deployment:
            action = "INSTALL" if not installed else "UPGRADE"

            message = (
                f"{datetime.now():%Y-%m-%d %H:%M:%S} | "
                f"{device['Device']} | "
                f"{device['Department']} | "
                f"{action} ExampleApp {TARGET_VERSION} | "
                f"DRY RUN"
            )

            print(message)
            log.write(message + "\n")
