#!/usr/bin/env python3
"""
Network Security Monitor - Lab 3 Task 3
This script demonstrates loops, conditions, and functions for network monitoring
"""

import random
import time
import datetime

def generate_network_data():
    """
    Function to simulate network traffic data
    Returns a dictionary with network metrics
    """
    return {
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'connections': random.randint(50, 200),
        'failed_logins': random.randint(0, 15),
        'bandwidth_usage': random.randint(10, 95),
        'suspicious_ips': random.randint(0, 5)
    }

def check_security_threats(data):
    """
    Function to analyze network data for security threats
    Uses conditions to determine threat levels
    """
    threats = []
    threat_level = "LOW"
    
    # Check for high failed login attempts
    if data['failed_logins'] > 10:
        threats.append("High number of failed login attempts")
        threat_level = "HIGH"
    elif data['failed_logins'] > 5:
        threats.append("Moderate failed login attempts")
        if threat_level == "LOW":
            threat_level = "MEDIUM"
    
    # Check for suspicious IP addresses
    if data['suspicious_ips'] > 3:
        threats.append("Multiple suspicious IP addresses detected")
        threat_level = "HIGH"
    elif data['suspicious_ips'] > 0:
        threats.append("Suspicious IP addresses detected")
        if threat_level == "LOW":
            threat_level = "MEDIUM"
    
    # Check for high bandwidth usage (potential DDoS)
    if data['bandwidth_usage'] > 85:
        threats.append("Unusually high bandwidth usage")
        if threat_level != "HIGH":
            threat_level = "MEDIUM"
    
    return threats, threat_level

def log_security_event(threat_level, threats, data):
    """
    Function to log security events to a file
    """
    log_file = "../logs/network_monitor.log"
    
    with open(log_file, 'a') as file:
        file.write(f"\n--- Security Scan: {data['timestamp']} ---\n")
        file.write(f"Threat Level: {threat_level}\n")
        file.write(f"Connections: {data['connections']}\n")
        file.write(f"Failed Logins: {data['failed_logins']}\n")
        file.write(f"Bandwidth Usage: {data['bandwidth_usage']}%\n")
        file.write(f"Suspicious IPs: {data['suspicious_ips']}\n")
        
        if threats:
            file.write("Detected Threats:\n")
            for threat in threats:
                file.write(f"  - {threat}\n")
        else:
            file.write("No threats detected\n")

def display_monitoring_dashboard(scan_number, data, threats, threat_level):
    """
    Function to display real-time monitoring information
    """
    print(f"\n=== NETWORK SECURITY SCAN #{scan_number} ===")
    print(f"Time: {data['timestamp']}")
    print(f"Threat Level: {threat_level}")
    print("-" * 40)
    print(f"Active Connections: {data['connections']}")
    print(f"Failed Login Attempts: {data['failed_logins']}")
    print(f"Bandwidth Usage: {data['bandwidth_usage']}%")
    print(f"Suspicious IP Addresses: {data['suspicious_ips']}")
    
    if threats:
        print("\n⚠️  SECURITY ALERTS:")
        for i, threat in enumerate(threats, 1):
            print(f"  {i}. {threat}")
    else:
        print("\n✅ No security threats detected")
    
    print("-" * 40)

def run_monitoring_cycle(duration_minutes=2, scan_interval=10):
    """
    Function to run continuous network monitoring
    Uses loops to repeat monitoring tasks
    """
    print("🔍 Starting Network Security Monitoring...")
    print(f"Duration: {duration_minutes} minutes")
    print(f"Scan Interval: {scan_interval} seconds")
    print("=" * 50)
    
    start_time = time.time()
    end_time = start_time + (duration_minutes * 60)
    scan_count = 0
    
    # Main monitoring loop
    while time.time() < end_time:
        scan_count += 1
        
        # Generate network data
        network_data = generate_network_data()
        
        # Analyze for threats
        detected_threats, threat_level = check_security_threats(network_data)
        
        # Display dashboard
        display_monitoring_dashboard(scan_count, network_data, detected_threats, threat_level)
        
        # Log events if threats detected
        if detected_threats or threat_level != "LOW":
            log_security_event(threat_level, detected_threats, network_data)
        
        # Wait before next scan (unless it's the last iteration)
        if time.time() + scan_interval < end_time:
            print(f"Next scan in {scan_interval} seconds...")
            time.sleep(scan_interval)
        else:
            break
    
    print(f"\n🏁 Monitoring completed. Total scans: {scan_count}")
    return scan_count

def generate_summary_report(total_scans):
    """
    Function to generate a summary report
    """
    log_file = "../logs/network_monitor.log"
    
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            content = file.read()
            high_threats = content.count("Threat Level: HIGH")
            medium_threats = content.count("Threat Level: MEDIUM")
            
        print("\n📊 MONITORING SUMMARY REPORT")
        print("=" * 40)
        print(f"Total Security Scans: {total_scans}")
        print(f"High Threat Events: {high_threats}")
        print(f"Medium Threat Events: {medium_threats}")
        print(f"Log File: {log_file}")
        print("=" * 40)

def main():
    """
    Main function to execute network monitoring
    """
    import os
    
    print("🛡️  NETWORK SECURITY MONITORING SYSTEM")
    print("=" * 50)
    
    # Run monitoring cycle
    total_scans = run_monitoring_cycle(duration_minutes=1, scan_interval=5)
    
    # Generate summary report
    generate_summary_report(total_scans)
    
    print("\n📋 Check the log file for detailed security events:")
    print("cat ../logs/network_monitor.log")

if __name__ == "__main__":
    main()
