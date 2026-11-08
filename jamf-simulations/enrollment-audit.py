from pathlib import Path
#!/usr/bin/env python3

import csv

with open(Path(__file__).resolve().parent.parent / "sample-data" / "apple-enrollment.csv", newline="") as file:
    devices = list(csv.DictReader(file))

print("APPLE BUSINESS MANAGER / JAMF ENROLLMENT AUDIT")
print("=" * 55)

ready = 0
attention = 0

for device in devices:

    if (
        device["ABMAssigned"] == "Yes"
        and device["MDMServer"] == "JamfPro"
        and device["EnrollmentStatus"] == "Enrolled"
    ):
        ready += 1
        continue

    attention += 1

    if device["ABMAssigned"] != "Yes":
        issue = "Device not assigned in ABM"

    elif device["MDMServer"] != "JamfPro":
        issue = "Assigned to another MDM server"

    else:
        issue = "Jamf enrollment pending"

    print(f"{device['Device']} | {device['Department']} | {issue}")

print("=" * 55)
print(f"Total devices: {len(devices)}")
print(f"Enrolled in Jamf: {ready}")
print(f"Require attention: {attention}")
