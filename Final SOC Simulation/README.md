# 🛡️ SOC Simulation Lab — Complete Security Operations Center Build

![SOC](https://img.shields.io/badge/SOC-Security%20Operations%20Center-red?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu_20.04+-E95420?style=for-the-badge&logo=ubuntu)
![Python](https://img.shields.io/badge/Python-Automation-blue?style=for-the-badge&logo=python)
![Suricata](https://img.shields.io/badge/Suricata-NIDS-orange?style=for-the-badge)
![Fail2Ban](https://img.shields.io/badge/Fail2Ban-Intrusion%20Prevention-purple?style=for-the-badge)

---

# 🚀 Final SOC Simulation 

This lab builds a **complete SOC (Security Operations Center)** including:

- 🔍 Log aggregation & analysis
- 🧠 Threat detection rules
- ⚡ Automated response system
- 📡 Network intrusion detection (Suricata)
- 🚫 IP blocking (iptables + Fail2Ban)
- 📑 Incident response playbooks
- 🤖 SOC automation engine

---

# 🎯 Objectives

By completing this lab, you will:

✔ Integrate multiple security tools into a SOC  
✔ Implement automated threat detection rules  
✔ Analyze multi-source security logs  
✔ Build incident response playbooks  
✔ Automate threat containment & remediation  

---

# 📌 Prerequisites

- Linux command line basics  
- Network security fundamentals  
- Log file analysis knowledge  
- Python or Bash scripting  
- Understanding of cyber attacks  

---

# 🖥️ LAB ENVIRONMENT

- Ubuntu 20.04 LTS (Cloud VM)
- 4GB RAM minimum
- 20GB disk
- Python 3 installed
- rsyslog, iptables preinstalled

---

# ⚙️ TASK 1 — SOC Infrastructure Setup

---

## 📦 Step 1: Install Security Tools

```bash
sudo apt update && sudo apt upgrade -y

sudo apt install -y suricata fail2ban rsyslog python3-pip jq

suricata --version
fail2ban-client version
📁 Step 2: SOC Directory Structure
sudo mkdir -p /opt/soc/{logs,scripts,playbooks,alerts,reports}
sudo chown -R $USER:$USER /opt/soc
📡 Step 3: Centralized Logging
sudo tee /etc/rsyslog.d/50-soc.conf << 'EOF'
*.* /opt/soc/logs/system.log
auth.* /opt/soc/logs/auth.log
EOF

sudo systemctl restart rsyslog
🌐 Step 4: Suricata Network Monitoring
sudo tee /etc/suricata/suricata.yaml << 'EOF'
vars:
  address-groups:
    HOME_NET: "[192.168.0.0/16,10.0.0.0/8,172.16.0.0/12]"
    EXTERNAL_NET: "!$HOME_NET"

default-log-dir: /opt/soc/logs/

outputs:
  - eve-log:
      enabled: yes
      filename: suricata-eve.json
      types:
        - alert
        - http
        - dns

af-packet:
  - interface: eth0

rule-files:
  - suricata.rules
EOF
sudo suricata-update
sudo systemctl enable suricata
sudo systemctl start suricata
⚠️ TASK 2 — Threat Detection System
🧠 Step 1: Custom Suricata Rules
sudo tee /etc/suricata/rules/custom.rules << 'EOF'
alert tcp any any -> $HOME_NET 22 (msg:"SSH Brute Force"; flow:established; threshold:type both, track by_src, count 5, seconds 60; sid:1000001;)

alert http any any -> $HOME_NET any (msg:"Web Shell Detected"; content:"cmd="; http_uri; sid:1000002;)

alert tcp any any -> $HOME_NET any (msg:"Port Scan"; flags:S; threshold:type both, track by_src, count 10, seconds 10; sid:1000003;)
EOF
echo "include: /etc/suricata/rules/custom.rules" | sudo tee -a /etc/suricata/suricata.yaml
sudo systemctl restart suricata
🧾 Step 2: SOC Log Analyzer (Python)
#!/usr/bin/env python3
import json
import re
from collections import defaultdict

class SOCAnalyzer:

    def __init__(self):
        self.alerts = []

    def analyze_auth_logs(self, log_file):
        failed = defaultdict(int)

        # TODO: Parse authentication logs
        # TODO: Count failed login attempts per IP
        # TODO: Generate brute-force alerts
        pass

    def analyze_suricata_logs(self, log_file):
        # TODO: Parse JSON logs
        # TODO: Extract alerts
        # TODO: Store into self.alerts
        pass

    def generate_report(self):
        # TODO: Build SOC report
        report = {
            "total_alerts": len(self.alerts),
            "alerts": self.alerts
        }

        return report


if __name__ == "__main__":
    analyzer = SOCAnalyzer()
    analyzer.analyze_auth_logs("/opt/soc/logs/auth.log")
    analyzer.analyze_suricata_logs("/opt/soc/logs/suricata-eve.json")
    print(analyzer.generate_report())
🛡️ Step 3: Fail2Ban Setup
sudo tee /etc/fail2ban/jail.local << 'EOF'
[sshd]
enabled = true
port = ssh
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
findtime = 600
EOF

sudo systemctl restart fail2ban
🚨 TASK 3 — Incident Response Automation
🚫 Step 1: IP Blocking Script
tee /opt/soc/scripts/block_ip.sh << 'EOF'
#!/bin/bash

IP=$1
REASON=$2

if [ -z "$IP" ]; then
    echo "Usage: block_ip.sh <IP> <REASON>"
    exit 1
fi

# TODO: Validate IP format
# TODO: Apply iptables rule
# TODO: Log action

echo "Blocking IP: $IP for $REASON"
EOF

chmod +x /opt/soc/scripts/block_ip.sh
🚨 Step 2: Alert System (Python)
#!/usr/bin/env python3
import sys
import json
from datetime import datetime

def send_alert(alert_type, message):
    """
    TODO:
    - Create structured alert
    - Save JSON alert file
    - Append to log file
    - Assign severity level
    """
    pass


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: send_alert.py TYPE MESSAGE")
        sys.exit(1)

    send_alert(sys.argv[1], sys.argv[2])
🤖 Step 3: Response Engine
#!/usr/bin/env python3
import subprocess
import time

class ResponseEngine:

    def __init__(self):
        self.blocked_ips = set()

    def process_alert(self, alert):
        # TODO: Parse alert
        # TODO: Decide response action
        pass

    def execute_ip_block(self, ip, reason):
        subprocess.run(["/opt/soc/scripts/block_ip.sh", ip, reason])
        self.blocked_ips.add(ip)

    def monitor_alerts(self):
        print("SOC Response Engine Running...")

        while True:
            # TODO: Monitor alerts file
            time.sleep(30)


if __name__ == "__main__":
    engine = ResponseEngine()
    engine.monitor_alerts()
📘 TASK 4 — Incident Response Playbooks
📄 Brute Force Playbook
# 🔐 Brute Force Attack Response

## Type
- Authentication Attack

## Detection
- 5+ failed logins in 5 minutes

## Response

### Immediate
- Identify IP
- Block IP
- Check login success

### Containment
- Reset passwords
- Enable MFA
- Monitor logs

### Recovery
- Document incident
- Update rules
🌐 Web Attack Playbook
# 🌐 Web Attack Response

## Type
- Web Exploitation

## Indicators
- cmd= injection
- SQLi patterns
- suspicious uploads

## Actions
- Block IP
- Inspect logs
- Patch system
- Restore backup
📊 Playbook Tracker
#!/usr/bin/env python3

class PlaybookTracker:

    def start_playbook(self, incident_type, incident_id):
        # TODO
        pass

    def log_step(self, exec_id, step, status):
        # TODO
        pass

    def complete_playbook(self, exec_id, outcome):
        # TODO
        pass
🧪 TASK 5 — SOC Testing & Validation
💣 Simulate Attack
for i in {1..6}; do
    ssh fakeuser@localhost
done
📊 Run SOC Pipeline
python3 /opt/soc/scripts/log_analyzer.py
python3 /opt/soc/scripts/response_engine.py &
🔍 Verify Results
sudo iptables -L -n
cat /opt/soc/logs/blocked_ips.log
cat /opt/soc/alerts/all_alerts.log
sudo fail2ban-client status sshd
📂 FINAL SOC ARCHITECTURE
/opt/soc/
│
├── logs/
├── scripts/
│   ├── log_analyzer.py
│   ├── block_ip.sh
│   ├── response_engine.py
│   └── send_alert.py
│
├── playbooks/
│   ├── brute_force_response.md
│   └── web_attack_response.md
│
├── alerts/
└── reports/
🎯 EXPECTED OUTCOMES

✔ Full SOC pipeline
✔ Automated threat detection
✔ Real-time response system
✔ IP blocking automation
✔ Structured incident playbooks

🧠 KEY TAKEAWAYS
SOC = Detection + Response + Automation
Logs are the foundation of security operations
Automation reduces response time
Playbooks ensure consistent incident handling
Multi-tool integration is essential in real SOCs
🛡️ END OF SOC LAB
