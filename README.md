# Enterprise Endpoint Management & Automation Lab

## Project Overview

A hands-on endpoint engineering portfolio project demonstrating application detection, version compliance, scripting, endpoint security auditing, software deployment decision logic, and Apple device management concepts.

The project consists of 13 practical exercises developed using Ubuntu WSL2, Bash, Python 3, and synthetic device inventories.

The exercises simulate selected workflows associated with Microsoft Intune, Jamf Pro, and Apple Business Manager.

**Environment:** Windows 11, Ubuntu WSL2, Bash, and Python 3.

**Important:** Jamf Pro and macOS management workflows are simulated. This project does not represent production Jamf Pro administration or actual macOS device enrollment.

---

## Technologies and Skills

- Bash scripting
- Python 3
- Linux / Ubuntu WSL2
- Git and GitHub
- CSV-based device inventories
- Application detection and version validation
- Endpoint compliance and security auditing
- Software deployment decision logic
- Apple Business Manager enrollment concepts
- Jamf Pro Smart Group concepts
- Jamf Pro policy and Self Service simulations
- Microsoft Intune workflow comparisons
- Troubleshooting and technical documentation

---

## Repository Structure

```text
endpoint-management-and-automation-lab/
|
|-- README.md
|-- .gitignore
|
|-- bash-scripting/
|   |-- check-app.sh
|   |-- detect-git.sh
|   |-- validate-git-version.sh
|   |-- endpoint-audit.sh
|   |-- remediate-app.sh
|
|-- macos-simulations/
|   |-- detect-macos-app.sh
|   |-- check-macos-version.sh
|   |-- mock-macos/
|
|-- jamf-simulations/
|   |-- smart-group-simulator.py
|   |-- jamf-policy-simulator.py
|   |-- mac-security-audit.py
|   |-- self-service-simulator.py
|   |-- enrollment-audit.py
|   |-- troubleshoot-enrollment.py
|
|-- sample-data/
|   |-- mac-inventory.csv
|   |-- mac-security-inventory.csv
|   |-- software-catalog.csv
|   |-- apple-enrollment.csv
|   |-- enrollment-troubleshooting.csv
|
|-- docs/
|
|-- evidence/
```

---

## Lab Series

### Labs 01-05: Bash Endpoint Automation

Developed Bash scripts to simulate enterprise application detection, version compliance, audit logging, and remediation assessment.

Key accomplishments:

- Implemented application and directory detection.
- Used shell exit codes to indicate success and failure.
- Validated installed application versions against minimum requirements.
- Generated timestamped audit logs.
- Simulated remediation decisions without modifying installed software.

### Labs 06-07: macOS Application Detection

Created a synthetic macOS-style application bundle to practice application detection and version inspection.

Key accomplishments:

- Simulated application bundle detection.
- Inspected application metadata using Info.plist.
- Validated application version information.
- Tested successful and unsuccessful detection scenarios.

These exercises were performed in Ubuntu WSL2 using synthetic files rather than a physical Mac.

### Lab 08: Jamf Pro Smart Group Simulation

Developed a Python simulation that evaluates device inventory records and identifies endpoints requiring application installation or upgrades.

Results:

- Evaluated 10 synthetic Mac records.
- Identified 2 devices missing the required application.
- Identified 4 devices with outdated application versions.
- Flagged 6 devices requiring attention.

### Lab 09: Jamf Pro Policy Deployment Simulation

Developed a Python simulation to determine which devices should receive application installations or upgrades.

Results:

- Generated 2 simulated installation decisions.
- Generated 4 simulated upgrade decisions.
- Created timestamped deployment audit logs.
- Validated dry-run execution without installing software.

### Lab 10: macOS Security Baseline Audit

Developed a Python security audit to evaluate synthetic devices against three baseline requirements:

- FileVault encryption enabled.
- macOS firewall enabled.
- Screen lock enabled.

Results:

- Total devices evaluated: 10
- Compliant devices: 5
- Noncompliant devices: 5

The simulation identified individual configuration failures for remediation planning.

### Lab 11: Jamf Pro Self Service Simulation

Developed a software catalog simulation to evaluate application eligibility based on departmental assignments and approval status.

Validated scenarios:

- Approved application request.
- Denied request due to department restrictions.
- Denied request for an unapproved application.

All decisions were recorded in a timestamped audit log.

