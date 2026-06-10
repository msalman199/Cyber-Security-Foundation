# 🔍 Port Scanning & Enumeration 

![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?logo=linux)
![Nmap](https://img.shields.io/badge/Nmap-Network%20Mapper-blue)
![Netcat](https://img.shields.io/badge/Netcat-Network%20Testing-green)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Ethical%20Hacking-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

# 📌 Overview

This lab provides hands-on experience with **Port Scanning and Network Enumeration** using industry-standard cybersecurity tools.

Students learn how to identify open ports, discover running services, perform service enumeration, analyze network exposure, and generate security assessment reports using Linux-based tools.

The lab emphasizes ethical hacking principles and safe security testing practices within a controlled environment.

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

* Understand port scanning fundamentals
* Perform network enumeration using Nmap
* Discover open TCP and UDP ports
* Identify running network services
* Use Netcat for service verification
* Analyze listening services on Linux systems
* Perform basic security assessments
* Generate scan reports
* Apply ethical hacking methodologies responsibly

---

# 🛠️ Technologies & Tools Used

| Tool           | Purpose                           |
| -------------- | --------------------------------- |
| Nmap           | Network Discovery & Port Scanning |
| Netcat (nc)    | Connection Testing                |
| Netstat        | Network Statistics                |
| SS             | Socket Statistics                 |
| Linux Terminal | Command Line Operations           |
| Bash           | Automation Scripts                |

---

# 🏗️ Lab Environment

## Al Nafi Cloud Machine

The lab runs entirely on a pre-configured Linux cloud machine.

### Environment Includes

* Ubuntu Linux
* Nmap
* Netcat
* Netstat
* SS Command
* Bash Shell
* Administrative Access

---

# 📚 Task 1: Understanding the Local Environment

## View Network Interfaces

```bash
ip addr show
```

Alternative:

```bash
ifconfig
```

### Purpose

Displays:

* Loopback Interface (lo)
* Main Network Interface (eth0/enp0s3)
* IPv4 Addresses
* IPv6 Addresses

---

## Check Listening Services

Using Netstat:

```bash
netstat -tuln
```

Using SS:

```bash
ss -tuln
```

### Flags Explained

| Flag | Meaning        |
| ---- | -------------- |
| -t   | TCP            |
| -u   | UDP            |
| -l   | Listening      |
| -n   | Numeric Output |

---

# 📚 Task 2: Basic Nmap Port Scanning

## Verify Installation

```bash
nmap --version
```

Install if missing:

```bash
sudo apt update
sudo apt install nmap -y
```

---

## Scan Localhost

Basic Scan:

```bash
nmap 127.0.0.1
```

Scan Specific Ports:

```bash
nmap -p 1-1000 127.0.0.1
```

Service Detection:

```bash
nmap -sV 127.0.0.1
```

### Scan States

| State    | Meaning                     |
| -------- | --------------------------- |
| Open     | Accepting Connections       |
| Closed   | Reachable but Not Listening |
| Filtered | Blocked by Firewall         |

---

## Detailed Enumeration

OS Detection:

```bash
nmap -sV -O 127.0.0.1
```

Aggressive Scan:

```bash
nmap -A 127.0.0.1
```

Scan All Ports:

```bash
nmap -p- 127.0.0.1
```

---

## UDP Scanning

```bash
sudo nmap -sU 127.0.0.1
```

Specific UDP Ports:

```bash
sudo nmap -sU -p 53,67,68,123,161 127.0.0.1
```

---

# 📚 Task 3: Advanced Nmap Techniques

## Stealth Scanning

SYN Scan:

```bash
sudo nmap -sS 127.0.0.1
```

TCP Connect Scan:

```bash
nmap -sT 127.0.0.1
```

ACK Scan:

```bash
sudo nmap -sA 127.0.0.1
```

---

## Nmap Scripting Engine (NSE)

Default Scripts:

```bash
nmap -sC 127.0.0.1
```

List Available Scripts:

```bash
nmap --script-help all | head -20
```

Vulnerability Scripts:

```bash
nmap --script vuln 127.0.0.1
```

HTTP Enumeration:

```bash
nmap --script http-enum 127.0.0.1
```

---

## Saving Scan Results

Normal Format:

```bash
nmap -oN scan_results.txt 127.0.0.1
```

XML Format:

```bash
nmap -oX scan_results.xml 127.0.0.1
```

Grepable Format:

```bash
nmap -oG scan_results.gnmap 127.0.0.1
```

All Formats:

```bash
nmap -oA complete_scan 127.0.0.1
```

View Results:

```bash
cat scan_results.txt
```

---

# 📚 Task 4: Netcat Connection Testing

## Verify Installation

```bash
nc -h
```

Install:

```bash
sudo apt install netcat-openbsd -y
```

---

## Test Connections

SSH Port:

```bash
nc -zv 127.0.0.1 22
```

Port Range:

```bash
nc -zv 127.0.0.1 20-25
```

Timeout Example:

```bash
timeout 5 nc -zv 127.0.0.1 80
```

---

## Banner Grabbing

SSH Banner:

```bash
nc 127.0.0.1 22
```

HTTP Banner:

```bash
echo -e "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n" | nc 127.0.0.1 80
```

Interactive Connection:

```bash
nc -C 127.0.0.1 22
```

---

## Create a Listener

Terminal 1:

```bash
nc -l -p 1234
```

Terminal 2:

```bash
nc 127.0.0.1 1234
```

---

# 📚 Task 5: Service Identification & Analysis

## Service Identification Script

```bash
#!/bin/bash

echo "=== Service Identification Report ==="
echo "Date: $(date)"
echo "Host: $(hostname)"
echo "IP: $(hostname -I)"

echo ""
echo "=== Open TCP Ports ==="
nmap -sT 127.0.0.1 | grep "open"

echo ""
echo "=== Service Versions ==="
nmap -sV 127.0.0.1 | grep -E "(open|Service Info)"

echo ""
echo "=== Listening Services ==="
ss -tuln | grep LISTEN

echo ""
echo "=== Process Information ==="
sudo netstat -tulnp | grep LISTEN
```

Save and Run:

```bash
chmod +x identify_services.sh
./identify_services.sh
```

---

## Port Analysis Script

```bash
#!/bin/bash

echo "=== Port Analysis ==="

declare -A common_ports=(
    [22]="SSH"
    [23]="Telnet"
    [25]="SMTP"
    [53]="DNS"
    [80]="HTTP"
    [110]="POP3"
    [143]="IMAP"
    [443]="HTTPS"
    [993]="IMAPS"
    [995]="POP3S"
)

open_ports=$(nmap -p- --open 127.0.0.1 2>/dev/null | grep "^[0-9]" | cut -d'/' -f1)

for port in $open_ports; do
    service=${common_ports[$port]:-"Unknown"}
    echo "Port $port: $service"
done
```

Run:

```bash
chmod +x analyze_ports.sh
./analyze_ports.sh
```

---

# 📚 Task 6: Security Assessment

## Vulnerability Scanning

```bash
nmap --script vuln 127.0.0.1
```

Authentication Checks:

```bash
nmap --script auth 127.0.0.1
```

Information Gathering:

```bash
nmap --script discovery 127.0.0.1
```

---

## Security Report Generator

```bash
#!/bin/bash

REPORT_FILE="security_report_$(date +%Y%m%d_%H%M%S).txt"

{
echo "=== SECURITY ASSESSMENT REPORT ==="
echo "Generated: $(date)"
echo "Target: localhost (127.0.0.1)"

echo ""
echo "=== OPEN PORTS ==="
nmap --open 127.0.0.1

echo ""
echo "=== SERVICE VERSIONS ==="
nmap -sV 127.0.0.1

echo ""
echo "=== VULNERABILITY SCAN ==="
nmap --script vuln 127.0.0.1

echo ""
echo "=== RECOMMENDATIONS ==="
echo "1. Close unnecessary ports"
echo "2. Update services"
echo "3. Configure firewall rules"
echo "4. Monitor running services"
echo "5. Perform regular assessments"

} > "$REPORT_FILE"

echo "Report saved to $REPORT_FILE"
```

Run:

```bash
chmod +x security_report.sh
./security_report.sh
```

---

# 🔍 Troubleshooting

## Permission Errors

```bash
sudo nmap -sS 127.0.0.1
```

Or:

```bash
nmap -sT 127.0.0.1
```

---

## No Open Ports Found

Start SSH:

```bash
sudo systemctl start ssh
```

Create Test Listener:

```bash
nc -l -p 8080 &
```

---

## Slow Scans

Aggressive Timing:

```bash
nmap -T4 127.0.0.1
```

Insane Timing:

```bash
nmap -T5 127.0.0.1
```

Top Ports Only:

```bash
nmap --top-ports 1000 127.0.0.1
```

---

# ✅ Lab Verification Checklist

* [x] Identify Open Ports
* [x] Discover Running Services
* [x] Perform Service Enumeration
* [x] Capture Service Banners
* [x] Run NSE Scripts
* [x] Generate Security Reports
* [x] Analyze Local Security Posture

---

# 🏆 Skills Gained

### Nmap Mastery

* TCP Scanning
* UDP Scanning
* Version Detection
* OS Detection
* NSE Scripting

### Netcat Usage

* Connection Testing
* Port Verification
* Banner Grabbing
* Listener Creation

### Security Analysis

* Service Enumeration
* Vulnerability Assessment
* Report Generation
* Network Exposure Analysis

---

# 🔐 Why This Matters in Cybersecurity

Port scanning and enumeration are fundamental skills for:

* Penetration Testing
* Vulnerability Assessments
* Threat Hunting
* Security Audits
* Incident Response
* Red Team Operations
* Blue Team Validation

Security professionals use these techniques daily to identify weaknesses before attackers do.

---

# 📈 Next Steps

Continue learning:

* Nmap Advanced Scripting
* Nmap NSE Development
* Network Mapping
* Vulnerability Scanning
* Nessus Essentials
* OpenVAS
* Wireshark
* tcpdump
* Burp Suite
* Ethical Hacking Methodologies

---

# ⚖️ Ethical Use Notice

> Always obtain proper authorization before performing any port scan or enumeration activity against systems or networks that you do not own or manage.

Unauthorized scanning may violate organizational policies, terms of service, or laws.

Use these skills responsibly and ethically.

---

# 🎉 Lab Completed Successfully

**Lab:** Port Scanning & Enumeration
**Platform:** Al Nafi Cloud
**Category:** Cyber Security Foundation
**Status:** ✅ Completed

Keep learning, keep practicing, and continue building your cybersecurity skills.
