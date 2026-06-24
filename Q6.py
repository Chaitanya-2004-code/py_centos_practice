#!/usr/bin/env python3
import subprocess as sp

# Run netstat to list TCP connections
output = sp.getoutput("netstat -tn 2>/dev/null | grep ESTABLISHED")

ip_counts = {}

for line in output.splitlines():
    parts = line.split()
    if len(parts) < 5:
        continue
    remote_ip_port = parts[4]   # Remote address:port
    remote_ip = remote_ip_port.split(":")[0]
    ip_counts[remote_ip] = ip_counts.get(remote_ip, 0) + 1

print("=== Active ESTABLISHED Connections ===")
for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{ip} -> {count} connections")
