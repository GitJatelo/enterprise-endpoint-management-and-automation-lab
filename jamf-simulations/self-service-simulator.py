from pathlib import Path
#!/usr/bin/env python3

import csv
from datetime import datetime

DEVICE = "MAC002"
DEPARTMENT = "Design"
REQUESTED_APP = "UnknownApp"

with open(Path(__file__).resolve().parent.parent / "sample-data" / "software-catalog.csv", newline="") as file:
    catalog = list(csv.DictReader(file))

print("JAMF SELF SERVICE SIMULATION")
print("=" * 40)

app = next(
    (item for item in catalog if item["App"] == REQUESTED_APP),
    None
)

if app is None:
    result = "DENIED: Application not found"

elif app["Approved"] != "Yes":
    result = "DENIED: Application not approved"

elif app["Department"] not in (DEPARTMENT, "All"):
    result = "DENIED: Department not authorized"

else:
    result = f"APPROVED: Would deploy {REQUESTED_APP} {app['Version']}"

message = (
    f"{datetime.now():%Y-%m-%d %H:%M:%S} | "
    f"{DEVICE} | {DEPARTMENT} | {result} | DRY RUN"
)

print(message)

with open("self-service.log", "a") as log:
    log.write(message + "\n")
