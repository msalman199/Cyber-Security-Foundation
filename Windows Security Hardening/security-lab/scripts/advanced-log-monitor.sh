#!/bin/bash

REPORT_FILE="$HOME/security-lab/logs/security-analysis-$(date +%Y%m%d-%H%M).log"

# TODO: Create function analyze_auth_logs()
# Count failed and successful logins
# Display recent failed attempts

analyze_auth_logs() {
    # TODO: Count failed login attempts
    # Hint: grep "authentication failure" /var/log/auth.log | wc -l
    
    # TODO: Count successful logins
    # Hint: grep "session opened" /var/log/auth.log | wc -l
    
    # TODO: Show last 5 failed attempts
}

# TODO: Create function analyze_system_logs()
# Count errors and warnings
# Show critical events

analyze_system_logs() {
    # TODO: Count system errors
    # TODO: Count system warnings
    # TODO: Display recent critical events
}

# TODO: Create function analyze_processes()
# Show top CPU processes
# List listening network services

analyze_processes() {
    # TODO: Use ps aux --sort=-%cpu
    # TODO: Use netstat -tuln | grep LISTEN
}

# TODO: Create function analyze_disk_usage()
# Show disk usage
# Alert on partitions >90% full

analyze_disk_usage() {
    # TODO: Use df -h
    # TODO: Use awk to filter partitions >90%
}

# TODO: Call all analysis functions
# TODO: Generate summary report
