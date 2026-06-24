#!/usr/bin/env python3
import os
import hashlib
import json
import subprocess as sp   # system tasks

# Directory to monitor
MONITOR_DIR = "/path/to/monitor"
HASH_FILE = "file_hashes.json"

def hash_file(filepath):
    """Return SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

# --- Step 1: Load previous hashes ---
if os.path.exists(HASH_FILE):
    with open(HASH_FILE, "r") as f:
        old_hashes = json.load(f)
else:
    old_hashes = {}

# --- Step 2: Generate current hashes ---
new_hashes = {}
for root, dirs, files in os.walk(MONITOR_DIR):
    for filename in files:
        filepath = os.path.join(root, filename)
        new_hashes[filepath] = hash_file(filepath)

# --- Step 3: Compare old vs new ---
modified = []
new_files = []
deleted = []

for filepath, old_hash in old_hashes.items():
    if filepath not in new_hashes:
        deleted.append(filepath)
    elif new_hashes[filepath] != old_hash:
        modified.append(filepath)

for filepath in new_hashes:
    if filepath not in old_hashes:
        new_files.append(filepath)

# --- Step 4: Report changes ---
print("=== File Integrity Report ===")
if modified:
    print("Modified files:")
    for f in modified:
        print(" -", f)
if new_files:
    print("New files:")
    for f in new_files:
        print(" -", f)
if deleted:
    print("Deleted files:")
    for f in deleted:
        print(" -", f)

if not (modified or new_files or deleted):
    print("No changes detected.")

# --- Step 5: Save current hashes ---
with open(HASH_FILE, "w") as f:
    json.dump(new_hashes, f, indent=4)

# --- Step 6: System task logging (optional) ---
sp.getoutput(f'echo "$(date): Integrity check completed" >> /var/log/file_integrity.log')
