#!/usr/bin/env python3
import re

text = """Sample text with email test@example.com, IP 192.168.1.10, and URL http://example.com"""

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)
urls = re.findall(r"https?://[^\s]+", text)

print("Emails:", emails)
print("IPs:", ips)
print("URLs:", urls)
