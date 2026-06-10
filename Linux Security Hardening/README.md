🛡️ Linux Security Hardening Lab
<div align="center">
Show Image
Show Image
Show Image
Show Image
Show Image
Show Image

A hands-on cybersecurity lab covering firewall management, SSH hardening, log monitoring, and automated security alerting on Ubuntu Linux.

</div>

📋 Table of Contents

🎯 Objectives
✅ Prerequisites
🖥️ Lab Environment
🔥 Task 1 — Configure UFW Firewall
🔐 Task 2 — Secure SSH Settings
📊 Task 3 — Monitor Logs Using Journalctl
🤖 Task 4 — Automate Log Alerts
✔️ Verification & Testing
🛠️ Troubleshooting
🎓 Conclusion


🎯 Objectives
By the end of this lab, students will be able to:

🔥 Configure and manage UFW (Uncomplicated Firewall) to control network traffic
🔑 Secure SSH settings to prevent unauthorized access
📜 Monitor system logs using journalctl for security analysis
🤖 Create automated scripts to monitor and alert on suspicious log activities
🧠 Understand fundamental Linux security hardening principles
✅ Apply best practices for system security configuration


✅ Prerequisites
Before starting this lab, students should have:
RequirementDescription🐧 Linux CLIBasic knowledge of Linux command line operations🔒 PermissionsUnderstanding of file permissions and ownership concepts✏️ Text EditorsFamiliarity with nano, vim, or gedit🌐 NetworkingBasic understanding of ports and protocols📜 Shell ScriptingKnowledge of shell scripting fundamentals

🖥️ Lab Environment
Show Image
Show Image
Show Image

Al Nafi provides ready-to-use Linux cloud machines. Simply click "Start Lab" to access your pre-configured Ubuntu environment — no VM setup required.

Your lab environment includes:

✅ Ubuntu Linux system with root access
✅ Pre-installed security tools and utilities
✅ Network connectivity for testing firewall rules
✅ All necessary packages for completing the lab tasks


🔥 Task 1 — Configure UFW Firewall
Show Image
Show Image
🔹 Subtask 1.1 — Install and Enable UFW
Check if UFW is installed and enable it on your system:
bash# ✅ Check if UFW is installed
sudo ufw --version

# 📦 If not installed, install it
sudo apt update
sudo apt install ufw -y

# 🔍 Check current UFW status
sudo ufw status

# ▶️ Enable UFW firewall
sudo ufw enable

# ✔️ Verify UFW is active
sudo ufw status verbose

🔹 Subtask 1.2 — Configure Basic Firewall Rules
Set up essential firewall rules to secure your system:
bash# 🚫 Set default policies — deny all incoming, allow outgoing
sudo ufw default deny incoming
sudo ufw default allow outgoing

# 🔑 Allow SSH (port 22) — IMPORTANT: Do this first to maintain access
sudo ufw allow ssh
# Alternative: sudo ufw allow 22

# 🌐 Allow HTTP traffic (port 80)
sudo ufw allow http
# Alternative: sudo ufw allow 80

# 🔒 Allow HTTPS traffic (port 443)
sudo ufw allow https
# Alternative: sudo ufw allow 443

# 📋 Check the current rules
sudo ufw status numbered

🔹 Subtask 1.3 — Create Advanced Firewall Rules
Create more specific rules for enhanced security:
bash# 🎯 Allow specific IP address to access SSH
sudo ufw allow from 192.168.1.100 to any port 22

# 📐 Allow a specific port range
sudo ufw allow 8000:8010/tcp

# 🚫 Deny specific port (Telnet)
sudo ufw deny 23

# 🔌 Allow specific service on specific interface
sudo ufw allow in on eth0 to any port 3306

# 📋 View all rules with numbers
sudo ufw status numbered

# 🗑️ Delete a rule by number (example: delete rule number 3)
# sudo ufw delete 3

