#!/bin/bash

logfile="/var/log/service_monitor.log"
services=("sshd" "nginx" "httpd" "mysql")
for service in "${services[@]}"; do
	systemctl is-active --quiet $service
	if [ $? -ne 0 ]; then
		systemctl restart $service
		echo "$(date): $service was stopped. Restarted." >> $logfile
	fi
done
