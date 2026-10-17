# SSH Brute-Force Detection Using Wazuh SIEM

## Project Overview

This project documents a hands-on security monitoring lab using Kali Linux, Windows security events, and Wazuh SIEM.

The objective is to investigate repeated SSH authentication failures, examine Windows authentication events, understand Wazuh detection rules, and document the workflow from a SOC analyst's perspective.

## Objectives

- Understand Windows authentication-failure events.
- Generate controlled SSH login test attempts from Kali Linux against my lab target.
- Investigate security alerts in Wazuh Threat Hunting.
- Examine Wazuh rules and severity levels.
- Document findings and identify areas for improving detection.

## Lab Environment

- **SIEM:** Wazuh
- **Attack simulation system:** Kali Linux
- **Monitored endpoint:** Windows
- **Log source:** Windows security events collected by the Wazuh agent
- **Testing method:** Python-based SSH login testing in an authorized lab

## Investigation Workflow

1. Configure Wazuh monitoring for the Windows endpoint.
2. Perform SSH login testing from Kali Linux in the lab.
3. Review authentication-failure events in Wazuh Threat Hunting.
4. Inspect Wazuh rule 60122, which identifies Windows logon failures.
5. Review related authentication events and the dashboard overview.
6. Capture screenshots and document the results.

## Evidence
Video Demonstration

Kali Linux SSH Authentication Testing

Watch the project demonstration- https://drive.google.com/drive/folders/1NUYLyjhUt5QE2gUHveS8JDMeqCUOS2Ts?usp=sharing

The recording demonstrates SSH authentication testing in the lab environment. Wazuh alert correlation is documented separately in the project findings.

### 1. Wazuh Service Logon Rule
![Wazuh service logon rule](screenshots/01-wazuh-rule-67024-service-logon.png)

Inspection of rule 67024, related to a Windows service-logon event.

### 2. Windows Authentication-Failure Events
![Authentication failure events](screenshots/02-wazuh-authentication-failure-events.png)

Threat Hunting view displaying Windows endpoint events, including repeated logon failures.

### 3. Wazuh Logon-Failure Rule
![Wazuh logon failure rule](screenshots/03-wazuh-rule-60122-logon-failure.png)

Inspection of rule 60122, level 5, used to identify Windows logon failures.

### 4. Wazuh Threat Hunting Overview
![Threat Hunting overview](screenshots/04-wazuh-threat-hunting-overview.png)

Dashboard overview showing authentication failures and successful authentications for the selected time range.

### 5. Kali Linux Test Recording

See `evidence/kali-ssh-login-test.mp4` for the SSH login testing demonstration.

## Findings

- Wazuh received and displayed Windows authentication-related events.
- Rule 60122 identifies Windows logon failures.
- Threat Hunting provides a searchable view of collected security events.
- Authentication failures are useful indicators for investigating possible brute-force activity.
- Repeated failures alone do not prove a brute-force attack; event correlation, timestamps, source information, and testing context are important.

## Detection Validation Status

The available screenshots demonstrate authentication-event visibility and rule investigation. They do not independently confirm that a custom brute-force correlation rule triggered on the Kali test attempts. That result requires separate validation.

## Skills Demonstrated

- SIEM monitoring and alert investigation
- Windows authentication-event analysis
- Wazuh rule inspection
- Linux command-line usage
- Security testing in a lab environment
- Evidence collection and technical documentation

## Disclaimer

This project was conducted for educational purposes in an authorized lab environment. Testing should only be performed against systems for which permission has been granted.
