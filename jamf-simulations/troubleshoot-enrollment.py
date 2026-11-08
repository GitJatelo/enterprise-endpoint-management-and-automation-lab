from pathlib import Path
#!/usr/bin/env python3

import csv

with open(Path(__file__).resolve().parent.parent / "sample-data" / "enrollment-troubleshooting.csv", newline="") as file:
    devices = list(csv.DictReader(file))

print("JAMF ENROLLMENT TROUBLESHOOTING")
print("=" * 55)

issues = 0

for device in devices:

    if (
        device["ABMAssigned"] == "Yes"
        and device["MDMServer"] == "JamfPro"
        and device["NetworkReachable"] == "Yes"
        and device["EnrollmentProfile"] == "Assigned"
        and device["EnrollmentStatus"] == "Enrolled"
    ):
        continue

    issues += 1

    if device["ABMAssigned"] != "Yes":
        diagnosis = "Missing ABM assignment"
        action = "Verify device assignment in Apple Business Manager"

    elif device["MDMServer"] != "JamfPro":
        diagnosis = "Incorrect MDM server"
        action = "Review MDM assignment and approved migration plan"

    elif device["NetworkReachable"] != "Yes":
        diagnosis = "Network connectivity failure"
        action = "Verify DNS, internet access, and required Apple/Jamf endpoints"

    elif device["EnrollmentProfile"] != "Assigned":
        diagnosis = "Enrollment configuration missing"
        action = "Verify Automated Device Enrollment configuration in Jamf"

    else:
        diagnosis = "Enrollment incomplete"
        action = "Investigate Setup Assistant and enrollment logs"

    print(f"\nDevice: {device['Device']}")
    print(f"Diagnosis: {diagnosis}")
    print(f"Recommended action: {action}")

print("\n" + "=" * 55)
print(f"Total devices: {len(devices)}")
print(f"Devices requiring investigation: {issues}")