### Lab 12: Apple Business Manager Enrollment Audit

Developed a Python simulation to evaluate device enrollment records and identify potential management issues.

Results:

- Total devices evaluated: 10
- Devices recorded as enrolled in Jamf Pro: 5
- Devices requiring attention: 5

Detected scenarios included:

- Pending enrollment.
- Missing Apple Business Manager assignment.
- Assignment to a legacy MDM server.

### Lab 13: Jamf Pro Enrollment Troubleshooting

Developed a troubleshooting simulation to classify enrollment problems and recommend corrective actions.

Identified five devices requiring investigation.

Simulated issues included:

- Network connectivity failures.
- Missing Apple Business Manager assignments.
- Incorrect MDM server assignments.
- Missing enrollment configurations.

---

## Key Validation Results

| Exercise | Verified Result |
|---|---|
| Bash application detection | Successful detection |
| Application version compliance | PASS and FAIL scenarios |
| Audit logging | Timestamped records |
| Remediation assessment | Dry-run execution |
| macOS application detection | PASS and FAIL scenarios |
| macOS version detection | PASS and FAIL scenarios |
| Smart Group simulation | 6 devices identified |
| Policy deployment simulation | 2 installs and 4 upgrades |
| Security baseline audit | 5 compliant, 5 noncompliant |
| Self Service simulation | 1 approved, 2 denied |
| ABM enrollment audit | 5 enrolled, 5 requiring attention |
| Enrollment troubleshooting | 5 devices flagged |

---

## Running the Simulations

### Requirements

- Python 3
- Bash
- Linux or Ubuntu WSL2

No Jamf Pro tenant, Apple Business Manager account, or physical Mac is required.

### Example: Run the Smart Group Simulation

The Python simulations use synthetic CSV inventories stored in the sample-data directory.

Before running scripts from their new repository locations, their CSV file paths must be updated to reference the sample-data directory.

After path validation, an example command from the repository root will be:

```bash
python3 jamf-simulations/smart-group-simulator.py
```

### Example: Run Bash Application Detection

From the repository root:

```bash
bash bash-scripting/detect-git.sh
```

Some Bash exercises use Linux-specific paths and should be run in a compatible Linux or WSL2 environment.

---

## Microsoft Intune and Jamf Pro Concepts

This project explores transferable concepts between Microsoft Intune and Jamf Pro.

| Microsoft Intune | Jamf Pro Concept |
|---|---|
| Company Portal | Self Service |
| Entra ID group targeting | Smart Groups and policy scoping |
| Win32 application deployment | macOS application package deployment |
| Device configuration policies | Configuration profiles |
| Device compliance policies | Inventory-based compliance evaluation |
| Windows Autopilot | Apple Automated Device Enrollment |
| Intune Management Extension logs | Jamf policy and management logs |

These comparisons illustrate related endpoint management concepts. The products have different architectures, features, and implementation requirements.

---

## Professional Relevance

This project demonstrates transferable technical skills relevant to:

- Endpoint Engineer
- Systems Administrator
- Microsoft Intune Administrator
- Desktop Engineer
- Enterprise IT Support Engineer

It complements professional experience with:

- Microsoft Intune
- Windows Autopilot
- Microsoft Entra ID
- SCCM/MECM
- Apple Business Manager
- Enterprise mobile device management
- Endpoint migrations
- IT service management and troubleshooting

The project also demonstrates continued professional development in Bash scripting, Python automation, and Apple endpoint management concepts.

---

## Future Enhancements

Planned improvements include:

- Automated Python unit tests.
- Improved CSV input validation.
- Portable file path handling.
- Structured logging and error handling.
- Configuration profile examples.
- Additional simulated Jamf Pro policy scenarios.
- Application deployment reporting.
- Expanded macOS troubleshooting exercises.
- GitHub Actions testing.

---

## Project Status

**Initial Lab Series: Completed**

13 hands-on endpoint scripting and management concept exercises completed.

**Portfolio Preparation: In Progress**

Repository organization, documentation, validation, and GitHub publication.

---

## Disclaimer

This is an independent educational portfolio project.

All device inventories and application records are synthetic.

Jamf Pro, Apple Business Manager, and macOS management workflows are represented through simulations rather than live integrations.

The project does not claim production Jamf Pro administration experience or actual deployment to managed macOS devices.
