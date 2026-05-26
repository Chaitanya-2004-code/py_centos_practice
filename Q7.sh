#!/bin/bash

usage=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')


	echo "$(date): Warning - Disk usage is ${usage}% on /" >> /var/log/disk_alert.log
fi
