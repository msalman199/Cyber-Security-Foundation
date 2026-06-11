# 🛡️ Windows Security Hardening Lab

<div align="center">

# 🔐 Windows Security Hardening Simulation on Linux

### Security Monitoring • PowerShell Automation • Log Analysis • Change Detection

![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge\&logo=ubuntu\&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-Core-5391FE?style=for-the-badge\&logo=powershell\&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=for-the-badge\&logo=gnubash\&logoColor=white)
![Security](https://img.shields.io/badge/Security-Hardening-red?style=for-the-badge\&logo=securityscorecard\&logoColor=white)
![Monitoring](https://img.shields.io/badge/System-Monitoring-blue?style=for-the-badge)
![Logs](https://img.shields.io/badge/Log-Analysis-orange?style=for-the-badge)

</div>

---

# 📖 Overview

This lab demonstrates how to perform **Windows Security Hardening concepts** using a Linux-based environment.

The project covers:

✅ Security Policy Configuration

✅ PowerShell Automation

✅ Scheduled Security Tasks

✅ Log Monitoring & Analysis

✅ File Integrity Monitoring

✅ Real-Time Threat Detection

✅ Unauthorized Change Detection

✅ Automated Security Reporting

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

* Configure security policies using PowerShell Core
* Create and manage scheduled monitoring tasks
* Monitor authentication and system logs
* Detect unauthorized system modifications
* Implement file integrity monitoring
* Generate automated security reports
* Build a basic Security Operations workflow

---

# 📋 Prerequisites

* Basic Linux command-line knowledge
* Familiarity with Nano or Vim
* Understanding of Linux permissions
* Basic PowerShell concepts
* Basic Bash scripting knowledge

---

# ☁️ Lab Environment

The lab is performed in an Al Nafi Cloud Linux Environment containing:

| Tool            | Purpose                  |
| --------------- | ------------------------ |
| PowerShell Core | Windows-style automation |
| Bash            | Security scripting       |
| Cron            | Task scheduling          |
| jq              | JSON processing          |
| Netstat         | Network monitoring       |
| System Logs     | Security analysis        |

---

# 📁 Project Structure

```text
security-lab/
│
├── scripts/
│   ├── security-config.ps1
│   ├── create-scheduled-tasks.ps1
│   ├── security-log-monitor.sh
│   ├── file-integrity-check.sh
│   ├── advanced-log-monitor.sh
│   ├── realtime-monitor.sh
│   ├── change-detector.sh
│   └── security-report.sh
│
├── config/
│   ├── security-config.json
│   ├── registry-security.json
│   ├── scheduled-tasks.json
│   ├── crontab-security
│   └── baselines/
│
├── logs/
│
└── monitoring/
```

---

# 🚀 Task 1 — Configure Security Policies

## 🔹 Verify PowerShell Installation

```bash
pwsh --version

mkdir -p ~/security-lab/{scripts,logs,config,monitoring}

cd ~/security-lab
```

---

## 🔹 Create Security Configuration Script

### File

```text
scripts/security-config.ps1
```

### Features

✔ Password Complexity Enforcement

✔ Minimum Password Length

✔ Account Lockout Protection

✔ Password Expiration Policy

✔ Audit Logging Configuration

✔ Firewall Enforcement

### Example Policies

```powershell
$SecurityPolicies = @{
    PasswordComplexity      = $true
    MinPasswordLength       = 12
    AccountLockoutThreshold = 5
    MaxPasswordAge          = 90
    AuditLogonEvents        = $true
    FirewallStatus          = "Enabled"
}
```

---

## 🔹 Execute Script

```bash
chmod +x scripts/security-config.ps1

pwsh scripts/security-config.ps1
```

---

## 🔹 Verify Output

```bash
cat config/security-config.json

jq . config/security-config.json

cat config/registry-security.json
```

---

# 🔐 Task 2 — Create Scheduled Security Tasks

---

## 🔹 Create Scheduled Task Definitions

### File

```text
scripts/create-scheduled-tasks.ps1
```

### Tasks Created

| Task                       | Purpose                     |
| -------------------------- | --------------------------- |
| SecurityLogMonitor         | Monitor security logs       |
| FileIntegrityCheck         | Detect file changes         |
| UnauthorizedChangeDetector | Detect system modifications |
| SecurityReportGenerator    | Generate reports            |

---

### Example Task

```powershell
@{
 Name = "SecurityLogMonitor"
 Description = "Monitor security logs"
 Schedule = "Daily"
 Script = "security-log-monitor.sh"
 Status = "Enabled"
}
```

---

## 🔹 Generate Cron Schedule

Example:

```cron
0 2 * * * /path/to/security-log-monitor.sh
0 3 * * * /path/to/file-integrity-check.sh
0 4 * * * /path/to/change-detector.sh
0 5 * * * /path/to/security-report.sh
```

---

# 📊 Task 3 — Security Log Monitoring

---

## 🔹 Security Log Monitor

### File

```text
scripts/security-log-monitor.sh
```

### Monitoring Activities

* Authentication Failures
* Failed Logins
* System Errors
* Warning Messages
* Active Network Connections

### Example Commands

```bash
grep "authentication failure" /var/log/auth.log

grep -Ei "error|warning" /var/log/syslog

netstat -tuln
```

---

## 🔹 File Integrity Checker

### File

```text
scripts/file-integrity-check.sh
```

### Critical Files Monitored

```bash
/etc/passwd
/etc/shadow
/etc/sudoers
/etc/ssh/sshd_config
```

### Hash Verification

```bash
sha256sum /etc/passwd
```

---

## 🔹 Make Scripts Executable

```bash
chmod +x scripts/security-log-monitor.sh

chmod +x scripts/file-integrity-check.sh
```

---

# 📈 Task 4 — Advanced Log Analysis

---

## 🔹 Advanced Log Monitoring

### File

```text
scripts/advanced-log-monitor.sh
```

### Analysis Functions

### Authentication Analysis

```bash
grep "authentication failure" /var/log/auth.log | wc -l

grep "session opened" /var/log/auth.log | wc -l
```

---

### System Analysis

```bash
grep -i error /var/log/syslog

grep -i warning /var/log/syslog
```

---

### Process Analysis

```bash
ps aux --sort=-%cpu

netstat -tuln | grep LISTEN
```

---

### Disk Analysis

```bash
df -h
```

Detect disks above:

```text
90% utilization
```

---

# ⚡ Real-Time Monitoring

---

## 🔹 Realtime Monitor

### File

```text
scripts/realtime-monitor.sh
```

### Monitors

✔ Authentication Failures

✔ Invalid Users

✔ System Errors

✔ Critical Events

✔ High System Load

---

### Real-Time Log Monitoring

```bash
tail -f /var/log/auth.log

tail -f /var/log/syslog
```

---

# 🚨 Task 5 — Unauthorized Change Detection

---

## 🔹 Change Detection Script

### File

```text
scripts/change-detector.sh
```

### Checks

* Critical File Changes
* User Account Changes
* Service Changes
* Network Configuration Changes

---

## 🔹 File Metadata Monitoring

```bash
stat -c "%Y %s %a" /etc/passwd
```

---

## 🔹 User Change Detection

```bash
sha256sum /etc/passwd

sha256sum /etc/shadow
```

---

## 🔹 Network Change Detection

```bash
sha256sum /etc/hosts
```

---

## 🔹 Running Services

```bash
systemctl list-units --type=service --state=running
```

---

# 📑 Task 6 — Security Report Generator

---

## 🔹 Report Script

### File

```text
scripts/security-report.sh
```

### Generates

✔ HTML Security Report

✔ Security Configuration Summary

✔ Monitoring Summary

✔ Alert Statistics

✔ System Status

✔ Disk Usage

✔ Memory Usage

✔ Load Average

---

## 🔹 Generate Report

```bash
chmod +x scripts/security-report.sh

./scripts/security-report.sh
```

---

## 🔹 Example Report

```text
security-report-YYYYMMDD-HHMM.html
```

---

# 🧪 Testing Change Detection

---

## Create Baselines

```bash
./scripts/change-detector.sh
```

---

## Modify File

```bash
echo "127.0.0.1 test.local" | sudo tee -a /etc/hosts
```

---

## Detect Change

```bash
./scripts/change-detector.sh
```

---

## Generate Report

```bash
./scripts/security-report.sh
```

---

# ✅ Expected Outcomes

After completing the lab:

### Configuration Files

* security-config.json
* registry-security.json

### Scheduled Tasks

* Scheduled monitoring jobs
* Automated cron entries

### Monitoring

* Authentication monitoring
* System event monitoring

### Change Detection

* Baseline creation
* Integrity verification

### Security Reports

* HTML reports
* Security summaries

---

# ✔ Verification Checklist

* [x] Security configuration files created
* [x] Monitoring scripts executable
* [x] Log files generated
* [x] Baselines created
* [x] Security reports generated
* [x] Change detection functioning

---

# 🛠 Troubleshooting

## PowerShell Permission Errors

```bash
chmod +x script.ps1
```

Verify:

```bash
pwsh --version
```

---

## Authentication Logs Missing

Use:

```bash
sudo grep "authentication failure" /var/log/auth.log
```

---

## False Positives

Recreate baselines:

```bash
rm -rf config/baselines/*
```

Then run:

```bash
./scripts/change-detector.sh
```

---

## Invalid JSON

Validate:

```bash
jq . config/security-config.json

jq . config/registry-security.json
```

---

## Cron Issues

Check:

```bash
systemctl status cron
```

Review logs:

```bash
grep CRON /var/log/syslog
```

---

# 🏆 Key Security Concepts Learned

### 🔐 Defense in Depth

Multiple security layers provide stronger protection.

### 📊 Continuous Monitoring

Security events should be monitored continuously.

### 🚨 Early Threat Detection

Automated alerts reduce response time.

### 🔍 Integrity Verification

Critical files must be protected against unauthorized modifications.

### 📑 Security Reporting

Regular reports improve visibility and compliance.

### ⚙️ Automation

Security automation reduces human error.

---

# 📚 Best Practices

✅ Maintain file integrity baselines

✅ Log all security events

✅ Use strong password policies

✅ Monitor authentication activity

✅ Automate recurring security tasks

✅ Generate regular reports

✅ Review security configurations frequently

✅ Keep documentation updated

---

# 🎓 Conclusion

This lab provided hands-on experience implementing a comprehensive Windows Security Hardening simulation within a Linux environment. Using PowerShell Core and Bash scripting, security policies were configured, monitoring systems were automated, file integrity controls were established, and detailed security reporting mechanisms were implemented.

These skills form a strong foundation for careers in:

* Cyber Security
* SOC Operations
* System Administration
* Blue Team Operations
* Security Engineering
* Threat Detection & Monitoring

---

<div align="center">

### 🛡️ Security Is A Continuous Process, Not A One-Time Task

⭐ If you found this project useful, consider giving it a star on GitHub!

</div>