🔹 Subtask 1.4 — Test Firewall Configuration
Create a script to test your firewall rules:
bash# 📝 Create the test script
nano ~/firewall_test.sh
Add the following content:
bash#!/bin/bash

echo "=== 🔥 UFW Firewall Status Test ==="
echo "Current UFW Status:"
sudo ufw status verbose

echo ""
echo "=== 🌐 Testing Network Connectivity ==="

# Test outgoing connection (should work — outgoing allowed)
echo "Testing outgoing connection to Google:"
ping -c 3 google.com

echo ""
echo "=== 🔍 Checking Open Ports ==="
sudo netstat -tlnp | grep LISTEN

echo ""
echo "=== 📜 UFW Log Check ==="
sudo tail -10 /var/log/ufw.log
Make the script executable and run it:
bashchmod +x ~/firewall_test.sh
./firewall_test.sh

🔐 Task 2 — Secure SSH Settings
Show Image
Show Image
🔹 Subtask 2.1 — Backup and Modify SSH Configuration
Always backup the SSH config before modifying it:
bash# 💾 Create a backup of the original SSH config
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup

# 👁️ View current SSH configuration
sudo nano /etc/ssh/sshd_config

🔹 Subtask 2.2 — Apply SSH Security Hardening
Edit the SSH configuration file with these security improvements:
bashsudo nano /etc/ssh/sshd_config
Find and modify these lines (uncomment and change values as needed):
ini# 🚪 Change default SSH port (optional but recommended)
Port 2222

# 🚫 Disable root login
PermitRootLogin no

# 🔑 Enable public key authentication
PubkeyAuthentication yes

# 🚫 Disable password authentication (after setting up key-based auth)
PasswordAuthentication no

# 🚫 Disable empty passwords
PermitEmptyPasswords no

# 🔢 Set maximum authentication attempts
MaxAuthTries 3

# ⏱️ Set client alive interval (disconnect idle sessions)
ClientAliveInterval 300
ClientAliveCountMax 2

# 🖥️ Disable X11 forwarding if not needed
X11Forwarding no

# 👤 Allow only specific users (replace 'username' with actual username)
AllowUsers username

# 🚫 Disable unused authentication methods
ChallengeResponseAuthentication no
KerberosAuthentication no
GSSAPIAuthentication no

🔹 Subtask 2.3 — Generate SSH Key Pair
Create SSH keys for secure authentication:
bash# 🔑 Generate SSH key pair (RSA 4096-bit)
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# Press Enter to accept default location
# Set a strong passphrase when prompted

# 📋 Display the public key
cat ~/.ssh/id_rsa.pub

# ➕ Add the public key to authorized_keys
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# 🔒 Set proper permissions
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

🔹 Subtask 2.4 — Test SSH Configuration
Before restarting SSH, test the configuration:
bash# ✔️ Test SSH configuration syntax
sudo sshd -t

# 🔄 If no errors, restart SSH service
sudo systemctl restart sshd

# 📊 Check SSH service status
sudo systemctl status sshd

# 🔥 Update UFW rule for new SSH port (if changed)
sudo ufw allow 2222
sudo ufw delete allow ssh
Create an SSH security test script:
bashnano ~/ssh_security_test.sh
Add this content:
bash#!/bin/bash

echo "=== 🔐 SSH Security Configuration Test ==="

echo "SSH Service Status:"
sudo systemctl status sshd --no-pager

echo ""
echo "SSH Configuration Summary:"
echo "Port: $(sudo grep "^Port" /etc/ssh/sshd_config || echo "22 (default)")"
echo "Root Login: $(sudo grep "^PermitRootLogin" /etc/ssh/sshd_config || echo "Not explicitly set")"
echo "Password Auth: $(sudo grep "^PasswordAuthentication" /etc/ssh/sshd_config || echo "Not explicitly set")"
echo "Max Auth Tries: $(sudo grep "^MaxAuthTries" /etc/ssh/sshd_config || echo "Not explicitly set")"

