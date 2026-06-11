#!/bin/bash

LOG_FILE="$HOME/security-lab/logs/integrity-check-$(date +%Y%m%d).log"
BASELINE_DIR="$HOME/security-lab/config/baselines"

# TODO: Create baseline directory if not exists

# TODO: Define array of critical files to monitor
CRITICAL_FILES=(
    "/etc/passwd"
    # TODO: Add /etc/shadow, /etc/sudoers, /etc/ssh/sshd_config
)

# TODO: For each file:
#   1. Calculate current SHA256 hash
#   2. Compare with baseline (if exists)
#   3. Alert if different, or create baseline if new
# Hint: Use sha256sum command

# TODO: Log completion message
