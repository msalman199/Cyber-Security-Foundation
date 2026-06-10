#!/usr/bin/env python3
"""
File Reader Script - Lab 3 Task 1
This script demonstrates basic file reading operations
"""

def read_network_devices(filename):
    """
    Function to read network device information from a CSV file
    """
    try:
        with open(filename, 'r') as file:
            print("Network Device Inventory:")
            print("-" * 40)
            print("Device Name | IP Address | Status")
            print("-" * 40)
            
            for line in file:
                # Remove newline character and split by comma
                device_info = line.strip().split(',')
                if len(device_info) == 3:
                    device_name, ip_address, status = device_info
                    print(f"{device_name:12} | {ip_address:13} | {status}")
                    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    """
    Main function to execute the file reading operation
    """
    filename = "../data/network_devices.csv"
    read_network_devices(filename)

if __name__ == "__main__":
    main()