echo ""
echo "SSH Key Information:"
if [ -f ~/.ssh/id_rsa.pub ]; then
    echo "✅ Public key exists:"
    cat ~/.ssh/id_rsa.pub
else
    echo "❌ No SSH public key found"
fi

echo ""
echo "Active SSH Connections:"
who
Make it executable and run:
bashchmod +x ~/ssh_security_test.sh
./ssh_security_test.sh

📊 Task 3 — Monitor Logs Using Journalctl
Show Image
Show Image
Show Image
🔹 Subtask 3.1 — Basic Log Monitoring
Learn to use journalctl for system log analysis:
bash# 📜 View all system logs
sudo journalctl

# 🔄 View logs from current boot
sudo journalctl -b

# ⏪ View logs from previous boot
sudo journalctl -b -1

# 📡 View logs in real-time (like tail -f)
sudo journalctl -f

# 🔍 View logs for specific service (SSH)
sudo journalctl -u sshd

# 📅 View logs for specific time period
sudo journalctl --since "2024-01-01" --until "2024-01-02"

🔹 Subtask 3.2 — Security-Focused Log Analysis
Focus on security-related log entries:
bash# ❌ Check for failed SSH login attempts
sudo journalctl -u sshd | grep "Failed password"

# ✅ Check for successful SSH logins
sudo journalctl -u sshd | grep "Accepted"

# 👤 Check for sudo usage
sudo journalctl | grep sudo

# 🔐 Check for authentication failures
sudo journalctl | grep "authentication failure"

# 🔥 Check UFW firewall logs
sudo journalctl | grep UFW

🔹 Subtask 3.3 — Create Log Analysis Script
Create a comprehensive log analysis script:
bashnano ~/log_analysis.sh
Add this content:
bash#!/bin/bash

echo "=== 📊 Security Log Analysis Report ==="
echo "Generated on: $(date)"
echo "========================================"

echo ""
echo "=== 🔐 SSH Login Analysis ==="
echo "Failed SSH login attempts (last 24 hours):"
sudo journalctl -u sshd --since "24 hours ago" | grep "Failed password" | wc -l

echo ""
echo "Recent failed SSH attempts:"
sudo journalctl -u sshd --since "24 hours ago" | grep "Failed password" | tail -5

echo ""
echo "Successful SSH logins (last 24 hours):"
sudo journalctl -u sshd --since "24 hours ago" | grep "Accepted" | tail -5

echo ""
echo "=== 👤 Sudo Usage Analysis ==="
echo "Sudo commands executed (last 24 hours):"
sudo journalctl --since "24 hours ago" | grep "sudo:" | wc -l

echo ""
echo "Recent sudo usage:"
sudo journalctl --since "24 hours ago" | grep "sudo:" | tail -5

echo ""
echo "=== 🔥 Firewall Activity ==="
echo "UFW blocked connections (last 24 hours):"
sudo journalctl --since "24 hours ago" | grep "UFW BLOCK" | wc -l

echo ""
echo "Recent UFW blocks:"
sudo journalctl --since "24 hours ago" | grep "UFW BLOCK" | tail -5

echo ""
echo "=== 🔑 System Authentication ==="
echo "Authentication failures (last 24 hours):"
sudo journalctl --since "24 hours ago" | grep "authentication failure" | wc -l

echo ""
echo "=== 💽 Disk Usage Check ==="
df -h | grep -E "(Filesystem|/dev/)"

echo ""
echo "=== 🧠 Memory Usage ==="
free -h

echo ""
echo "=== 👥 Current Active Users ==="
who

echo ""
echo "========================================"
echo "✅ Log analysis complete."
Make it executable and run:
bashchmod +x ~/log_analysis.sh
./log_analysis.sh

