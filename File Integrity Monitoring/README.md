# 🛡️ File Integrity Monitoring (FIM) 

<div align="center">

# 🔐 Linux File Integrity Monitoring & Security Auditing

### Monitor • Detect • Protect • Respond

![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04%2B-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Security-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Auditd](https://img.shields.io/badge/Auditd-System%20Auditing-blue?style=for-the-badge)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![Inotify](https://img.shields.io/badge/Inotify-Real--Time%20Monitoring-orange?style=for-the-badge)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Defense-red?style=for-the-badge)
![Monitoring](https://img.shields.io/badge/File-Integrity%20Monitoring-success?style=for-the-badge)

</div>

---

# 📖 Overview

File Integrity Monitoring (FIM) is a critical cybersecurity practice used to detect unauthorized changes to files, directories, and system configurations.

In this lab, you will learn how to:

✅ Configure and use Auditd

✅ Monitor sensitive files and directories

✅ Detect unauthorized modifications

✅ Generate security reports

✅ Implement real-time monitoring

✅ Create automated monitoring services

✅ Improve Linux security posture

---

# 🎯 Learning Objectives

By the end of this lab, you will be able to:

- 🔍 Understand File Integrity Monitoring concepts
- 🛡️ Configure and manage Auditd
- 📁 Monitor sensitive files and directories
- ⚙️ Create automated integrity checking scripts
- 🚨 Detect unauthorized modifications
- 📊 Analyze security audit logs
- 🔄 Implement real-time monitoring solutions
- 📑 Generate security reports for incident response

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

- Linux command-line fundamentals
- Understanding of Linux permissions
- Basic Bash scripting knowledge
- Familiarity with text editors
- Cybersecurity fundamentals

---

# 🖥️ Lab Environment

### ☁️ Al Nafi Cloud Machine

This lab runs entirely on a Linux-based cloud machine provided by Al Nafi.

No additional virtual machine setup is required.

### System Requirements

| Requirement | Details |
|------------|----------|
| Operating System | Ubuntu 20.04+ |
| Access | Root / Sudo |
| Internet | Required |
| Shell | Bash |

---

# 🧰 Technologies Used

| Technology | Purpose |
|------------|----------|
| Auditd | System Auditing |
| Auditctl | Audit Rule Management |
| Ausearch | Audit Log Searching |
| Aureport | Audit Reporting |
| Inotify | Real-Time File Monitoring |
| Bash | Automation |
| MD5 Checksums | Integrity Validation |
| Linux | Security Operations |

---

# 🚀 Task 1: Setting Up Auditd

## 🔹 Install Auditd

```bash
sudo apt update
sudo apt install auditd audispd-plugins -y
```

---

## 🔹 Verify Service Status

```bash
sudo systemctl status auditd
```

---

## 🔹 Enable Auditd

```bash
sudo systemctl start auditd
sudo systemctl enable auditd
```

---

## 🔹 Verify Configuration

```bash
auditctl --version
sudo auditctl -s
```

---

# 📂 Creating Audit Rules

## Create Monitoring Directory

```bash
mkdir -p /home/$USER/secure_files

echo "This is a sensitive document" > /home/$USER/secure_files/important.txt

echo "Configuration data" > /home/$USER/secure_files/config.conf
```

---

## Configure Audit Rules

```bash
sudo auditctl -w /home/$USER/secure_files -p rwxa -k file_access

sudo auditctl -w /home/$USER/secure_files -p a -k file_attributes

sudo auditctl -w /etc/passwd -p wa -k passwd_changes

sudo auditctl -w /etc/shadow -p wa -k shadow_changes
```

---

## View Active Rules

```bash
sudo auditctl -l
```

---

## Generate Test Events

### Read File

```bash
cat /home/$USER/secure_files/important.txt
```

### Modify File

```bash
echo "Modified content" >> /home/$USER/secure_files/important.txt
```

### Change Permissions

```bash
chmod 755 /home/$USER/secure_files/important.txt
```

---

# 🔍 Audit Log Analysis

## Search Events

```bash
sudo ausearch -k file_access
```

---

## Recent Events

```bash
sudo ausearch -ts recent
```

---

## Generate Reports

```bash
sudo aureport -f
sudo aureport -au
```

---

# 📊 Audit Report Script

Create:

```bash
nano audit_report.sh
```

Make executable:

```bash
chmod +x audit_report.sh
```

Run:

```bash
./audit_report.sh
```

---

# 🚀 Task 2: Automated File Integrity Checking

## 🔐 MD5-Based Integrity Monitoring

Create:

```bash
nano file_integrity_checker.sh
```

Features:

- Baseline Creation
- Change Detection
- Deleted File Detection
- New File Detection
- Detailed Reporting

---

## Make Script Executable

```bash
chmod +x file_integrity_checker.sh
```

---

## Create Baseline

```bash
./file_integrity_checker.sh -c
```

---

## Modify File

```bash
echo "This file has been modified" >> /home/$USER/secure_files/important.txt
```

---

## Run Integrity Scan

```bash
./file_integrity_checker.sh -s
```

---

# ⚡ Real-Time Monitoring with Inotify

## Install Tools

```bash
sudo apt install inotify-tools -y
```

---

## Create Monitoring Script

```bash
nano realtime_monitor.sh
```

---

## Make Executable

```bash
chmod +x realtime_monitor.sh
```

---

## Start Monitoring

```bash
./realtime_monitor.sh &
```

---

## Generate Events

### Create File

```bash
echo "New test file" > /home/$USER/secure_files/test_new.txt
```

### Modify File

```bash
echo "Additional content" >> /home/$USER/secure_files/config.conf
```

### Change Permissions

```bash
chmod 600 /home/$USER/secure_files/test_new.txt
```

### Delete File

```bash
rm /home/$USER/secure_files/test_new.txt
```

---

## View Monitoring Log

```bash
cat /home/$USER/realtime_monitor.log
```

---

# 🚨 Task 3: Monitoring Critical Directories

## Critical Directories

```text
/etc
/home/$USER/secure_files
/var/log
/usr/bin
/usr/sbin
```

---

## Create Monitoring Tool

```bash
nano critical_dirs_monitor.sh
```

Capabilities:

- Audit Rule Deployment
- Baseline Creation
- Change Detection
- Security Reporting
- Critical File Monitoring

---

## Make Executable

```bash
chmod +x critical_dirs_monitor.sh
```

---

## Configure Monitoring

```bash
./critical_dirs_monitor.sh setup
```

---

## Create Baseline

```bash
./critical_dirs_monitor.sh baseline
```

---

## Generate Monitoring Report

```bash
./critical_dirs_monitor.sh monitor
```

---

## Generate Security Report

```bash
./critical_dirs_monitor.sh report
```

---

# 🔄 Automated Monitoring Service

Create:

```bash
nano fim_service.sh
```

---

## Make Executable

```bash
chmod +x fim_service.sh
```

---

## Start Service

```bash
./fim_service.sh start
```

---

## Check Status

```bash
./fim_service.sh status
```

---

## View Logs

```bash
tail -20 /home/$USER/monitoring_logs/fim_service.log
```

---

## Stop Service

```bash
./fim_service.sh stop
```

---

# ✅ Verification

## Verify Rules

```bash
sudo auditctl -l | wc -l
```

---

## Run Full Monitoring Workflow

```bash
echo "Final test modification" >> /home/$USER/secure_files/important.txt

touch /home/$USER/secure_files/final_test.txt

./file_integrity_checker.sh -s

./critical_dirs_monitor.sh monitor

./critical_dirs_monitor.sh report
```

---

## Review Reports

```bash
ls -la /home/$USER/monitoring_logs/

ls -la /home/$USER/integrity_report_*.txt
```

---

# 🛠️ Troubleshooting

## Issue 1: Auditd Not Starting

```bash
sudo systemctl reset-failed auditd

sudo systemctl start auditd

sudo systemctl status auditd
```

---

## Issue 2: Permission Errors

```bash
chmod 755 /home/$USER/secure_files

sudo auditctl -l
```

---

## Issue 3: No Audit Events

```bash
sudo auditctl -l

sudo tail -f /var/log/audit/audit.log
```

---

## Issue 4: Script Errors

```bash
chmod +x *.sh

bash -n script_name.sh
```

---

# 🏆 Key Achievements

### 🛡️ Security Enhancement

Implemented multi-layer file integrity monitoring.

### ⚙️ Automation

Developed automated monitoring and reporting scripts.

### 🚨 Incident Response

Generated detailed reports for investigations.

### 🔄 Continuous Monitoring

Implemented real-time file monitoring capabilities.

---

# 🌍 Real-World Applications

### Enterprise Security
Monitor sensitive files and configurations.

### Compliance Monitoring
Meet regulatory FIM requirements.

### Incident Detection
Identify unauthorized modifications quickly.

### System Administration
Maintain system integrity and stability.

---

# 📈 Future Enhancements

- SIEM Integration
- Email Alerting
- Slack Notifications
- AIDE Deployment
- Distributed Monitoring
- Centralized Log Management
- Threat Intelligence Integration

---

# 🎓 Conclusion

This File Integrity Monitoring Lab provided hands-on experience with:

- Auditd Configuration
- Security Auditing
- Real-Time Monitoring
- Bash Automation
- Incident Response
- Linux Hardening

You now possess practical skills required to deploy enterprise-grade File Integrity Monitoring solutions using open-source Linux security tools.

---

<div align="center">

## 🔐 Secure Systems • Detect Threats • Protect Assets

### ⭐ If this lab helped you, consider starring the repository!

</div>
