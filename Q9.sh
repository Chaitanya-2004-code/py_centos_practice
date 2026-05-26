#!/bin/bash
echo "last 10 failed login attempts:"
grep "failed" /var/log/secure | tail -n 10