🤖 Task 4 — Automate Log Alerts
Show Image
Show Image
Show Image
🔹 Subtask 4.1 — Create SSH Intrusion Detection Script
bashnano ~/ssh_monitor.sh
Add this content:
bash#!/bin/bash

# ⚙️ Configuration
ALERT_THRESHOLD=5
LOG_FILE="/var/log/ssh_alerts.log"
EMAIL_ALERT=false  # Set to true if you want email alerts

# 📝 Function to log alerts
log_alert() {
    echo "[$(date)] ALERT: $1" | sudo tee -a $LOG_FILE
}

# 🚨 Function to send alert
send_alert() {
    echo "🚨 SECURITY ALERT: $1"
    log_alert "$1"
}

echo "=== 🔍 SSH Security Monitor ==="
echo "Checking for suspicious SSH activity..."

# 📊 Check for failed login attempts in the last hour
FAILED_ATTEMPTS=$(sudo journalctl -u sshd --since "1 hour ago" | grep "Failed password" | wc -l)

if [ $FAILED_ATTEMPTS -gt $ALERT_THRESHOLD ]; then
    ALERT_MSG="⚠️ High number of failed SSH attempts detected: $FAILED_ATTEMPTS in the last hour"
    send_alert "$ALERT_MSG"

    echo "Suspicious IPs attempting to connect:"
    sudo journalctl -u sshd --since "1 hour ago" | grep "Failed password" | awk '{print $11}' | sort | uniq -c | sort -nr
fi

# ✅ Check for successful logins from new IPs
echo ""
echo "Recent successful SSH logins:"
sudo journalctl -u sshd --since "1 hour ago" | grep "Accepted" | tail -5

# 🚫 Check for root login attempts (should be blocked)
ROOT_ATTEMPTS=$(sudo journalctl -u sshd --since "1 hour ago" | grep "Failed password for root" | wc -l)
if [ $ROOT_ATTEMPTS -gt 0 ]; then
    ALERT_MSG="🔴 Root login attempts detected: $ROOT_ATTEMPTS in the last hour"
    send_alert "$ALERT_MSG"
fi

echo ""
echo "✅ SSH monitoring complete. Check $LOG_FILE for alerts."

🔹 Subtask 4.2 — Create System Resource Monitor
bashnano ~/system_monitor.sh
Add this content:
bash#!/bin/bash

# ⚙️ Configuration
CPU_THRESHOLD=80
MEMORY_THRESHOLD=80
DISK_THRESHOLD=90
LOG_FILE="/var/log/system_alerts.log"

# 📝 Function to log alerts
log_alert() {
    echo "[$(date)] SYSTEM ALERT: $1" | sudo tee -a $LOG_FILE
}

echo "=== 🖥️ System Security Monitor ==="

# 🔥 Check CPU usage
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
CPU_USAGE_INT=$(echo $CPU_USAGE | cut -d'.' -f1)

if [ $CPU_USAGE_INT -gt $CPU_THRESHOLD ]; then
    log_alert "⚠️ High CPU usage detected: ${CPU_USAGE}%"
fi

# 🧠 Check memory usage
MEMORY_USAGE=$(free | grep Mem | awk '{printf("%.0f", $3/$2 * 100.0)}')
if [ $MEMORY_USAGE -gt $MEMORY_THRESHOLD ]; then
    log_alert "⚠️ High memory usage detected: ${MEMORY_USAGE}%"
fi

# 💽 Check disk usage
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | cut -d'%' -f1)
if [ $DISK_USAGE -gt $DISK_THRESHOLD ]; then
    log_alert "⚠️ High disk usage detected: ${DISK_USAGE}%"
fi

# 👀 Check for unusual processes
echo "Top CPU consuming processes:"
ps aux --sort=-%cpu | head -6

# 🔌 Check for listening ports
echo ""
echo "Current listening ports:"
sudo netstat -tlnp | grep LISTEN

