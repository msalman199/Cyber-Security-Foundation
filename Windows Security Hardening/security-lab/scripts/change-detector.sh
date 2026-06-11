#!/bin/bash

LOG_FILE="$HOME/security-lab/logs/change-detection-$(date +%Y%m%d).log"
BASELINE_DIR="$HOME/security-lab/config/baselines"

# TODO: Create function check_file_changes(file_path)
# Compare current file stats with baseline
# Alert if modified

check_file_changes() {
    local file_path="$1"
    # TODO: Get current file stats (modification time, size, permissions)
    # Hint: Use stat -c "%Y %s %a" $file_path
    
    # TODO: Compare with baseline file
    # TODO: Alert if different or create baseline if new
}

# TODO: Create function check_user_changes()
# Monitor /etc/passwd and /etc/shadow for changes

check_user_changes() {
    # TODO: Calculate SHA256 hash of /etc/passwd
    # TODO: Compare with baseline
    # TODO: Show diff if changed
    # TODO: Repeat for /etc/shadow
}

# TODO: Create function check_network_changes()
# Monitor /etc/hosts for modifications

check_network_changes() {
    # TODO: Calculate hash of /etc/hosts
    # TODO: Compare with baseline
    # TODO: Show diff if changed
}

# TODO: Create function check_service_changes()
# Monitor running services

check_service_changes() {
    # TODO: List running services
    # Hint: systemctl list-units --type=service --state=running
    # TODO: Compare with baseline
    # TODO: Show diff if changed
}

# TODO: Define CRITICAL_FILES array
CRITICAL_FILES=(
    # TODO: Add critical system files
)

# TODO: Run all check functions
# TODO: Log results
