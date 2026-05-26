#!/usr/bin/env python3

logfile = "/var/log/secure"

with open(logfile, "r") as f:
    lines = f.readlines()

failed_attempts= {}

for line in lines:
    if "Failed password" in line:
        parts = line.split()
        ip = parts[-4]
        if ip in failed_attempts:
            failed_attempts[ip] +=1

        else:
            failed_attempts[ip]=1

for ip,count in failed_attempts.items():
    if count > 3:
        print(f"Suspicious IP : {ip} ({count}) failed attempts")