# 👤 Check for recent sudo usage
RECENT_SUDO=$(sudo journalctl --since "1 hour ago" | grep "sudo:" | wc -l)
if [ $RECENT_SUDO -gt 10 ]; then
    log_alert "⚠️ High sudo usage detected: $RECENT_SUDO commands in the last hour"
fi

echo ""
echo "✅ System monitoring complete."

🔹 Subtask 4.3 — Create Automated Alert Scheduler
bashnano ~/security_monitor_master.sh
Add this content:
bash#!/bin/bash

SCRIPT_DIR="$HOME"
REPORT_FILE="/tmp/security_report_$(date +%Y%m%d_%H%M%S).txt"

echo "=== 🛡️ Automated Security Monitoring System ===" | tee $REPORT_FILE
echo "Report generated on: $(date)" | tee -a $REPORT_FILE
echo "================================================" | tee -a $REPORT_FILE

# 🔐 Run SSH monitoring
echo "" | tee -a $REPORT_FILE
echo "=== SSH Security Check ===" | tee -a $REPORT_FILE
$SCRIPT_DIR/ssh_monitor.sh | tee -a $REPORT_FILE

# 🖥️ Run system monitoring
echo "" | tee -a $REPORT_FILE
echo "=== System Resource Check ===" | tee -a $REPORT_FILE
$SCRIPT_DIR/system_monitor.sh | tee -a $REPORT_FILE

# 📊 Run log analysis
echo "" | tee -a $REPORT_FILE
echo "=== Log Analysis ===" | tee -a $REPORT_FILE
$SCRIPT_DIR/log_analysis.sh | tee -a $REPORT_FILE

# 🔥 Check firewall status
echo "" | tee -a $REPORT_FILE
echo "=== Firewall Status ===" | tee -a $REPORT_FILE
sudo ufw status verbose | tee -a $REPORT_FILE

# 📋 Summary
echo "" | tee -a $REPORT_FILE
echo "=== ✅ Security Summary ===" | tee -a $REPORT_FILE
echo "All security checks completed successfully." | tee -a $REPORT_FILE
echo "Full report saved to: $REPORT_FILE" | tee -a $REPORT_FILE

echo ""
echo "🎉 Security monitoring complete!"
echo "📄 Detailed report available at: $REPORT_FILE"

🔹 Subtask 4.4 — Set Up Automated Monitoring
Make all scripts executable and configure cron automation:
bash# ✅ Make all scripts executable
chmod +x ~/ssh_monitor.sh
chmod +x ~/system_monitor.sh
chmod +x ~/security_monitor_master.sh

# ▶️ Test the master monitoring script
./security_monitor_master.sh
Create the cron setup script:
bashnano ~/setup_monitoring_cron.sh
Add this content:
bash#!/bin/bash

echo "⚙️ Setting up automated security monitoring..."

# ⏰ Run full security check every hour
(crontab -l 2>/dev/null; echo "0 * * * * $HOME/security_monitor_master.sh") | crontab -

# ⏱️ Run SSH monitoring every 15 minutes
(crontab -l 2>/dev/null; echo "*/15 * * * * $HOME/ssh_monitor.sh") | crontab -

echo "✅ Cron jobs added successfully!"
echo "Current crontab:"
crontab -l

echo ""
echo "📅 Monitoring will run automatically:"
echo "  🔁 Full security check  → Every hour"
echo "  🔁 SSH monitoring       → Every 15 minutes"
echo ""
echo "💡 To remove these cron jobs later, run: crontab -e"
Make it executable:
bashchmod +x ~/setup_monitoring_cron.sh

✔️ Verification & Testing
Show Image
Create a comprehensive verification script:
bashnano ~/security_verification.sh
Add this content:
bash#!/bin/bash

echo "=== 🛡️ Linux Security Hardening Verification ==="
echo "=================================================="

echo ""
echo "1. 🔥 UFW Firewall Status:"
sudo ufw status verbose

