#!/usr/bin/env python3
import os, tarfile, time

SOURCE_DIR = "/path/to/source"
BACKUP_DIR = "/backup"

if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

timestamp = time.strftime("%Y%m%d-%H%M%S")
backup_file = os.path.join(BACKUP_DIR, f"backup-{timestamp}.tar.gz")

# Create compressed backup
with tarfile.open(backup_file, "w:gz") as tar:
    tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR))

print(f"Backup created: {backup_file}")

# Keep only last 5 backups
backups = sorted([f for f in os.listdir(BACKUP_DIR) if f.endswith(".tar.gz")])
while len(backups) > 5:
    old = backups.pop(0)
    os.remove(os.path.join(BACKUP_DIR, old))
    print(f"Removed old backup: {old}")
