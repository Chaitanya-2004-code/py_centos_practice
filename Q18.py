#!/usr/bin/env python3
import subprocess as sp

subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")
base = subnet.split(".")[:3]
prefix = ".".join(base)

print("=== Live Hosts ===")
for i in range(1, 255):
    ip = f"{prefix}.{i}"
    result = sp.getoutput(f"ping -c 1 -W 1 {ip}")
    if "1 received" in result or "bytes from" in result:
        print(ip)
