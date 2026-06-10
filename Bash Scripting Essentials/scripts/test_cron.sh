#!/bin/bash

# Test Cron Script - Runs every minute for testing
echo "$(date): Cron test executed successfully" >> "$HOME/cron_test.log"

# Create a simple backup of scripts directory
if [ -d "$HOME/scripts" ]; then
    cp -r "$HOME/scripts" "$HOME/cron_test_backup_$(date +%H%M%S)" 2>/dev/null
    echo "$(date): Test backup created" >> "$HOME/cron_test.log"
fi
