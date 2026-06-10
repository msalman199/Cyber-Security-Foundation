#!/bin/bash

# Cron Job Monitoring Script
# Lab 4 - Bash Scripting Essentials

echo "Cron Job Monitoring Dashboard"
echo "============================="

# Display current cron jobs
echo ""
echo "Current Cron Jobs:"
echo "------------------"
crontab -l | grep -v "^#" | grep -v "^$" || echo "No active cron jobs found"

# Check cron service status
echo ""
echo "Cron Service Status:"
echo "-------------------"
if systemctl is-active --quiet cron; then
    echo "✓ Cron service is running"
else
    echo "✗ Cron service is not running"
fi

# Display recent cron logs (if available)
echo ""
echo "Recent Cron Activity:"
echo "--------------------"
if [ -f "/var/log/cron" ]; then
    tail -10 /var/log/cron
elif [ -f "/var/log/syslog" ]; then
    grep -i cron /var/log/syslog | tail -10
else
    echo "Cron logs not accessible or not found"
fi

# Display our custom log files
echo ""
echo "Custom Backup Logs:"
echo "------------------"
if [ -f "$HOME/cron_backup.log" ]; then
    echo "Last 5 backup log entries:"
    tail -5 "$HOME/cron_backup.log"
else
    echo "No backup logs found yet"
fi

# Display backup directory status
echo ""
echo "Backup Directory Status:"
echo "-----------------------"
if [ -d "$HOME/scheduled_backups" ]; then
    backup_count=$(ls -1 "$HOME/scheduled_backups" | wc -l)
    echo "Number of backups: $backup_count"
    
    if [ "$backup_count" -gt 0 ]; then
        echo "Recent backups:"
        ls -lt "$HOME/scheduled_backups" | head -5
    fi
else
    echo "No scheduled backups directory found"
fi

# Check disk usage
echo ""
echo "Disk Usage Summary:"
echo "------------------"
df -h "$HOME" | tail -1

echo ""
echo "Monitoring complete!"
