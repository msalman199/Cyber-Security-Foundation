# 🌐 Networking Basics with IP Tools

![Linux](https://img.shields.io/badge/Linux-Networking-blue?style=for-the-badge\&logo=linux)
![Networking](https://img.shields.io/badge/Networking-IP%20Tools-green?style=for-the-badge)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Network%20Analysis-red?style=for-the-badge)
![Al Nafi](https://img.shields.io/badge/AlNafi-Cloud-orange?style=for-the-badge)

---

# 📖 Overview

This lab introduces fundamental networking concepts and practical network troubleshooting techniques using essential Linux networking tools.

Students will learn how to:

* View and analyze network configurations
* Test connectivity between systems
* Investigate DNS resolution
* Trace network paths
* Troubleshoot networking problems
* Perform basic security-focused network analysis

---

# 🎯 Objectives

By the end of this lab, you will be able to:

✅ Understand IP addressing concepts

✅ View network interface configurations

✅ Test network connectivity using Ping

✅ Trace network routes using Traceroute

✅ Explore DNS resolution using nslookup and dig

✅ Troubleshoot connectivity issues

✅ Analyze network outputs from a cybersecurity perspective

---

# 📚 Prerequisites

Before starting this lab, you should have:

* Basic Linux command-line knowledge
* Basic understanding of IP addresses
* Ability to open a terminal
* No prior networking experience required

---

# ☁️ Lab Environment

Al Nafi provides pre-configured Linux cloud machines.

### Steps

1. Click **Start Lab**
2. Wait for machine initialization
3. Open Terminal
4. Begin lab exercises

All networking tools are already installed.

---

# 🔍 Task 1: Understanding Network Interface Configuration

## Subtask 1.1 — View Network Interfaces

### Display All Network Interfaces

```bash
ip addr show
```

### Short Version

```bash
ip a
```

### Understanding Output

| Interface     | Description               |
| ------------- | ------------------------- |
| lo            | Loopback Interface        |
| eth0 / enp0s3 | Primary Network Interface |
| inet          | IPv4 Address              |
| inet6         | IPv6 Address              |

---

## Subtask 1.2 — Traditional ifconfig Command

### Display Interfaces

```bash
ifconfig
```

### Install ifconfig if Missing

```bash
sudo apt update
sudo apt install net-tools -y
```

```bash
ifconfig
```

### View All Interfaces

```bash
ifconfig -a
```

---

## Subtask 1.3 — Find Your IP Address

### Show Primary IP

```bash
hostname -I
```

### Show Routing Information

```bash
ip route show
```

### Important Information

* IP Address
* Subnet Mask
* Default Gateway

Example:

```text
IP Address: 192.168.1.50
Subnet: /24
Gateway: 192.168.1.1
```

---

# 📡 Task 2: Testing Network Connectivity

## Subtask 2.1 — Basic Ping Testing

### Test Local Machine

```bash
ping -c 4 127.0.0.1
```

### Find Default Gateway

```bash
ip route | grep default
```

Example:

```bash
ping -c 4 192.168.1.1
```

---

## Subtask 2.2 — Internet Connectivity Testing

### Test Public DNS

```bash
ping -c 4 8.8.8.8
```

### Test Website Connectivity

```bash
ping -c 4 google.com
```

### Understanding Ping Results

| Field       | Meaning      |
| ----------- | ------------ |
| time        | Latency      |
| ttl         | Time To Live |
| packet loss | Lost packets |
| transmitted | Packets sent |

---

## Subtask 2.3 — Advanced Ping Options

### Large Packet Test

```bash
ping -c 4 -s 1000 google.com
```

### Timestamped Ping

```bash
ping -c 4 -D google.com
```

---

# 🛰️ Task 3: Tracing Network Paths

## Subtask 3.1 — Install Traceroute

```bash
sudo apt install traceroute -y
```

### Trace Route to Google

```bash
traceroute google.com
```

### Alternative Tool

```bash
tracepath google.com
```

---

## Subtask 3.2 — Analyze Route

```bash
traceroute -n 8.8.8.8
```

### Output Explanation

| Item          | Description     |
| ------------- | --------------- |
| Hop Number    | Router Sequence |
| IP Address    | Router Address  |
| Response Time | Latency         |
| *             | Timeout         |

---

# 🌍 Task 4: DNS Resolution

## Subtask 4.1 — nslookup

### Resolve Domain Name

```bash
nslookup google.com
```

### Reverse Lookup

```bash
nslookup 8.8.8.8
```

### Query Specific DNS Server

```bash
nslookup google.com 1.1.1.1
```

---

## Subtask 4.2 — Using dig

### Install DNS Utilities

```bash
sudo apt install dnsutils -y
```

### Basic Query

```bash
dig google.com
```

### Clean Output

```bash
dig +short google.com
```

### Query MX Records

```bash
dig google.com MX
```

### Query NS Records

```bash
dig google.com NS
```

### Query TXT Records

```bash
dig google.com TXT
```

---

## Subtask 4.3 — DNS Investigation

### Full Resolution Path

```bash
dig +trace google.com
```

### View Local DNS Settings

```bash
cat /etc/resolv.conf
```

---

# 🛠️ Task 5: Network Troubleshooting

## Subtask 5.1 — Create Diagnostic Script

### Create Script

```bash
nano network_check.sh
```

### Script Content

```bash
#!/bin/bash

echo "=== Network Diagnostic Report ==="
echo "Date: $(date)"
echo ""

echo "=== IP Configuration ==="
ip addr show | grep -E "inet |UP"
echo ""

echo "=== Default Gateway ==="
ip route | grep default
echo ""

echo "=== DNS Servers ==="
cat /etc/resolv.conf | grep nameserver
echo ""

echo "=== Connectivity Tests ==="

echo "Testing loopback..."
ping -c 2 127.0.0.1 | tail -2

echo ""

echo "Testing DNS server..."
ping -c 2 8.8.8.8 | tail -2

echo ""

echo "Testing internet connectivity..."
ping -c 2 google.com | tail -2

echo ""

echo "=== DNS Resolution Test ==="
nslookup google.com | grep -A 2 "Non-authoritative"
```

### Make Executable

```bash
chmod +x network_check.sh
```

### Run Script

```bash
./network_check.sh
```

---

## Subtask 5.2 — Network Performance Testing

### Test Different Packet Sizes

```bash
echo "Testing different packet sizes..."

for size in 64 128 512 1024
do
    echo "Packet size: $size bytes"
    ping -c 3 -s $size google.com | grep "min/avg/max"
done
```

### Monitor Interfaces

```bash
watch -n 2 'ip -s link'
```

Stop monitoring:

```bash
Ctrl + C
```

---

# 🔐 Task 6: Security-Focused Network Analysis

## Subtask 6.1 — Port Scanning Basics

### Install Netcat

```bash
sudo apt install netcat -y
```

### Scan Common Ports

```bash
nc -zv 127.0.0.1 22
```

```bash
nc -zv 127.0.0.1 80
```

```bash
nc -zv 127.0.0.1 443
```

---

## Subtask 6.2 — Discover Running Services

### View Open Ports

```bash
ss -tuln
```

### Show Listening Services

```bash
ss -tuln | grep LISTEN
```

### Output Explanation

| Flag | Meaning           |
| ---- | ----------------- |
| t    | TCP               |
| u    | UDP               |
| l    | Listening         |
| n    | Numeric Addresses |

---

# ⚠️ Troubleshooting Guide

## Command Not Found

### Install net-tools

```bash
sudo apt install net-tools
```

### Install DNS Tools

```bash
sudo apt install dnsutils
```

### Install Traceroute

```bash
sudo apt install traceroute
```

---

## Permission Issues

```bash
sudo [command]
```

---

## Network Unreachable

Check:

```bash
ip addr show
```

```bash
ip route show
```

```bash
ping 127.0.0.1
```

---

## DNS Problems

```bash
cat /etc/resolv.conf
```

```bash
ping 8.8.8.8
```

```bash
nslookup google.com 1.1.1.1
```

---

# ✅ Lab Verification Checklist

Verify you can:

* [ ] View network interfaces
* [ ] Display IP address information
* [ ] Ping localhost
* [ ] Ping gateway
* [ ] Ping internet hosts
* [ ] Trace routes
* [ ] Resolve DNS names
* [ ] Use dig queries
* [ ] Run network diagnostic script
* [ ] Identify listening services

---

# 📚 Networking Commands Summary

| Command       | Purpose              |
| ------------- | -------------------- |
| ip addr show  | View interfaces      |
| ip route show | View routing table   |
| hostname -I   | Show IP              |
| ping          | Connectivity testing |
| traceroute    | Path tracing         |
| tracepath     | Route analysis       |
| nslookup      | DNS queries          |
| dig           | Advanced DNS lookup  |
| ss            | View sockets         |
| nc            | Port testing         |
| watch         | Real-time monitoring |

---

# 🔐 Cybersecurity Relevance

Networking knowledge is essential for:

### Incident Response

* Investigate communication issues
* Trace attacker connections

### Threat Hunting

* Discover suspicious hosts
* Identify unusual network behavior

### Vulnerability Assessment

* Map network topology
* Understand attack paths

### Forensics

* Analyze communications
* Reconstruct attack timelines

### Security Monitoring

* Detect anomalies
* Monitor services

---

# 🎓 Lab Conclusion

Congratulations! 🎉

You have successfully completed **Networking Basics with IP Tools**.

## Key Achievements

✅ Learned IP addressing fundamentals

✅ Explored network interfaces

✅ Tested connectivity using ping

✅ Traced network paths with traceroute

✅ Performed DNS investigations

✅ Created automated diagnostic scripts

✅ Practiced security-focused network analysis

---

# 🚀 Next Steps

Continue your cybersecurity journey by learning:

* Nmap Network Scanning
* Tcpdump Packet Analysis
* Wireshark Traffic Analysis
* Network Monitoring Tools
* Intrusion Detection Systems (IDS)
* Threat Hunting Methodologies

---

## 🏆 Lab Completed Successfully

**Technology Stack**

* 🐧 Linux
* 🌐 Networking
* 📡 IP Tools
* 🔎 DNS Analysis
* 🛰️ Traceroute
* 🔐 Cybersecurity
* ☁️ Al Nafi Cloud Labs

**Author:** Hafiz Muhammad Salman
**Lab:** Networking Basics with IP Tools
**Platform:** Al Nafi Cloud

---
