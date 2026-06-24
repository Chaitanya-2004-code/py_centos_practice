#!/usr/bin/env python3
import requests, time

urls = input("Enter URLs (comma separated): ").split(",")

for url in urls:
    url = url.strip()
    start = time.time()
    try:
        r = requests.get(url, timeout=5)
        elapsed = round(time.time() - start, 3)
        print(f"{url} -> Status: {r.status_code}, Response time: {elapsed}s")
    except Exception as e:
        print(f"{url} -> Error: {e}")
