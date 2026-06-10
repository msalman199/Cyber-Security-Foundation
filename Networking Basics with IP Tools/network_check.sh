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

echo "Testing DNS server..."
ping -c 2 8.8.8.8 | tail -2

echo "Testing internet connectivity..."
ping -c 2 google.com | tail -2

echo ""
echo "=== DNS Resolution Test ==="
nslookup google.com | grep -A 2 "Non-authoritative"
