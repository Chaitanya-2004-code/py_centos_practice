#!/bin/bash
echo "Cron jobs for use $USER"
crontab -l

read -p "Enter the command/job to very: " job

crontab -l > /tmp/cron_jobs.txt

python3 <<EOF
job_chk = "$job"
with open("/tmp/cron_jobs.txt") as f:
	jobs = f.read().splitlines()

if any(job_chk in line for line in jobs):
	print(f" job Exist : {job_chk}")
else:
	print("not found")
EOF

rm /tmp/cron_jobs.txt
