#!/bin/bash

# Scheduled Backup Script for Cron Execution
# Lab 4 - Bash Scripting Essentials

# Set PATH for cron environment
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Configuration
SOURCE_DIRS=(
    "$HOME/test_data"
    "$HOME/scripts"
    "$HOME/Documents"
)

BACKUP_BASE="$HOME/scheduled_backups"
LOG_FILE="$HOME/cron_backup.log"
DATE=$(date +%Y%m%d_%H%M%S)
MAX_BACKUPS=7

# Function to log with timestamp
log_msg() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [CRON-BACKUP] $1" >> "$LOG_FILE"
}

# Function to send notification (for demonstration)
send_notification() {
    local message="$1"
    log_msg "NOTIFICATION: $message"
    # In a real environment, you might send email or system notification
    echo "$message" > "$HOME/last_backup_status.txt"
}

# Start logging
log_msg "Starting scheduled backup process"

# Create backup directory
mkdir -p "$BACKUP_BASE"

# Initialize success counter
successful_backups=0
total_dirs=${#SOURCE_DIRS[@]}

# Backup each directory
for source_dir in "${SOURCE_DIRS[@]}"; do
    if [ -d "$source_dir" ]; then
        dir_name=$(basename "$source_dir")
        backup_name="${dir_name}_${DATE}"
        
        log_msg "Backing up: $source_dir -> $backup_name"
        
        # Create backup
        if cp -r "$source_dir" "$BACKUP_BASE/$backup_name" 2>/dev/null; then
            backup_size=$(du -sh "$BACKUP_BASE/$backup_name" | cut -f1)
            log_msg "SUCCESS: $source_dir backed up successfully (Size: $backup_size)"
            ((successful_backups++))
        else
            log_msg "ERROR: Failed to backup $source_dir"
        fi
    else
        log_msg "WARNING: Directory $source_dir does not exist, skipping"
    fi
done

# Cleanup old backups
log_msg "Cleaning up old backups (keeping last $MAX_BACKUPS)"
backup_count=$(ls -1 "$BACKUP_BASE" 2>/dev/null | wc -l)

if [ "$backup_count" -gt "$MAX_BACKUPS" ]; then
    old_backups_count=$((backup_count - MAX_BACKUPS))
    ls -1t "$BACKUP_BASE" | tail -n "$old_backups_count" | while read old_backup; do
        rm -rf "$BACKUP_BASE/$old_backup"
        log_msg "Removed old backup: $old_backup"
    done
    log_msg "Cleanup completed: removed $old_backups_count old backups"
fi

# Generate summary
log_msg "Backup process completed: $successful_backups/$total_dirs directories backed up successfully"

# Send notification based on results
if [ "$successful_backups" -eq "$total_dirs" ]; then
    send_notification "Backup completed successfully: $successful_backups/$total_dirs directories"
else
    send_notification "Backup completed with issues: $successful_backups/$total_dirs directories successful"
fi

# Exit with appropriate code
if [ "$successful_backups" -gt 0 ]; then
    exit 0
else
    exit 1
fi
