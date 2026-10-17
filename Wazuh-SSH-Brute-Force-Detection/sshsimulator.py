#!/usr/bin/env python3
import subprocess
import getpass

target_ip = input("Windows target IP: ").strip()
username = input("Windows SSH username: ").strip()
attempts = 50

if not target_ip or not username:
    raise SystemExit("IP and username are required.")

for i in range(1, attempts + 1):
    print(f"\nTest {i}/{attempts}")
    print("Enter an intentionally incorrect password for your lab account.")

    result = subprocess.run([
        "ssh",
        "-o", "NumberOfPasswordPrompts=1",
        "-o", "ConnectTimeout=5",
        "-o", "PreferredAuthentications=password",
        "-o", "PubkeyAuthentication=no",
        f"{username}@{target_ip}"
    ])

    if result.returncode == 0:
        print("Authentication succeeded. Stopping.")
        break

print("\nCheck Wazuh for the corresponding Windows authentication events.")