echo ""
echo "2. 🔐 SSH Configuration Check:"
echo "SSH Port: $(sudo grep "^Port" /etc/ssh/sshd_config 2>/dev/null || echo "22 (default)")"
echo "Root Login: $(sudo grep "^PermitRootLogin" /etc/ssh/sshd_config 2>/dev/null || echo "Not configured")"
echo "Password Auth: $(sudo grep "^PasswordAuthentication" /etc/ssh/sshd_config 2>/dev/null || echo "Not configured")"

echo ""
echo "3. 📡 SSH Service Status:"
sudo systemctl status sshd --no-pager -l

echo ""
echo "4. 📂 Available Security Scripts:"
ls -la ~/*monitor*.sh ~/log_analysis.sh ~/firewall_test.sh 2>/dev/null

echo ""
echo "5. 📄 Log Files Created:"
ls -la /var/log/*alerts.log 2>/dev/null || echo "No alert logs found yet"

echo ""
echo "6. ⏰ Cron Jobs (Automated Monitoring):"
crontab -l 2>/dev/null || echo "No cron jobs configured"

echo ""
echo "7. 📊 Recent Security Events:"
echo "Failed SSH attempts (last 24h): $(sudo journalctl -u sshd --since "24 hours ago" | grep "Failed password" | wc -l)"
echo "Successful SSH logins (last 24h): $(sudo journalctl -u sshd --since "24 hours ago" | grep "Accepted" | wc -l)"
echo "UFW blocks (last 24h): $(sudo journalctl --since "24 hours ago" | grep "UFW BLOCK" | wc -l)"

echo ""
echo "=================================================="
echo "✅ Security hardening verification complete!"
Make it executable and run:
bashchmod +x ~/security_verification.sh
./security_verification.sh

🛠️ Troubleshooting
❗ Issue 1 — UFW Not Starting
bash# 🔍 Check UFW service status
sudo systemctl status ufw

# 🔄 Restart UFW service
sudo systemctl restart ufw

# ▶️ Enable UFW service at boot
sudo systemctl enable ufw
❗ Issue 2 — SSH Connection Issues After Configuration
bash# ✔️ Check SSH configuration syntax
sudo sshd -t

# 🔄 Restore backup configuration if needed
sudo cp /etc/ssh/sshd_config.backup /etc/ssh/sshd_config
sudo systemctl restart sshd
❗ Issue 3 — Log Files Not Accessible
bash# 🔍 Check log file permissions
ls -la /var/log/

# 📁 Create log directory if needed
sudo mkdir -p /var/log
sudo chmod 755 /var/log

🎓 Conclusion
<div align="center">
🏆 Congratulations on completing the Linux Security Hardening Lab!
</div>
✅ Accomplished Tasks
#TaskDescription🔥UFW FirewallSet up default deny policies, allowing only necessary services🔐SSH HardeningDisabled root login, implemented key-based auth, set connection limits📊Log MonitoringUsed journalctl to track authentication and security events🤖Auto MonitoringBuilt scripts to detect SSH intrusions and generate security alerts

🌍 Why This Matters
These security hardening techniques are fundamental to protecting Linux systems in real-world environments. The skills you've developed are directly applicable to:
Career PathRelevance🛡️ Cybersecurity AnalystEssential knowledge for security professionals🖥️ System AdministratorCore hardening and monitoring skills📋 Compliance EngineerMeets many security framework requirements🎓 Certification PrepAligns with CompTIA, CEH, OSCP exam objectives

🔑 Key Security Principles Applied
🧱 Defense in Depth       →  Multiple layers: firewall + SSH + monitoring
🔒 Least Privilege        →  Allowing only necessary access and services
👁️  Continuous Monitoring  →  Automated detection of suspicious activities
🚨 Incident Response      →  Log analysis and alerting capabilities

<div align="center">
Show Image
Show Image
Show Image

You now have a solid foundation in Linux security hardening that you can build upon as you advance in your cybersecurity journey.

</div>
