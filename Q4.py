#!/usr/bin/env python3

import subprocess
domain = input("Enter the domain name : ")
ip_res = subprocess.getoutput(f"host -t A {domain}")
ip = ip_res.split()[-1]

rev=subprocess.getoutput(f"host -t PTR {ip}")
rev_ip=rev.split()[-1]
print(rev,rev_ip)
print(f"Domain {domain}")
print(f" IP Add is {ip}")
print(f"Reverser DNS: {rev_ip}")

