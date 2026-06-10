# 🦈 Introduction to Wireshark
> **Cyber Security Foundation Lab**
>
> Learn how to capture, analyze, filter, and investigate network traffic using Wireshark and Tshark.

![Wireshark](https://img.shields.io/badge/Wireshark-Network%20Analysis-blue?style=for-the-badge&logo=wireshark)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge&logo=ubuntu)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Packet%20Analysis-red?style=for-the-badge&logo=securityscorecard)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

---

# 📖 Overview

Wireshark is one of the most powerful network protocol analyzers used by cybersecurity professionals, network engineers, incident responders, and digital forensic analysts.

In this lab you will:

- Capture live network traffic
- Analyze HTTP, TCP, and DNS communications
- Apply packet filters
- Detect suspicious network behavior
- Export and report captured traffic
- Use Tshark for command-line packet analysis

---

# 🎯 Learning Objectives

By the end of this lab, you will be able to:

✅ Install and configure Wireshark

✅ Capture live network traffic

✅ Apply protocol-specific filters

✅ Analyze HTTP, TCP, and DNS packets

✅ Identify suspicious network activities

✅ Export packet captures

✅ Generate analysis reports

✅ Understand packet analysis fundamentals for cybersecurity

---

# 📋 Prerequisites

Before starting:

- Basic Networking Knowledge
- Linux Command Line Experience
- Understanding of:
  - IP Addresses
  - TCP/IP
  - DNS
  - HTTP/HTTPS
- Basic Cybersecurity Concepts

---

# ☁️ Lab Environment

Al Nafi Cloud provides:

| Component | Availability |
|------------|--------------|
| Ubuntu Linux | ✅ |
| Network Access | ✅ |
| Administrative Privileges | ✅ |
| Packet Capture Support | ✅ |
| Internet Connectivity | ✅ |

---

# 🛠️ Task 1: Installing and Configuring Wireshark

## 📌 Subtask 1.1 Install Wireshark

### Update System

```bash
sudo apt update
```

### Install Wireshark

```bash
sudo apt install wireshark -y
```

### Install Traffic Generation Tools

```bash
sudo apt install curl wget dnsutils -y
```

---

## 📌 Subtask 1.2 Configure Permissions

### Add User to Wireshark Group

```bash
sudo usermod -a -G wireshark $USER
```

### Configure Dumpcap Permissions

```bash
sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap
```

### Verify

```bash
getcap /usr/bin/dumpcap
```

Expected Output:

```bash
/usr/bin/dumpcap cap_net_admin,cap_net_raw=eip
```

---

## 📌 Subtask 1.3 Launch Wireshark

### GUI Version

```bash
wireshark &
```

### Command-Line Version

```bash
tshark -D
```

List available interfaces.

---

# 📡 Task 2: Capturing Network Traffic

## 📌 Subtask 2.1 Identify Network Interface

### View Interfaces

```bash
ip addr show
```

### View Statistics

```bash
ip -s link show
```

Look for interfaces like:

```text
eth0
ens33
enp0s3
```

---

## 📌 Subtask 2.2 Start Packet Capture

### Using Wireshark

1. Open Wireshark
2. Select active interface
3. Double-click interface
4. Start capture

### Using Tshark

```bash
sudo tshark -i eth0 -w capture.pcap
```

Capture only 100 packets:

```bash
sudo tshark -i eth0 -c 100 -w capture.pcap
```

---

## 📌 Subtask 2.3 Generate Traffic

### HTTP Traffic

```bash
curl -I http://httpbin.org/get

curl -I http://example.com
```

---

### DNS Traffic

```bash
nslookup google.com

dig facebook.com

host github.com
```

---

### HTTPS Traffic

```bash
curl -I https://www.google.com

wget -q --spider https://www.github.com
```

---

### ICMP Traffic

```bash
ping -c 10 8.8.8.8
```

---

## 📌 Subtask 2.4 Stop Capture

### GUI

Click:

```text
■ Stop Capture
```

### Tshark

Press:

```text
CTRL + C
```

---

# 🔍 Task 3: Filtering and Analyzing Packets

## 📌 Subtask 3.1 Understanding Wireshark Interface

### Packet List Pane

Displays packet summary.

### Packet Details Pane

Displays protocol details.

### Packet Bytes Pane

Displays raw packet bytes.

---

# 🌐 HTTP Filters

### All HTTP Traffic

```text
http
```

### GET Requests

```text
http.request.method == "GET"
```

### HTTP Responses

```text
http.response
```

### Specific Host

```text
http.host == "example.com"
```

### Status Code 200

```text
http.response.code == 200
```

---

# 🔗 TCP Filters

### All TCP Traffic

```text
tcp
```

### Port 80

```text
tcp.port == 80
```

### SYN Packets

```text
tcp.flags.syn == 1
```

### Specific IP

```text
ip.addr == 8.8.8.8 and tcp
```

---

## Advanced TCP Analysis

### Retransmissions

```text
tcp.analysis.retransmission
```

### Out of Order Packets

```text
tcp.analysis.out_of_order
```

### Window Updates

```text
tcp.analysis.window_update
```

---

# 🌍 DNS Filters

### All DNS Traffic

```text
dns
```

### DNS Queries

```text
dns.flags.response == 0
```

### DNS Responses

```text
dns.flags.response == 1
```

### Google Queries

```text
dns.qry.name contains "google"
```

### DNS Errors

```text
dns.flags.rcode != 0
```

---

# 🔀 Combined Filters

### HTTP OR HTTPS

```text
http or tls
```

### DNS OR HTTP

```text
dns or http
```

### Exclude SSH

```text
ip.addr == 192.168.1.1 and not ssh
```

### Web Traffic

```text
tcp.port == 80 or tcp.port == 443
```

---

# 🚨 Task 4: Identifying Network Anomalies

## Suspicious Port Activity

```text
tcp.port > 1024 and tcp.port < 5000
```

---

## Repeated Connection Attempts

```text
tcp.flags.syn == 1
```

---

## Suspicious DNS Queries

```text
dns and not (
dns.qry.name contains "google" or
dns.qry.name contains "facebook"
)
```

---

## Possible DGA Domains

```text
dns.qry.name matches ".*\..*\..*\..*\."
```

---

# 🔎 Security Indicators

Look for:

### Port Scanning

- Multiple SYN packets
- Sequential port probing
- Many RST responses

### DNS Abuse

- Excessive DNS requests
- Unknown domains
- Randomized domains

### HTTP Abuse

- Suspicious User Agents
- Unexpected File Downloads
- Large POST Requests

---

## Follow TCP Stream

Right Click Packet

```text
Follow → TCP Stream
```

or

```text
Follow → HTTP Stream
```

Analyze:

- Credentials
- Requests
- Responses
- Malware Indicators

---

# 📤 Task 5: Exporting Data

## Export HTTP Traffic

```bash
tshark -r capture.pcap -Y "http" -w http_traffic.pcap
```

---

## Export CSV

```bash
tshark -r capture.pcap -Y "http" -T csv > http_traffic.csv
```

---

## Export DNS Fields

```bash
tshark -r capture.pcap \
-Y "dns" \
-T fields \
-e dns.qry.name \
-e dns.resp.addr
```

---

# 📊 Generate Statistics

## Protocol Hierarchy

```bash
tshark -r capture.pcap -q -z io,phs
```

---

## TCP Conversations

```bash
tshark -r capture.pcap -q -z conv,tcp
```

---

## DNS Statistics

```bash
tshark -r capture.pcap -q -z dns,tree
```

---

## HTTP Statistics

```bash
tshark -r capture.pcap -q -z http,tree
```

---

# 📝 Automated Analysis Script

Create:

```bash
nano analyze_capture.sh
```

Paste:

```bash
#!/bin/bash

PCAP_FILE="capture.pcap"
REPORT_FILE="network_analysis_report.txt"

echo "Network Traffic Analysis Report" > $REPORT_FILE
echo "Generated on: $(date)" >> $REPORT_FILE
echo "=================================" >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "1. TOTAL PACKETS CAPTURED:" >> $REPORT_FILE
tshark -r $PCAP_FILE -q -z io,stat,0 | grep "Packets" >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "2. PROTOCOL DISTRIBUTION:" >> $REPORT_FILE
tshark -r $PCAP_FILE -q -z io,phs >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "3. TOP CONVERSATIONS:" >> $REPORT_FILE
tshark -r $PCAP_FILE -q -z conv,tcp | head -20 >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "4. DNS QUERIES:" >> $REPORT_FILE
tshark -r $PCAP_FILE -Y "dns.flags.response == 0" \
-T fields -e dns.qry.name \
| sort | uniq -c | sort -nr | head -10 >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "5. HTTP HOSTS:" >> $REPORT_FILE
tshark -r $PCAP_FILE -Y "http" \
-T fields -e http.host \
| sort | uniq -c | sort -nr >> $REPORT_FILE

echo "Analysis complete."
```

Run:

```bash
chmod +x analyze_capture.sh

./analyze_capture.sh
```

---

# ⏱️ Advanced Analysis

## Traffic Over Time

```bash
tshark -r capture.pcap -q -z io,stat,60
```

---

## Packets Per Second

```bash
tshark -r capture.pcap -q -z io,stat,1
```

---

# 🌎 Geolocation Analysis

Extract External IPs:

```bash
tshark -r capture.pcap \
-T fields \
-e ip.src \
-e ip.dst \
| tr '\t' '\n' \
| grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$' \
| grep -v '^192\.168\.' \
| grep -v '^10\.' \
| grep -v '^172\.' \
| sort | uniq > external_ips.txt
```

View Results:

```bash
cat external_ips.txt
```

---

# 🛡️ Security-Focused Filters

## Potential DGA Domains

```text
dns.qry.name matches ".{20,}"
```

---

## Suspicious User Agents

```text
http.user_agent contains "bot" or
http.user_agent contains "crawler"
```

---

## HTTP on Non-Standard Ports

```text
(tcp.port != 80 and tcp.port != 443) and http
```

---

## Large Uploads

```text
http.request.method == "POST" and
http.content_length > 1000000
```

---

# 🧪 Verification Commands

## Verify Capture Exists

```bash
ls -la *.pcap
```

---

## View Packets

```bash
tshark -r capture.pcap -c 10
```

---

## Verify HTTP Traffic

```bash
tshark -r capture.pcap -Y "http" -c 5
```

---

## Verify DNS Traffic

```bash
tshark -r capture.pcap -Y "dns" -c 5
```

---

## Verify TCP Traffic

```bash
tshark -r capture.pcap -Y "tcp" -c 5
```

---

# 🔧 Troubleshooting

## Permission Denied

```bash
groups $USER

sudo usermod -a -G wireshark $USER

newgrp wireshark
```

---

## No Interfaces Available

```bash
ip link show

sudo systemctl restart NetworkManager

ls -la /usr/bin/dumpcap
```

---

## Capture File Too Large

```bash
tshark -i eth0 \
-b filesize:100000 \
-b files:5 \
-w capture
```

---

## Limit Capture Duration

```bash
timeout 300 tshark -i eth0 -w capture.pcap
```

---

## No Traffic Captured

```bash
ip link show eth0

ping -c 5 8.8.8.8

ip link show eth0 | grep PROMISC
```

---

# ✅ Lab Verification Checklist

- [x] Installed Wireshark
- [x] Configured Packet Capture Permissions
- [x] Captured Network Traffic
- [x] Applied HTTP Filters
- [x] Applied TCP Filters
- [x] Applied DNS Filters
- [x] Investigated Anomalies
- [x] Exported Captured Data
- [x] Generated Analysis Report

---

# 🎓 Conclusion

In this lab, you successfully explored the fundamentals of network traffic analysis using Wireshark and Tshark.

## Skills Acquired

### Packet Capture

- Live Network Monitoring
- Traffic Collection
- Protocol Identification

### Protocol Analysis

- HTTP
- TCP
- DNS
- HTTPS

### Security Monitoring

- Detect Suspicious Activity
- Analyze Threat Indicators
- Investigate Network Anomalies

### Reporting

- Export Packet Data
- Generate Traffic Reports
- Create Security Findings

---

# 🛡️ Why This Matters in Cybersecurity

Packet analysis is essential for:

- Security Monitoring
- Threat Hunting
- Incident Response
- Malware Investigation
- Digital Forensics
- Compliance Auditing
- Network Troubleshooting

These are the same techniques used by:

- SOC Analysts
- Threat Hunters
- Incident Responders
- Network Security Engineers
- Digital Forensics Investigators

---

# 🚀 Next Steps

Continue learning:

- Advanced Wireshark Analysis
- Network Forensics
- Malware Traffic Analysis
- Threat Hunting
- IDS/IPS Monitoring
- Security Onion
- Zeek Network Monitoring

---

## 👨‍💻 Lab Completed Successfully

**Course:** Cyber Security Foundation  
**Lab:** Introduction to Wireshark  
**Platform:** Al Nafi Cloud Labs  
**Focus:** Network Traffic Analysis & Security Monitoring

⭐ Happy Packet Hunting!
