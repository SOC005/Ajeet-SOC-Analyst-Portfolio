# RDP Brute-Force Detection & Investigation Using Splunk

## Project Overview

This project demonstrates the investigation and detection of suspected RDP brute-force activity using Splunk Enterprise and Sysmon network connection logs.

## Objective

- Ingest security telemetry into Splunk
- Investigate RDP connection activity
- Identify suspicious source IP addresses
- Count repeated RDP connection attempts
- Identify the targeted host and service
- Build a Splunk detection rule
- Configure a Splunk alert
- Document the incident using SOC investigation methodology

## Tools & Technologies

- Splunk Enterprise 10.6
- Sysmon
- Splunk SPL
- Windows security telemetry
- MITRE ATT&CK

## Investigation Findings

| Field | Finding |
|---|---|
| Source IP | 23.93.242.200 |
| Destination IP | 10.0.1.14 |
| Destination Port | 3389 |
| Protocol/Service | RDP |
| Attempts | 23 |
| Activity Duration | Approximately 5 minutes 35 seconds |
| MITRE ATT&CK | T1110.001 – Password Guessing |

## Detection Logic

The investigation identifies repeated RDP connection attempts from the same source IP.

```spl
index=rdp_lab
| rex field=_raw "(?i)SourceIp[^>]*>\s*(?<src_ip>[^<]+)"
| rex field=_raw "(?i)DestinationPort[^>]*>\s*(?<dest_port>[^<]+)"
| stats count as attempts by src_ip dest_port
| where dest_port="3389" AND attempts>10
```

## Result

The detection identified:

- Source IP: 23.93.242.200
- Destination: 10.0.1.14
- RDP port: 3389
- Attempts: 23

## Investigation Conclusion

The available Sysmon network telemetry indicates repeated RDP connection attempts consistent with suspected brute-force activity.

The dataset does not contain Windows Security authentication events such as Event ID 4624 or 4625. Therefore, successful or failed authentication cannot be confirmed from this dataset alone.

## Recommended SOC Response

1. Investigate the source IP and related indicators.
2. Review Windows authentication logs on the targeted host.
3. Check for successful RDP logons.
4. Review the target host for signs of compromise.
5. Block or contain the source where appropriate according to organizational policy.
6. Continue monitoring for related activity.

## MITRE ATT&CK

**T1110.001 – Password Guessing**

## Evidence

Screenshots of Splunk searches, detection results, alert configuration and dashboard are included in this repository.

## Disclaimer

This project uses a security research dataset in a controlled lab environment. The IP addresses and activity shown are part of the dataset and should not be interpreted as evidence of a real-world incident.
