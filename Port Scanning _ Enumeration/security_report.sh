#!/bin/bash

REPORT_FILE="security_report_$(date +%Y%m%d_%H%M%S).txt"

{
    echo "=== SECURITY ASSESSMENT REPORT ==="
    echo "Generated: $(date)"
    echo "Target: localhost (127.0.0.1)"
    echo "Assessed by: $(whoami)"
    echo
    
    echo "=== OPEN PORTS ==="
    nmap --open 127.0.0.1
    echo
    
    echo "=== SERVICE VERSIONS ==="
    nmap -sV 127.0.0.1
    echo
    
    echo "=== VULNERABILITY SCAN ==="
    nmap --script vuln 127.0.0.1
    echo
    
    echo "=== RECOMMENDATIONS ==="
    echo "1. Close unnecessary ports"
    echo "2. Update services to latest versions"
    echo "3. Configure firewall rules"
    echo "4. Monitor for unauthorized services"
    echo "5. Regular security assessments"
    
} > "$REPORT_FILE"

echo "Security report saved to: $REPORT_FILE"
cat "$REPORT_FILE"
