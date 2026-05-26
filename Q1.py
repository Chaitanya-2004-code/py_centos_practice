#!/usr/bin/env python3
import socket

target = input("Enter the hostname or IP : ")

ip = socket.gethostbyname(target)

print(f"\nScanning {target}  ({ip}) . . . \n")

# port scan 1-1025

for port in range(1,1025):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((ip, port))
    if result == 0:
        service = socket.getservbyport(port, "tcp") if port in range(1,1025) else "unknown"
        print(f"port {port} OPEN -> {service}")

    s.close()
