#!/bin/bash

LOG_FILE="$HOME/security-lab/logs/realtime-monitor.log"
ALERT_FILE="$HOME/security-lab/logs/security-alerts.log"

# TODO: Create log_event() function
# Format: [timestamp] message

log_event() {
    # TODO: Implement logging with timestamp
}

# TODO: Create create_alert() function
# Format: [timestamp] ALERT: message

create_alert() {
    # TODO: Implement alert logging
}

# TODO: Create monitor_auth() function
# Monitor /var/log/auth.log in real-time
# Alert on authentication failures and invalid users

monitor_auth() {
    # TODO: Use tail -f /var/log/auth.log
    # TODO: Pipe to while read loop
    # TODO: Check for "authentication failure" and "invalid user"
}

# TODO: Create monitor_system() function
# Monitor /var/log/syslog in real-time
# Alert on errors and critical events

monitor_system() {
    # TODO: Use tail -f /var/log/syslog
    # TODO: Check for "error|critical|emergency"
}

# TODO: Start both monitoring functions in background
# TODO: Add main loop to check system load every 10 seconds
