#!/bin/bash

LOG_FILE="$HOME/security-lab/logs/security-monitor-$(date +%Y%m%d).log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# TODO: Log start message with timestamp

# TODO: Check authentication logs for failures
# Hint: grep /var/log/auth.log for "authentication failure"

# TODO: Check system logs for errors/warnings
# Hint: grep /var/log/syslog for "error|warning"

# TODO: Check network connections
# Hint: Use netstat -tuln

# TODO: Log completion message
