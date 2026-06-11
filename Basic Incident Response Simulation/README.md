# 🚨 Basic Incident Response Simulation

<div align="center">

![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Incident Response](https://img.shields.io/badge/Incident_Response-Blue?style=for-the-badge&logo=securityscorecard&logoColor=white)
![Digital Forensics](https://img.shields.io/badge/Digital_Forensics-Analysis-red?style=for-the-badge)
![Cyber Security](https://img.shields.io/badge/Cyber_Security-SOC-green?style=for-the-badge)
![Bash](https://img.shields.io/badge/Bash-Scripting-black?style=for-the-badge&logo=gnubash)

</div>

---

# 📖 Overview

This hands-on lab introduces fundamental **Incident Response (IR)** procedures through a simulated security breach scenario.

You will learn how to:

- 🔍 Identify Indicators of Compromise (IoCs)
- 🚫 Contain suspicious processes and network activity
- 📦 Collect forensic evidence
- 📊 Analyze logs and system activity
- 📝 Document incident response actions
- 🛡️ Follow industry-standard IR methodologies

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

✅ Identify common Indicators of Compromise (IoCs)

✅ Analyze Linux processes and network activity

✅ Implement threat containment measures

✅ Collect forensic evidence safely

✅ Create incident response documentation

✅ Investigate suspicious files and user activity

---

# 📋 Prerequisites

Before beginning this lab, ensure you have:

- Linux Command Line Knowledge
- Understanding of Linux File Permissions
- Basic Networking Concepts
- Familiarity with Nano or Vim
- Knowledge of Linux Logs
- Understanding of Processes and Services

---

# 🖥️ Lab Environment

## ☁️ Al Nafi Cloud Machine

When you click **Start Lab**, you will receive access to a Linux cloud machine.

All tools required for this exercise will be installed during the lab.

---

# ⚙️ Initial System Preparation

## 📦 Update System

```bash
sudo apt update
```

## 📦 Install Incident Response Tools

```bash
sudo apt install -y netstat-nat tcpdump aide chkrootkit
```

## ✅ Verify Installation

```bash
which tcpdump aide chkrootkit
```

---

# 🔍 Exercise 1: Identifying Indicators of Compromise

## 🛠️ Step 1: Check Suspicious Processes

### View All Running Processes

```bash
ps aux | less
```

### Find High CPU Usage Processes

```bash
ps aux --sort=-%cpu | head -20
```

### Check Processes Running as Root

```bash
ps aux | grep root
```

### 🔎 What to Look For

- Unknown processes
- Processes running from `/tmp`
- High CPU usage
- Unexpected root-owned services

---

## 🌐 Step 2: Examine Network Connections

### Active Network Connections

```bash
sudo netstat -tulpn
```

### Established Connections

```bash
sudo netstat -antp | grep ESTABLISHED
```

### Listening Ports

```bash
sudo ss -tulpn
```

### 🔎 What to Look For

- Unknown IP addresses
- Suspicious outbound traffic
- Unexpected listening services
- Unusual ports

---

## 🔑 Step 3: Review Authentication Logs

### Failed Login Attempts

```bash
sudo grep "Failed password" /var/log/auth.log | tail -20
```

### Root Logins

```bash
sudo grep "session opened for user root" /var/log/auth.log
```

### Recent sudo Activity

```bash
sudo grep "sudo:" /var/log/auth.log | tail -20
```

### 🔎 Indicators

- Brute-force attempts
- Unauthorized root access
- Unexpected sudo usage

---

# 🚫 Exercise 2: Implementing Containment Measures

## 🛑 Step 1: Isolate Suspicious Processes

### Kill Malicious Process

```bash
sudo kill -9 [PID]
```

### Stop Suspicious Service

```bash
sudo systemctl stop [service_name]
```

### Disable Service Permanently

```bash
sudo systemctl disable [service_name]
```

---

## 🔥 Step 2: Block Network Communication

### Block Outbound Traffic

```bash
sudo iptables -A OUTPUT -d [SUSPICIOUS_IP] -j DROP
```

### Block Inbound Traffic

```bash
sudo iptables -A INPUT -s [SUSPICIOUS_IP] -j DROP
```

### Save Firewall Rules

```bash
sudo iptables-save > /tmp/firewall_rules_backup.txt
```

---

## 👤 Step 3: Preserve User Accounts

### Lock User Account

```bash
sudo usermod -L [username]
```

### Disable Password Authentication

```bash
sudo passwd -l [username]
```

### Check Active Sessions

```bash
who
```

```bash
w
```

---

# 📦 Exercise 3: Forensic Data Collection

---

## 📄 collect_evidence.sh

```bash
#!/bin/bash

# Incident Response Data Collection Script

TIMESTAMP=$(date +%Y%m%d_%H%M%S)

OUTPUT_DIR="/tmp/ir_collection_${TIMESTAMP}"

mkdir -p ${OUTPUT_DIR}

echo "Starting forensic data collection..."

# System Information

uname -a > ${OUTPUT_DIR}/system_info.txt
hostname >> ${OUTPUT_DIR}/system_info.txt
uptime >> ${OUTPUT_DIR}/system_info.txt

# Processes

ps auxf > ${OUTPUT_DIR}/processes.txt

# Network

sudo netstat -antp > ${OUTPUT_DIR}/network_connections.txt
sudo ss -tulpn > ${OUTPUT_DIR}/listening_ports.txt

# Users

who > ${OUTPUT_DIR}/logged_in_users.txt
last -20 > ${OUTPUT_DIR}/recent_logins.txt

# Authentication Logs

sudo cp /var/log/auth.log ${OUTPUT_DIR}/auth.log

# Create Evidence Archive

tar -czf ${OUTPUT_DIR}.tar.gz ${OUTPUT_DIR}

echo "Collection complete: ${OUTPUT_DIR}.tar.gz"
```

---

## ▶ Save and Execute

### Create File

```bash
nano collect_evidence.sh
```

### Make Executable

```bash
chmod +x collect_evidence.sh
```

### Run Script

```bash
sudo ./collect_evidence.sh
```

---

## 🔐 Generate Evidence Hash

### Create SHA256 Hash

```bash
sha256sum /tmp/ir_collection_*.tar.gz > evidence_hashes.txt
```

### Display Hash

```bash
cat evidence_hashes.txt
```

---

# 📊 Exercise 4: Log Analysis

## 📜 Step 1: Analyze Logs

### Search Bash History

```bash
cat ~/.bash_history | grep -E "(wget|curl|nc|nmap)"
```

### Review System Errors

```bash
sudo grep -i error /var/log/syslog | tail -50
```

### Check Kernel Errors

```bash
sudo dmesg | grep -i error
```

---

## ⏳ Step 2: Create Activity Timeline

### Recent User File Changes

```bash
find /home -type f -mtime -1 -ls > /tmp/recent_file_changes.txt
```

### Recent Configuration Changes

```bash
find /etc -type f -mtime -1 -ls > /tmp/recent_etc_changes.txt
```

---

## 🔍 Step 3: Search for Malicious Indicators

### Recently Created Shell Scripts

```bash
sudo find / -name "*.sh" -type f -mtime -1 2>/dev/null
```

### Find SUID Binaries

```bash
sudo find / -perm -4000 -type f 2>/dev/null
```

### Hidden Files in Temporary Directories

```bash
sudo find /tmp /var/tmp -name ".*" -type f 2>/dev/null
```

---

# 📝 Exercise 5: Incident Documentation

## 📄 Incident Report Template

```markdown
# Incident Response Report

**Incident ID:** IR-[DATE]-001
**Date/Time Detected:** [TIMESTAMP]
**Analyst:** [YOUR NAME]
**Severity:** [HIGH/MEDIUM/LOW]

## Executive Summary

[Brief description of incident]

## Indicators of Compromise

- Suspicious Process: [DETAILS]
- Network Connection: [DETAILS]
- File Modifications: [DETAILS]

## Containment Actions Taken

1. [ACTION 1]
2. [ACTION 2]
3. [ACTION 3]

## Evidence Collected

- Location: /tmp/ir_collection_[TIMESTAMP].tar.gz
- Hash: [SHA256 HASH]

## Timeline of Events

- [TIME] - [EVENT]
- [TIME] - [EVENT]

## Recommendations

1. [RECOMMENDATION]
2. [RECOMMENDATION]

## Next Steps

- [ ] Complete malware analysis
- [ ] Review firewall rules
- [ ] Update security policies
```

---

# 🧹 Lab Cleanup

## Remove Collected Evidence

```bash
sudo rm -rf /tmp/ir_collection_*
```

## Flush Firewall Rules

```bash
sudo iptables -F
```

## Final Documentation

```text
Document all actions taken during the investigation.
```

---

# ✅ Verification Checklist

Verify that you successfully completed:

- [ ] Process Analysis
- [ ] Network Investigation
- [ ] Authentication Log Review
- [ ] Threat Containment
- [ ] Evidence Collection
- [ ] Evidence Hashing
- [ ] Timeline Creation
- [ ] IOC Discovery
- [ ] Incident Report Creation

---

# 🚀 Key Takeaways

### 🔐 Preserve Evidence Integrity

Always create cryptographic hashes for evidence.

### 📝 Document Everything

Every action taken during an incident should be recorded.

### 🚫 Containment First

Prevent further compromise before remediation.

### 📦 Collect Before Changing

Gather evidence before modifying the affected system.

### 🔗 Maintain Chain of Custody

Track evidence ownership and handling.

---

# 🌍 Real-World Applications

This lab prepares you for:

- 🏢 Security Operations Center (SOC)
- 🕵️ Digital Forensics
- 🚨 Incident Response Teams
- 🔐 Cyber Defense Operations
- 📊 Security Monitoring
- 🛡️ Threat Hunting

---

# 📚 Additional Resources

### NIST Incident Response Guide

NIST SP 800-61 Computer Security Incident Handling Guide

### SANS Incident Handler's Handbook

Industry-standard incident response methodology.

### Linux Forensics Resources

Open-source tools and forensic analysis techniques.

---

# 🎓 Conclusion

In this lab, you successfully learned the core phases of Incident Response:

✅ Detection

✅ Analysis

✅ Containment

✅ Evidence Collection

✅ Documentation

✅ Investigation

You now have practical experience performing a basic incident response investigation using Linux tools and industry best practices. These skills serve as the foundation for advanced SOC operations, digital forensics, threat hunting, and cybersecurity incident management.

---

<div align="center">

## 🚨 Detect • Analyze • Contain • Investigate • Recover

### Hands-On Incident Response & Digital Forensics Lab

⭐ Built for SOC Analysts, Incident Responders, and Cybersecurity Professionals

</div>
