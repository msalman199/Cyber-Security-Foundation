# 🛡️ Basic Threat Simulation 

![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Threat%20Simulation-red)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Nmap](https://img.shields.io/badge/Nmap-Network%20Scanning-green)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

# 📖 Overview

The **Basic Threat Simulation Lab** introduces fundamental network reconnaissance and threat assessment techniques using **Nmap** and **Python automation**.

This hands-on lab demonstrates how security professionals perform network discovery, service enumeration, vulnerability identification, and automated reporting while maintaining proper security assessment documentation.

---

# 🎯 Objectives

By completing this lab, I learned how to:

* Understand network reconnaissance techniques
* Perform network scanning using Nmap
* Discover and enumerate open ports
* Identify running network services
* Analyze scan results for potential risks
* Automate scanning tasks with Python
* Log scan results in JSON and CSV formats
* Generate professional security reports
* Create HTML dashboards for scan visualization

---

# 🧰 Technologies Used

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Nmap       | Network Discovery & Enumeration |
| Python 3   | Automation & Reporting          |
| JSON       | Data Storage                    |
| CSV        | Report Export                   |
| HTML/CSS   | Dashboard Visualization         |
| Linux      | Security Testing Environment    |

---

# 🖥️ Lab Environment

The cloud machine included:

* Ubuntu Linux
* Nmap Scanner
* Python 3
* python-nmap Library
* Text Editors
* Local Target Services

---

# 📂 Project Structure

```text
Basic-Threat-Simulation/
│
├── basic_scanner.py
├── advanced_scanner.py
├── generate_dashboard.py
│
├── scan_results_*.json
├── threat_analysis_*.json
├── threat_analysis_*.csv
│
├── security_report_*.txt
├── threat_scan_*.log
│
└── threat_dashboard_*.html
```

---

# 🚀 Task 1 – Nmap Network Scanning

## Verify Nmap Installation

```bash
nmap --version
```

Install if required:

```bash
sudo apt update
sudo apt install nmap -y
```

---

## Start Target Services

```bash
sudo systemctl start ssh
sudo systemctl start apache2
```

Verify services:

```bash
sudo systemctl status ssh
sudo systemctl status apache2
```

---

## Basic Scan

```bash
nmap 127.0.0.1
```

Example Output:

```text
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

---

## Scan All Ports

```bash
nmap -p- 127.0.0.1
```

---

## Fast Scan

```bash
nmap -F 127.0.0.1
```

---

## Specific Ports

```bash
nmap -p 22,80,443,8080 127.0.0.1
```

---

## TCP Scan

```bash
nmap -sS 127.0.0.1
```

---

## UDP Scan

```bash
sudo nmap -sU 127.0.0.1
```

---

## Combined TCP + UDP Scan

```bash
sudo nmap -sS -sU 127.0.0.1
```

---

# 🔍 Task 2 – Service Enumeration

## Service Version Detection

```bash
nmap -sV 127.0.0.1
```

Aggressive Detection:

```bash
nmap -sV --version-intensity 9 127.0.0.1
```

---

## Operating System Detection

```bash
sudo nmap -O 127.0.0.1
```

Combined Scan:

```bash
sudo nmap -O -sV 127.0.0.1
```

---

## Default Script Scan

```bash
nmap -sC 127.0.0.1
```

---

## Vulnerability Scan

```bash
nmap --script vuln 127.0.0.1
```

---

## HTTP Enumeration

```bash
nmap --script http-enum 127.0.0.1
```

---

## Aggressive Enumeration

```bash
sudo nmap -A 127.0.0.1
```

Save Results:

```bash
sudo nmap -A 127.0.0.1 -oA comprehensive_scan
```

Generated Files:

```text
comprehensive_scan.nmap
comprehensive_scan.xml
comprehensive_scan.gnmap
```

---

# 🐍 Task 3 – Python Automation

## Install Python Nmap Library

```bash
pip3 install python-nmap
```

---

# Basic Scanner

## Run Scanner

```bash
python3 basic_scanner.py
```

### Features

* Automated Nmap scans
* Service detection
* JSON output
* Timestamped reports

---

# Advanced Scanner

## Run Scanner

```bash
python3 advanced_scanner.py
```

Verbose Mode:

```bash
python3 advanced_scanner.py 127.0.0.1 -p 1-5000 -f csv -v
```

### Features

* Logging System
* Vulnerability Detection
* Threat Classification
* CSV Export
* JSON Export
* Security Reporting

---

# Threat Categories

| Service | Threat                  |
| ------- | ----------------------- |
| SSH     | Brute Force Risk        |
| HTTP    | Web Vulnerabilities     |
| HTTPS   | TLS Issues              |
| FTP     | Weak Authentication     |
| Telnet  | Cleartext Communication |
| SMTP    | Email Abuse             |

---

# 📊 HTML Dashboard

Generate dashboard:

```bash
python3 generate_dashboard.py
```

Output:

```text
threat_dashboard_YYYYMMDD_HHMMSS.html
```

Dashboard includes:

* Host Information
* Open Ports
* Running Services
* Threat Severity
* Scan Statistics

---

# 📁 Output Files

## JSON Results

```json
{
  "host": "127.0.0.1",
  "state": "up",
  "open_ports": [],
  "potential_threats": []
}
```

---

## CSV Results

```csv
Port,Protocol,Service,Version,Product
22,tcp,ssh,OpenSSH,Ubuntu
80,tcp,http,Apache,Apache2
```

---

## Security Report

```text
BASIC THREAT SIMULATION REPORT

Target: 127.0.0.1
Host State: up

Open Ports: 2

Potential Threats:
1. SSH exposed
2. HTTP exposed
```

---

# ✅ Verification Steps

## Verify Scanner

```bash
python3 basic_scanner.py
```

---

## Validate JSON

```bash
sudo apt install jq -y

jq . threat_analysis_*.json
```

---

## Verify Services

```bash
sudo systemctl status ssh
sudo systemctl status apache2
```

---

## Compare Scan Types

```bash
nmap -F 127.0.0.1

nmap -A 127.0.0.1

nmap -sV 127.0.0.1
```

---

# 🛠️ Troubleshooting

## Nmap Permission Error

```bash
sudo nmap -sU 127.0.0.1
```

---

## Python Module Missing

```bash
pip3 install python-nmap
```

---

## No Services Found

```bash
sudo systemctl start ssh
sudo systemctl start apache2
```

---

## Slow Scans

Use fast mode:

```bash
nmap -F 127.0.0.1
```

---

# 🧪 Lab Exercises

## Exercise 1

Scan only web ports:

```bash
nmap -p 80,443,8080,8443 127.0.0.1
```

---

## Exercise 2

Create a service enumeration script to identify:

* Web Servers
* CMS Platforms
* HTTP Technologies

---

## Exercise 3

Enhance reporting with:

* Risk Ratings
* Security Recommendations
* Vulnerability References

---

# 📚 Key Skills Acquired

### Network Reconnaissance

* Host Discovery
* Port Scanning
* Service Enumeration

### Threat Analysis

* Exposure Assessment
* Service Risk Identification
* Security Evaluation

### Python Automation

* Scan Automation
* Data Parsing
* Logging
* Reporting

### Security Documentation

* Assessment Reports
* JSON Export
* CSV Export
* HTML Dashboards

---

# 🎓 Learning Outcomes

After completing this lab, I can:

✅ Conduct network reconnaissance

✅ Enumerate services and ports

✅ Perform security assessments

✅ Automate scans using Python

✅ Generate professional reports

✅ Visualize security findings

✅ Understand attacker reconnaissance techniques

---

# ⚠️ Ethical Use Notice

This project is intended strictly for:

* Educational Purposes
* Authorized Security Testing
* Cybersecurity Training Labs

Never perform scans against systems without explicit authorization.

Unauthorized scanning may violate laws, regulations, and organizational policies.

---

# 🏆 Conclusion

The **Basic Threat Simulation Lab** provided practical experience in network discovery, service enumeration, threat identification, and security reporting. Through the use of **Nmap**, **Python automation**, and **dashboard generation**, I developed foundational skills required for cybersecurity assessments, penetration testing, and defensive security operations.

These techniques form the basis of professional reconnaissance workflows used by security analysts, penetration testers, and blue team defenders worldwide.
