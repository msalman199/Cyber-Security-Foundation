# 🐧 Bash Scripting Essentials 

![Bash](https://img.shields.io/badge/Bash-Scripting-green?style=for-the-badge&logo=gnu-bash)
![Linux](https://img.shields.io/badge/Linux-Automation-blue?style=for-the-badge&logo=linux)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Automation-red?style=for-the-badge&logo=securityscorecard)
![Al%20Nafi](https://img.shields.io/badge/AlNafi-Cloud-orange?style=for-the-badge)

---

# 📖 Overview

This lab introduces the fundamentals of Bash scripting and automation on Linux systems. Students learn how to create executable scripts, implement loops and conditional statements, automate backups, schedule tasks with cron jobs, and apply scripting techniques commonly used in cybersecurity and system administration.

---

# 🎯 Lab Objectives

By the end of this lab, students will be able to:

- ✅ Create and execute Bash scripts
- ✅ Automate Linux administration tasks
- ✅ Implement loops and conditional statements
- ✅ Create file backup automation solutions
- ✅ Schedule scripts using cron jobs
- ✅ Apply Bash scripting concepts to cybersecurity automation

---

# 📚 Prerequisites

Before starting this lab, ensure you have:

- Basic Linux command-line knowledge
- Understanding of file system navigation
- Familiarity with Nano or Vim editors
- Knowledge of Linux file permissions
- Understanding of commands:
  - `cp`
  - `mv`
  - `mkdir`
  - `chmod`

---

# ☁️ Lab Environment

## Al Nafi Cloud Machine

This lab runs entirely on a Linux cloud machine provided by Al Nafi.

### System Requirements

- Ubuntu / CentOS / RHEL
- Bash Shell
- Nano or Vim
- Cron Service

---

# 🚀 Task 1 — Creating Your First Backup Script

## 📂 Setup Script Environment

### Create Working Directories

```bash
mkdir ~/scripts
cd ~/scripts

mkdir ~/test_data
cd ~/test_data

echo "This is document 1" > document1.txt
echo "This is document 2" > document2.txt
echo "Important data here" > important.txt

mkdir subdirectory
echo "Nested file content" > subdirectory/nested.txt

cd ~/scripts
```

---

## 📝 backup_script.sh

```bash
#!/bin/bash

# Backup Script - Lab 4

SOURCE_DIR="$HOME/test_data"
BACKUP_DIR="$HOME/backups"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="backup_$DATE"

if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
    echo "Created backup directory: $BACKUP_DIR"
fi

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory $SOURCE_DIR does not exist!"
    exit 1
fi

echo "Starting backup process..."
echo "Source: $SOURCE_DIR"
echo "Destination: $BACKUP_DIR/$BACKUP_NAME"

cp -r "$SOURCE_DIR" "$BACKUP_DIR/$BACKUP_NAME"

if [ $? -eq 0 ]; then
    echo "Backup completed successfully!"
    echo "Backup saved as: $BACKUP_DIR/$BACKUP_NAME"

    BACKUP_SIZE=$(du -sh "$BACKUP_DIR/$BACKUP_NAME" | cut -f1)
    echo "Backup size: $BACKUP_SIZE"
else
    echo "Backup failed!"
    exit 1
fi
```

### Make Executable

```bash
chmod +x backup_script.sh
```

### Run Script

```bash
./backup_script.sh
```

### Verify Backup

```bash
ls -la ~/backups/
```

---

# 🔁 Task 2 — Loops and Conditional Statements

## 🛡️ advanced_backup.sh

```bash
#!/bin/bash

BACKUP_BASE_DIR="$HOME/backups"
DATE=$(date +%Y%m%d_%H%M%S)
LOG_FILE="$HOME/backup_log.txt"

DIRECTORIES_TO_BACKUP=(
    "$HOME/test_data"
    "$HOME/scripts"
)

log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

check_disk_space() {
    local required_space=100
    local available_space=$(df -m "$HOME" | awk 'NR==2 {print $4}')

    if [ "$available_space" -lt "$required_space" ]; then
        log_message "ERROR: Insufficient disk space"
        return 1
    else
        log_message "Disk space check passed"
        return 0
    fi
}

backup_directory() {
    local source_dir="$1"
    local backup_name="$2"

    if [ ! -d "$source_dir" ]; then
        log_message "WARNING: Directory missing"
        return 1
    fi

    cp -r "$source_dir" "$BACKUP_BASE_DIR/$backup_name"

    if [ $? -eq 0 ]; then
        log_message "SUCCESS: Backup completed"
        return 0
    else
        log_message "ERROR: Backup failed"
        return 1
    fi
}

log_message "Starting backup process"

if ! check_disk_space; then
    exit 1
fi

mkdir -p "$BACKUP_BASE_DIR"

successful_backups=0
failed_backups=0

for dir in "${DIRECTORIES_TO_BACKUP[@]}"; do

    dir_name=$(basename "$dir")
    backup_folder_name="${dir_name}_${DATE}"

    if [ -d "$dir" ]; then

        if backup_directory "$dir" "$backup_folder_name"; then
            ((successful_backups++))
        else
            ((failed_backups++))
        fi

    else
        ((failed_backups++))
    fi

    sleep 1

done

log_message "Successful backups: $successful_backups"
log_message "Failed backups: $failed_backups"

exit 0
```

### Execute

```bash
chmod +x advanced_backup.sh
./advanced_backup.sh
```

### View Log

```bash
cat ~/backup_log.txt
```

---

# 📁 File Management Automation

## 📝 file_manager.sh

```bash
#!/bin/bash

TEST_DIR="$HOME/file_test"

mkdir -p "$TEST_DIR"

create_test_files() {

    for i in {1..10}; do
        echo "Test file content $i" > "$TEST_DIR/testfile$i.txt"
    done

    echo "Log Entry" > "$TEST_DIR/app.log"
    echo "Config Data" > "$TEST_DIR/config.conf"
    echo "Backup Data" > "$TEST_DIR/backup.bak"
}

analyze_files() {

    find "$TEST_DIR" -type f | while read file
    do
        extension="${file##*.}"

        case "$extension" in
            txt)
                echo "Text File"
                ;;
            log)
                echo "Log File"
                ;;
            conf)
                echo "Configuration File"
                ;;
            bak)
                echo "Backup File"
                ;;
            *)
                echo "Unknown File"
                ;;
        esac
    done
}

organize_files() {

    mkdir -p "$TEST_DIR/txt_files"
    mkdir -p "$TEST_DIR/log_files"
    mkdir -p "$TEST_DIR/config_files"
    mkdir -p "$TEST_DIR/backup_files"

    for file in "$TEST_DIR"/*
    do

        [ -d "$file" ] && continue

        extension="${file##*.}"

        if [ "$extension" = "txt" ]; then
            mv "$file" "$TEST_DIR/txt_files/"
        elif [ "$extension" = "log" ]; then
            mv "$file" "$TEST_DIR/log_files/"
        elif [ "$extension" = "conf" ]; then
            mv "$file" "$TEST_DIR/config_files/"
        elif [ "$extension" = "bak" ]; then
            mv "$file" "$TEST_DIR/backup_files/"
        fi

    done
}

while true
do

echo "1) Create Files"
echo "2) Analyze Files"
echo "3) Organize Files"
echo "4) Exit"

read choice

case $choice in

1)
create_test_files
;;

2)
analyze_files
;;

3)
organize_files
;;

4)
break
;;

*)
echo "Invalid Option"
;;

esac

done
```

### Run

```bash
chmod +x file_manager.sh
./file_manager.sh
```

---

# ⏰ Task 3 — Scheduling Scripts with Cron

## Check Cron Service

```bash
systemctl status cron
```

### Start Cron

```bash
sudo systemctl start cron
sudo systemctl enable cron
```

### View Existing Cron Jobs

```bash
crontab -l
```

---

# 🗄️ scheduled_backup.sh

```bash
#!/bin/bash

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

SOURCE_DIRS=(
    "$HOME/test_data"
    "$HOME/scripts"
)

BACKUP_BASE="$HOME/scheduled_backups"
LOG_FILE="$HOME/cron_backup.log"

DATE=$(date +%Y%m%d_%H%M%S)

log_msg() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') $1" >> "$LOG_FILE"
}

mkdir -p "$BACKUP_BASE"

for source_dir in "${SOURCE_DIRS[@]}"
do

    if [ -d "$source_dir" ]; then

        dir_name=$(basename "$source_dir")
        backup_name="${dir_name}_${DATE}"

        cp -r "$source_dir" "$BACKUP_BASE/$backup_name"

        if [ $? -eq 0 ]; then
            log_msg "Backup successful: $source_dir"
        else
            log_msg "Backup failed: $source_dir"
        fi

    fi

done

exit 0
```

### Execute

```bash
chmod +x scheduled_backup.sh
./scheduled_backup.sh
```

---

# 🗓️ Cron Scheduling Examples

Open Crontab:

```bash
crontab -e
```

Add:

```cron
# Daily Backup at 2 AM
0 2 * * * /home/$USER/scripts/scheduled_backup.sh

# Every 30 Minutes During Business Hours
*/30 9-17 * * 1-5 /home/$USER/scripts/scheduled_backup.sh

# Weekly Backup
0 0 * * 0 /home/$USER/scripts/backup_script.sh

# Monthly Log Cleanup
0 3 1 * * find /home/$USER -name "*.log" -type f -mtime +30 -delete
```

Verify:

```bash
crontab -l
```

---

# 🧪 Test Cron Job

## test_cron.sh

```bash
#!/bin/bash

echo "$(date): Cron test executed successfully" >> "$HOME/cron_test.log"

if [ -d "$HOME/scripts" ]; then
    cp -r "$HOME/scripts" \
    "$HOME/cron_test_backup_$(date +%H%M%S)"
fi
```

### Execute Permission

```bash
chmod +x test_cron.sh
```

### Add Cron Entry

```cron
* * * * * /home/$USER/scripts/test_cron.sh
```

### Verify

```bash
cat ~/cron_test.log

ls -la ~/cron_test_backup_*
```

---

# 📊 Cron Monitoring Dashboard

## cron_monitor.sh

```bash
#!/bin/bash

echo "Cron Job Monitoring Dashboard"
echo "============================="

echo ""
echo "Current Cron Jobs:"
crontab -l

echo ""
echo "Cron Service Status:"

if systemctl is-active --quiet cron; then
    echo "Cron Running"
else
    echo "Cron Stopped"
fi

echo ""
echo "Backup Directory Status"

if [ -d "$HOME/scheduled_backups" ]; then

    backup_count=$(ls -1 "$HOME/scheduled_backups" | wc -l)

    echo "Backups: $backup_count"

fi

echo ""
echo "Disk Usage"

df -h "$HOME" | tail -1

echo ""
echo "Monitoring Complete"
```

### Run

```bash
chmod +x cron_monitor.sh
./cron_monitor.sh
```

---

# ✅ Verification Checklist

Run all scripts:

```bash
cd ~/scripts

./backup_script.sh
./advanced_backup.sh
./file_manager.sh
./scheduled_backup.sh
./cron_monitor.sh
```

Verify directories:

```bash
ls -la ~/scripts/

ls -la ~/backups/

ls -la ~/scheduled_backups/
```

Check logs:

```bash
cat ~/backup_log.txt

cat ~/cron_backup.log
```

Check cron jobs:

```bash
crontab -l
```

Check permissions:

```bash
ls -la ~/scripts/*.sh
```

---

# 🛠️ Troubleshooting

## Permission Denied

```bash
chmod +x script_name.sh
```

## Missing Directories

```bash
mkdir -p ~/test_data
mkdir -p ~/backups
mkdir -p ~/scheduled_backups
```

## Cron Not Running

```bash
systemctl status cron

sudo systemctl start cron
```

## Log File Problems

```bash
touch ~/backup_log.txt
touch ~/cron_backup.log

chmod 644 ~/backup_log.txt
chmod 644 ~/cron_backup.log
```

---

# 📚 Key Bash Concepts Learned

| Concept | Description |
|----------|------------|
| Variables | Store dynamic values |
| Functions | Reusable code blocks |
| Loops | Repeat operations |
| Conditionals | Decision making |
| Arrays | Store multiple values |
| Case Statements | Menu systems |
| Cron Jobs | Scheduled automation |
| Logging | Activity tracking |
| File Operations | Backup and management |

---

# 🔐 Cybersecurity Relevance

Bash scripting is heavily used for:

- Incident Response Automation
- Security Monitoring
- Backup Management
- Log Analysis
- Compliance Reporting
- Threat Detection
- System Auditing
- Security Operations (SOC)

---

# 🎓 Conclusion

In this lab, you successfully:

- Created multiple Bash automation scripts
- Implemented loops, arrays, and conditional logic
- Built backup and file management solutions
- Scheduled automated jobs using Cron
- Created monitoring and logging systems
- Applied Linux automation techniques used in cybersecurity operations

These Bash scripting skills provide a strong foundation for Linux administration, DevOps workflows, SOC operations, incident response, and cybersecurity automation.

---

## 🏆 Lab Completed Successfully

**Technology Stack**

- 🐧 Linux
- 🖥️ Bash
- ⏰ Cron
- 📂 File Management
- 🔐 Cybersecurity Automation
- ☁️ Al Nafi Cloud Lab

**Author:** Hafiz Muhammad Salman  
**Lab:** Bash Scripting Essentials  
**Platform:** Al Nafi Cloud Labs

---
