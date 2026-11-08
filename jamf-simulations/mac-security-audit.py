from pathlib import Path
#!/usr/bin/env python3

import csv

REQUIRED_SETTINGS = ["FileVault", "Firewall", "ScreenLock"]

with open(Path(__file__).resolve().parent.parent / "sample-data" / "mac-security-inventory.csv", newline="") as file:
    devices = list(csv.DictReader(file))

print("MACOS SECURITY BASELINE AUDIT")
print("=" * 45)

compliant = 0
noncompliant = 0

for device in devices:
    failures = [
        setting
        for setting in REQUIRED_SETTINGS
        if device[setting] != "Enabled"
    ]

    if failures:
        noncompliant += 1
        print(
            f"{device['Device']} | NONCOMPLIANT | "
            f"Missing: {', '.join(failures)}"
        )
    else:
        compliant += 1

print("=" * 45)
print(f"Total devices: {len(devices)}")
print(f"Compliant: {compliant}")
print(f"Noncompliant: {noncompliant}")
