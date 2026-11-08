from pathlib import Path
#!/usr/bin/env python3

import csv

MIN_VERSION = (2, 4, 0)

def parse_version(version):
    return tuple(int(part) for part in version.split("."))

with open(Path(__file__).resolve().parent.parent / "sample-data" / "mac-inventory.csv", newline="") as file:
    devices = list(csv.DictReader(file))

print("JAMF SMART GROUP SIMULATION")
print("=" * 35)

for device in devices:
    installed = device["AppInstalled"] == "Yes"

    outdated = (
        installed
        and parse_version(device["AppVersion"]) < MIN_VERSION
    )

    if not installed or outdated:
        print(
            f"{device['Device']} | "
            f"{device['Department']} | "
            f"Installed: {device['AppInstalled']} | "
            f"Version: {device['AppVersion']}"
        )
