#!/usr/bin/env/env python3

logfile = "/var/log/httpd/access_log"

with open(logfile, "r") as f:
    lines = f.readlines()

total_requests = len(lines)

error_404= 0
ip_counter={}

for line in lines:
    ip = line.split()[0]

    if ip in ip_counter:
        ip_counter[ip] += 1
    else:
        ip_counter[ip] =1

    if " 404 " in line:
        error_404 +=1

top_3_ips = sorted(ip_counter.items(),key=lambda x: x[1], reverse=True)[:3]

print(f"Total Requests: {total_requests}")
print(f"404 error : {error_404}")
print("Top 3 IP address: ")
for ip, count in top_3_ips:
    print(f"{ip} -> {count} requests")


