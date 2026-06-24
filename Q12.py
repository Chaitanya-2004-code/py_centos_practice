#!/usr/bin/env python3

ports = input("Enter ports (comma separated): ").split(",")

print("=== Generated iptables Rules ===")
for port in ports:
    port = port.strip()
    if port.isdigit():
        print(f"iptables -A INPUT -p tcp --dport {port} -j ACCEPT")
