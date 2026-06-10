#!/usr/bin/env python3
"""
Log Writer Script - Lab 3 Task 1
This script demonstrates file writing operations for security logs
"""

import datetime
import os

def write_security_log(log_file, event_type, message):
    """
    Function to write security events to a log file
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {event_type}: {message}\n"
    
    try:
        with open(log_file, 'a') as file:
            file.write(log_entry)
        print(f"Log entry written: {event_type}")
    except Exception as e:
        print(f"Error writing to log file: {e}")

def create_sample_logs():
    """
    Function to create sample security log entries
    """
    log_file = "../logs/security.log"
    
    # Sample security events
    events = [
        ("INFO", "User admin logged in successfully"),
        ("WARNING", "Failed login attempt from IP 192.168.1.100"),
        ("ERROR", "Unauthorized access attempt detected"),
        ("INFO", "Firewall rule updated"),
        ("CRITICAL", "Multiple failed login attempts - account locked")
    ]
    
    print("Generating security log entries...")
    print("-" * 40)
    
    for event_type, message in events:
        write_security_log(log_file, event_type, message)
    
    print("-" * 40)
    print(f"All log entries written to {log_file}")

def main():
    """
    Main function to execute log writing operations
    """
    create_sample_logs()

if __name__ == "__main__":
    main()
