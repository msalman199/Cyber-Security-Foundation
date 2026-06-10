# 🐍 Python Scripting for Automation

<div align="center">

# 🚀 Python Automation 

### 📚 Cyber Security Foundation – Hands-On Lab

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge\&logo=ubuntu)
![Automation](https://img.shields.io/badge/Automation-Scripting-green?style=for-the-badge)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Lab-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

</div>

---

# 📖 Overview

This lab introduces Python scripting for automation in a Linux environment. Students learn how to automate file operations, perform folder cleanup, create monitoring tools, validate password security, and develop reusable Python functions.

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

✅ Write Python scripts to read and write files

✅ Create automated folder cleanup utilities

✅ Use loops for repetitive tasks

✅ Apply conditional statements for decision making

✅ Define and reuse functions

✅ Build cybersecurity-focused automation tools

✅ Execute Python scripts from the Linux command line

---

# 📋 Prerequisites

* Linux Command Line Basics
* Text Editor Knowledge (Nano/Vim/Gedit)
* Basic Programming Concepts
* File System Navigation Skills

---

# 🛠️ Lab Environment

### Environment Includes

* Ubuntu Linux
* Python 3.x
* Nano
* Vim
* Gedit
* Full File Operation Permissions

---

# 📂 Task 1 — File Operations with Python

---

## 🔹 Create Lab Directory Structure

```bash
mkdir -p ~/python_automation_lab
cd ~/python_automation_lab
mkdir scripts data logs
```

---

## 🔹 Create Sample Dataset

```bash
echo -e "server1,192.168.1.10,active\nserver2,192.168.1.11,inactive\nserver3,192.168.1.12,active\nfirewall1,192.168.1.1,active" > data/network_devices.csv
```

---

## 🔹 File Reader Script

Create:

```bash
nano scripts/file_reader.py
```

```python
#!/usr/bin/env python3

"""
File Reader Script
"""

def read_network_devices(filename):
    try:
        with open(filename, 'r') as file:
            print("Network Device Inventory:")
            print("-" * 40)
            print("Device Name | IP Address | Status")
            print("-" * 40)

            for line in file:
                device_info = line.strip().split(',')

                if len(device_info) == 3:
                    device_name, ip_address, status = device_info

                    print(
                        f"{device_name:12} | {ip_address:13} | {status}"
                    )

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")

    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    filename = "../data/network_devices.csv"
    read_network_devices(filename)

if __name__ == "__main__":
    main()
```

Run:

```bash
chmod +x scripts/file_reader.py
cd scripts
python3 file_reader.py
```

---

# 📝 File Writer Script

Create:

```bash
nano log_writer.py
```

```python
#!/usr/bin/env python3

import datetime

def write_security_log(log_file, event_type, message):

    timestamp = datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    log_entry = f"[{timestamp}] {event_type}: {message}\n"

    with open(log_file, "a") as file:
        file.write(log_entry)

    print(f"Log entry written: {event_type}")

def create_sample_logs():

    log_file = "../logs/security.log"

    events = [
        ("INFO", "User admin logged in successfully"),
        ("WARNING", "Failed login attempt from IP 192.168.1.100"),
        ("ERROR", "Unauthorized access attempt detected"),
        ("INFO", "Firewall rule updated"),
        ("CRITICAL", "Multiple failed login attempts - account locked")
    ]

    for event_type, message in events:
        write_security_log(
            log_file,
            event_type,
            message
        )

def main():
    create_sample_logs()

if __name__ == "__main__":
    main()
```

Run:

```bash
python3 log_writer.py
```

Verify:

```bash
cat ../logs/security.log
```

---

# 🧹 Task 2 — Automated Folder Cleanup

---

## 🔹 Create Test Files

```bash
cd ~/python_automation_lab

mkdir temp_files
cd temp_files

touch old_log_1.log old_log_2.log

touch temp_file_1.tmp temp_file_2.tmp temp_file_3.tmp

touch backup_1.bak backup_2.bak

touch document.txt important.pdf

touch cache_file_1.cache cache_file_2.cache

mkdir old_backups

touch old_backups/backup_2023_01.bak
touch old_backups/backup_2023_02.bak
```

---

## 🔹 Folder Cleanup Script

```python
#!/usr/bin/env python3

import os
import glob

def cleanup_by_extension(directory, extensions_to_remove):

    removed_files = []

    for extension in extensions_to_remove:

        pattern = os.path.join(
            directory,
            f"*.{extension}"
        )

        files = glob.glob(pattern)

        for file_path in files:

            try:
                os.remove(file_path)

                removed_files.append(file_path)

                print(
                    f"Removed: {os.path.basename(file_path)}"
                )

            except Exception as e:
                print(e)

    return removed_files

def main():

    cleanup_directory = "../temp_files"

    extensions = [
        "tmp",
        "log",
        "cache",
        "bak"
    ]

    cleanup_by_extension(
        cleanup_directory,
        extensions
    )

if __name__ == "__main__":
    main()
```

Run:

```bash
python3 folder_cleanup.py
```

---

# 🌐 Task 3 — Network Security Monitoring

---

## 🔹 Network Monitor Script

Create:

```bash
nano network_monitor.py
```

### Features

* Random Network Traffic Simulation
* Failed Login Monitoring
* Threat Detection Logic
* Security Event Logging
* Dashboard Output
* Summary Reporting

Run:

```bash
python3 network_monitor.py
```

---

### Example Dashboard

```text
=== NETWORK SECURITY SCAN #1 ===

Threat Level: MEDIUM

Active Connections: 120
Failed Login Attempts: 8
Bandwidth Usage: 88%
Suspicious IP Addresses: 2

SECURITY ALERTS:
1. Moderate failed login attempts
2. Suspicious IP addresses detected
```

---

# 🔐 Task 4 — Password Security Checker

---

Create:

```bash
nano password_checker.py
```

### Security Checks

✅ Minimum Length

✅ Uppercase Letters

✅ Lowercase Letters

✅ Numbers

✅ Special Characters

✅ Common Password Detection

✅ Repeated Character Detection

---

Run:

```bash
python3 password_checker.py
```

---

### Example Output

```text
Password Strength: 🟢 VERY STRONG

Score: 10/11

Recommendations:
None
```

---

# ✅ Verification

---

## Verify Scripts

```bash
find . -name "*.py" -type f
```

---

## Verify Logs

```bash
find . -name "*.log" -type f
```

---

## Verify CSV Data

```bash
find . -name "*.csv" -type f
```

---

## Run Every Script

```bash
cd scripts

python3 file_reader.py

python3 log_writer.py

python3 folder_cleanup.py

python3 network_monitor.py

python3 password_checker.py
```

---

# 🔍 Troubleshooting

## Permission Denied

```bash
chmod +x *.py
```

---

## Python Version Check

```bash
python3 --version
```

---

## Verify Current Directory

```bash
pwd

ls -la
```

---

## Syntax Validation

```bash
python3 -m py_compile script_name.py
```

---

# 🚀 Advanced Challenges

### Challenge 1

Separate threat levels into different log files.

---

### Challenge 2

Generate CSV password security reports.

---

### Challenge 3

Build a Security Dashboard integrating:

* File Operations
* Log Analysis
* Threat Monitoring
* Reporting

---

# 🎓 Skills Gained

✅ Python File Handling

✅ Logging Automation

✅ Folder Cleanup Automation

✅ Functions and Reusable Code

✅ Conditional Logic

✅ Loops and Iteration

✅ Cybersecurity Automation

✅ Security Monitoring

✅ Password Security Analysis

---

# 🔐 Cybersecurity Relevance

Python automation enables:

* Threat Detection
* Log Analysis
* Incident Response
* Compliance Reporting
* Vulnerability Assessment
* Security Monitoring

These capabilities are fundamental for Security Analysts, SOC Engineers, Incident Responders, and Automation Engineers.

---

# 🏆 Lab Completion Summary

Successfully Completed:

* File Reader Automation
* Log Writer Automation
* Folder Cleanup Automation
* Network Security Monitoring
* Password Security Validation
* Python Scripting Fundamentals

---

<div align="center">

## 🎉 Congratulations!

You have successfully completed the

# 🐍 Python Scripting for Automation Lab

and developed practical automation skills used in real-world cybersecurity operations.

⭐ Keep Building • Keep Automating • Keep Securing ⭐

</div>
