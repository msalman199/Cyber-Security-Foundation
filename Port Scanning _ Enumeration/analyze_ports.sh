#!/bin/bash

echo "=== Port Analysis ==="

# Common ports and their services
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

# Get open ports
open_ports=$(nmap -p- --open 127.0.0.1 2>/dev/null | grep "^[0-9]" | cut -d'/' -f1)

echo "Open ports found:"
for port in $open_ports; do
    service=${common_ports[$port]:-"Unknown"}
    echo "Port $port: $service"
done
