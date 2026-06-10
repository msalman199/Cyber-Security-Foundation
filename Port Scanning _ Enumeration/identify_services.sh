#!/bin/bash

echo "=== Service Identification Report ==="
echo "Date: $(date)"
echo "Host: $(hostname)"
echo "IP: $(hostname -I)"
echo

echo "=== Open TCP Ports ==="
nmap -sT 127.0.0.1 | grep "open"

echo
echo "=== Service Versions ==="
nmap -sV 127.0.0.1 | grep -E "(open|Service Info)"

echo
echo "=== Listening Services ==="
ss -tuln | grep LISTEN

echo
echo "=== Process Information ==="
sudo netstat -tulnp | grep LISTEN
