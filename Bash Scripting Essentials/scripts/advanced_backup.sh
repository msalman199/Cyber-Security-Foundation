#!/bin/bash

# Advanced Backup Script with Loops and Conditionals
# Lab 4 - Bash Scripting Essentials

# Configuration variables
BACKUP_BASE_DIR="$HOME/backups"
DATE=$(date +%Y%m%d_%H%M%S)
LOG_FILE="$HOME/backup_log.txt"

# Array of directories to backup
DIRECTORIES_TO_BACKUP=(
    "$HOME/test_data"
    "$HOME/scripts"
)

# Function to log messages
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

# Function to check disk space
check_disk_space() {
    local required_space=100  # MB
    local available_space=$(df -m "$HOME" | awk 'NR==2 {print $4}')
    
    if [ "$available_space" -lt "$required_space" ]; then
        log_message "ERROR: Insufficient disk space. Required: ${required_space}MB, Available: ${available_space}MB"
        return 1
    else
        log_message "Disk space check passed. Available: ${available_space}MB"
        return 0
    fi
}

# Function to backup a single directory
backup_directory() {
    local source_dir="$1"
    local backup_name="$2"
    
    if [ ! -d "$source_dir" ]; then
        log_message "WARNING: Directory $source_dir does not exist, skipping..."
        return 1
    fi
    
    # Count files in source directory
    local file_count=$(find "$source_dir" -type f | wc -l)
    log_message "Backing up $file_count files from $source_dir"
    
    # Create backup
    cp -r "$source_dir" "$BACKUP_BASE_DIR/$backup_name"
    
    if [ $? -eq 0 ]; then
        local backup_size=$(du -sh "$BACKUP_BASE_DIR/$backup_name" | cut -f1)
        log_message "SUCCESS: Backup completed for $source_dir (Size: $backup_size)"
        return 0
    else
        log_message "ERROR: Backup failed for $source_dir"
        return 1
    fi
}

# Main script execution
log_message "Starting advanced backup process"

# Check disk space before proceeding
if ! check_disk_space; then
    log_message "Backup aborted due to insufficient disk space"
    exit 1
fi

# Create main backup directory
mkdir -p "$BACKUP_BASE_DIR"

# Initialize counters
successful_backups=0
failed_backups=0

# Loop through directories and backup each one
for dir in "${DIRECTORIES_TO_BACKUP[@]}"; do
    # Extract directory name for backup folder
    dir_name=$(basename "$dir")
    backup_folder_name="${dir_name}_${DATE}"
    
    log_message "Processing directory: $dir"
    
    # Conditional check for directory existence and backup
    if [ -d "$dir" ]; then
        if backup_directory "$dir" "$backup_folder_name"; then
            ((successful_backups++))
        else
            ((failed_backups++))
        fi
    else
        log_message "WARNING: Directory $dir not found"
        ((failed_backups++))
    fi
    
    # Add a small delay between backups
    sleep 1
done

# Final report
log_message "Backup process completed"
log_message "Successful backups: $successful_backups"
log_message "Failed backups: $failed_backups"

# Conditional cleanup of old backups (keep only last 5)
log_message "Checking for old backups to clean up..."
backup_count=$(ls -1 "$BACKUP_BASE_DIR" | wc -l)

if [ "$backup_count" -gt 5 ]; then
    log_message "Found $backup_count backups, cleaning up old ones..."
    # Remove oldest backups, keep only 5 most recent
    ls -1t "$BACKUP_BASE_DIR" | tail -n +6 | while read old_backup; do
        rm -rf "$BACKUP_BASE_DIR/$old_backup"
        log_message "Removed old backup: $old_backup"
    done
else
    log_message "Backup count ($backup_count) is within limit, no cleanup needed"
fi

# Exit with appropriate code
if [ "$failed_backups" -eq 0 ]; then
    log_message "All backups completed successfully!"
    exit 0
else
    log_message "Some backups failed. Check log for details."
    exit 1
fi
