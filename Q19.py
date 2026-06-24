#!/usr/bin/env python3
import subprocess as sp

output = sp.getoutput("netstat -tulpn 2>/dev/null")

print("=== Process + Port Mapping ===")
for line in output.splitlines()[2:]:
    parts = line.split()
    if len(parts) >= 7:
        proto = parts[0]
        local = parts[3]
        pid_proc = parts[6]
        print(f"{pid_proc} -> {local} ({proto})")
