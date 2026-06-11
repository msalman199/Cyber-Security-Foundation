# 🔍 Linux Forensics Automation 

<div align="center">

![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![Python](https://img.shields.io/badge/Python-Forensics-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Forensics-red?style=for-the-badge&logo=hackthebox&logoColor=white)
![Incident Response](https://img.shields.io/badge/Incident_Response-Automation-blue?style=for-the-badge)

</div>

---

# 🎯Overview

This lab introduces **Linux Forensics Automation** through hands-on collection, analysis, and reporting of forensic evidence from Linux systems.

Students will learn how to:

- 🔎 Collect forensic artifacts
- 📜 Analyze authentication logs
- 🌐 Investigate network activity
- ⚙️ Automate forensic workflows
- 🛡️ Detect unauthorized activities
- 📊 Generate forensic reports

---

# 🎓 Learning Objectives

By completing this lab, students will be able to:

✅ Extract and analyze system logs

✅ Collect process information

✅ Investigate network connections

✅ Create automated Bash forensic collectors

✅ Develop Python forensic analyzers

✅ Detect suspicious activities

✅ Generate professional forensic reports

✅ Implement incident response workflows

---

# 📚 Prerequisites

Before starting this lab, students should have:

- Basic Linux command-line proficiency
- Understanding of Linux file systems
- Familiarity with system logs
- Basic Bash scripting knowledge
- Basic Python programming knowledge
- Understanding of cybersecurity fundamentals

---

# 🖥️ Lab Environment

Al Nafi provides pre-configured Ubuntu cloud machines containing:

- Ubuntu Linux
- Root access
- Forensic tools installed
- Sample logs
- Python 3.x
- Bash Shell
- Network analysis utilities

---

# 📁 Task 1: Manual Forensic Data Collection

---

## 🔹 Step 1.1: Create Forensic Directory Structure

```bash
mkdir -p /home/forensics/{logs,processes,network,scripts,analysis}
cd /home/forensics

mkdir -p logs/{system,auth,application}
mkdir -p processes/{running,historical}
mkdir -p network/{connections,traffic}

tree /home/forensics || ls -R /home/forensics
```

---

## 🔹 Step 1.2: Extract System and Authentication Logs

```bash
cd /home/forensics/logs/system

echo "=== LOG EXTRACTION: $(date) ===" > extraction_log.txt

cp /var/log/syslog ./syslog_backup.log 2>/dev/null || echo "Syslog not found"
cp /var/log/kern.log ./kernel_backup.log 2>/dev/null || echo "Kernel log not found"

tail -n 1000 /var/log/syslog > recent_syslog.txt 2>/dev/null

journalctl --since "24 hours ago" > systemd_journal_24h.txt 2>/dev/null
```

### Authentication Logs

```bash
cd /home/forensics/logs/auth

cp /var/log/auth.log ./auth_backup.log 2>/dev/null || echo "Auth log not found"

grep "Failed password" /var/log/auth.log > failed_logins.txt

grep "Accepted password" /var/log/auth.log > successful_logins.txt

grep "sudo:" /var/log/auth.log > sudo_usage.txt
```

---

## 🔹 Step 1.3: Extract Process Information

```bash
cd /home/forensics/processes/running

ps aux > running_processes_$(date +%Y%m%d_%H%M%S).txt

pstree -p > process_tree.txt

ps -eo pid,ppid,cmd,etime,user,group > detailed_processes.txt

ps aux --sort=-%cpu > processes_by_cpu.txt

ps aux --sort=-%mem > processes_by_memory.txt

netstat -tulpn > network_processes.txt 2>/dev/null || ss -tulpn > network_processes.txt

lsof > open_files.txt
```

---

## 🔹 Step 1.4: Extract Network Information

```bash
cd /home/forensics/network/connections

netstat -an > all_connections.txt 2>/dev/null || ss -an > all_connections.txt

netstat -tln > listening_tcp.txt 2>/dev/null || ss -tln > listening_tcp.txt

netstat -uln > listening_udp.txt 2>/dev/null || ss -uln > listening_udp.txt

route -n > routing_table.txt 2>/dev/null || ip route > routing_table.txt

arp -a > arp_table.txt 2>/dev/null || ip neigh > arp_table.txt

ifconfig > interface_config.txt 2>/dev/null || ip addr show > interface_config.txt

iptables -L -n -v > firewall_rules.txt
```

---

## 🔹 Step 1.5: Collect System Information

```bash
mkdir -p /home/forensics/system_info

cd /home/forensics/system_info
```

### System Overview

```bash
{
echo "=== SYSTEM INFORMATION ==="
echo "Hostname: $(hostname)"
echo "Kernel: $(uname -a)"
echo "OS: $(cat /etc/os-release | grep PRETTY_NAME)"
echo "Uptime: $(uptime)"
echo "Date: $(date)"
} > system_overview.txt
```

### User Information

```bash
{
echo "=== USER INFORMATION ==="
who
echo ""
last | head -20
} > user_info.txt
```

### Hardware Information

```bash
{
echo "=== HARDWARE INFO ==="
lscpu | head -10
echo ""
free -h
echo ""
df -h
} > hardware_info.txt
```

---

# 🤖 Task 2: Automate Forensic Collection

---

## 🔹 Step 2.1: Bash Forensic Collector

Create:

```bash
cd /home/forensics/scripts

nano forensic_collector.sh
```

### forensic_collector.sh

```bash
#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

print_status() {
 echo -e "${GREEN}[INFO]${NC} $1"
}

TIMESTAMP=$(date +%Y%m%d_%H%M%S)

FORENSIC_DIR="/home/forensics/automated_collection_$TIMESTAMP"

mkdir -p "$FORENSIC_DIR"/{system_info,logs,processes,network,users}

print_status "Starting Collection"

uname -a > "$FORENSIC_DIR/system_info/system_overview.txt"

hostname >> "$FORENSIC_DIR/system_info/system_overview.txt"

uptime >> "$FORENSIC_DIR/system_info/system_overview.txt"

who > "$FORENSIC_DIR/users/user_info.txt"

last >> "$FORENSIC_DIR/users/user_info.txt"

cat /etc/passwd >> "$FORENSIC_DIR/users/user_info.txt"

ps aux > "$FORENSIC_DIR/processes/processes.txt"

pstree -p > "$FORENSIC_DIR/processes/process_tree.txt"

netstat -tulpn > "$FORENSIC_DIR/network/network_connections.txt" 2>/dev/null || ss -tulpn > "$FORENSIC_DIR/network/network_connections.txt"

cp /var/log/auth.log "$FORENSIC_DIR/logs/" 2>/dev/null

FILE_COUNT=$(find "$FORENSIC_DIR" | wc -l)

TOTAL_SIZE=$(du -sh "$FORENSIC_DIR" | cut -f1)

{
echo "Collection Date: $(date)"
echo "System Name: $(hostname)"
echo "File Count: $FILE_COUNT"
echo "Total Size: $TOTAL_SIZE"
} > "$FORENSIC_DIR/summary.txt"

tar -czf "forensic_collection_$TIMESTAMP.tar.gz" "$FORENSIC_DIR"

print_status "Collection Completed"
```

---

### Make Executable

```bash
chmod +x forensic_collector.sh
```

### Run

```bash
./forensic_collector.sh
```

---

## 🔹 Step 2.2: Python Forensic Analyzer

Create:

```bash
nano forensic_analyzer.py
```

### forensic_analyzer.py

```python
#!/usr/bin/env python3

import os
import json
import datetime
from collections import defaultdict

class LinuxForensicAnalyzer:

    def __init__(self, data_directory):
        self.data_dir = data_directory
        self.analysis_results = {}
        self.suspicious_activities = []

    def analyze_auth_logs(self, auth_log):

        failed_logins = defaultdict(int)

        if not os.path.exists(auth_log):
            return

        with open(auth_log, "r", errors="ignore") as f:
            for line in f:
                if "Failed password" in line:
                    parts = line.split()
                    ip = parts[-4] if len(parts) > 5 else "Unknown"
                    failed_logins[ip] += 1

        self.analysis_results["failed_logins"] = dict(failed_logins)

        for ip,count in failed_logins.items():
            if count > 10:
                self.suspicious_activities.append(
                    f"Possible brute-force attack from {ip}"
                )

    def generate_report(self):

        report = {
            "timestamp": datetime.datetime.now().isoformat(),
            "results": self.analysis_results,
            "suspicious": self.suspicious_activities
        }

        with open("forensic_report.json","w") as f:
            json.dump(report,f,indent=4)

        print("Report Generated")

if __name__ == "__main__":

    analyzer = LinuxForensicAnalyzer("/home/forensics")

    analyzer.analyze_auth_logs(
        "/var/log/auth.log"
    )

    analyzer.generate_report()
```

---

### Execute

```bash
chmod +x forensic_analyzer.py

python3 forensic_analyzer.py
```

---

# 🚨 Task 3: Detect Unauthorized Activities

---

## 🔹 Step 3.1 Create Simulated Threats

```bash
nano create_test_activities.sh
```

```bash
#!/bin/bash

for i in {1..15}
do
 echo "$(date) sshd[$$]: Failed password for invalid user admin from 192.168.1.100 port 22" >> /tmp/test_auth.log
done

nc -l 4444 &
NC_PID=$!

mkdir -p /tmp/suspicious_test

echo "test backdoor" > /tmp/suspicious_test/backdoor.sh

chmod +x /tmp/suspicious_test/backdoor.sh

echo "Cleanup:"
echo "kill $NC_PID"
```

Run:

```bash
chmod +x create_test_activities.sh

./create_test_activities.sh
```

---

## 🔹 Step 3.2 Detection Script

```bash
nano detect_unauthorized.sh
```

```bash
#!/bin/bash

ANALYSIS_DIR="/home/forensics/unauthorized_analysis_$(date +%Y%m%d_%H%M%S)"

mkdir -p "$ANALYSIS_DIR"

echo "=== Unauthorized Activity Detection ===" > "$ANALYSIS_DIR/findings.txt"

FAILED=$(grep -c "Failed password" /var/log/auth.log 2>/dev/null)

echo "Failed Logins: $FAILED" >> "$ANALYSIS_DIR/findings.txt"

ps aux | egrep "nc|netcat|ncat|socat" >> "$ANALYSIS_DIR/findings.txt"

ss -tln | egrep "4444|5555|6666|1234|31337" >> "$ANALYSIS_DIR/findings.txt"

find /tmp -iname "*backdoor*" >> "$ANALYSIS_DIR/findings.txt"

echo "Analysis Completed"
```

Run:

```bash
chmod +x detect_unauthorized.sh

./detect_unauthorized.sh
```

---

# 📊 Task 4: Generate Forensic Reports

---

## 🔹 Report Generator Script

```bash
nano generate_report.sh
```

### generate_report.sh

```bash
#!/bin/bash

REPORT_DIR="/home/forensics/reports"

mkdir -p "$REPORT_DIR"

REPORT_FILE="$REPORT_DIR/forensic_report_$(date +%Y%m%d_%H%M%S).txt"

{
echo "==============================="
echo " Linux Forensics Report"
echo "==============================="
echo "Date: $(date)"
echo "Hostname: $(hostname)"
echo ""

echo "Executive Summary"
echo "-----------------"
echo "Automated forensic analysis completed."

echo ""
echo "Recommendations"
echo "---------------"
echo "1. Review suspicious processes"
echo "2. Review failed logins"
echo "3. Audit network connections"
echo "4. Harden firewall policies"

} > "$REPORT_FILE"

echo "Report generated: $REPORT_FILE"
```

Run:

```bash
chmod +x generate_report.sh

./generate_report.sh
```

---

# ✅ Expected Outcomes

After completing this lab you will have:

- 🔍 Complete forensic evidence collection
- 🤖 Automated Bash forensic workflows
- 🐍 Python-based forensic analysis
- 🚨 Unauthorized activity detection
- 📊 Security reporting capabilities
- 🛡️ Linux incident response experience

---

# 🛠 Troubleshooting

### Permission Denied

```bash
sudo ./script.sh
```

### netstat Missing

```bash
sudo apt install net-tools
```

### Python Errors

```bash
python3 --version
```

```bash
chmod +x forensic_analyzer.py
```

### Missing Logs

```bash
sudo journalctl
```

```bash
ls /var/log
```

---

# 📖 Key Takeaways

✅ Evidence collection must be systematic

✅ Automation improves consistency

✅ Logs provide critical forensic evidence

✅ Network monitoring reveals suspicious activity

✅ Reporting is essential for incident response

✅ Linux forensic skills are valuable for SOC and DFIR roles

---

# 🚀 Real-World Applications

- Security Operations Center (SOC)
- Digital Forensics
- Incident Response
- Threat Hunting
- Malware Investigation
- Compliance Auditing
- Enterprise Security Monitoring

---

# 🎉 Conclusion

This Linux Forensics Automation Lab provides practical experience in forensic evidence collection, automation, threat detection, and reporting. By combining Bash scripting, Python analysis, and Linux investigative techniques, students develop foundational Digital Forensics and Incident Response (DFIR) skills used by cybersecurity professionals in real-world environments.

---

## 👨‍💻 Author

**Hafiz Muhammad Salman**

Cloud • DevOps • Cybersecurity • DFIR • Linux Administration
