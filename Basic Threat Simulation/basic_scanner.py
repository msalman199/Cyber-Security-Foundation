#!/usr/bin/env python3

import nmap
import json
from datetime import datetime

def basic_scan(target, ports="1-1000"):
    """
    Perform a basic Nmap scan and return results
    """
    nm = nmap.PortScanner()
    
    print(f"Starting scan of {target} on ports {ports}")
    print("This may take a few minutes...")
    
    # Perform the scan
    nm.scan(target, ports, arguments='-sV -sC')
    
    return nm

def display_results(nm, target):
    """
    Display scan results in a readable format
    """
    print(f"\n{'='*50}")
    print(f"SCAN RESULTS FOR {target}")
    print(f"{'='*50}")
    
    if target in nm.all_hosts():
        host_info = nm[target]
        
        print(f"Host: {target}")
        print(f"State: {host_info.state()}")
        
        if 'tcp' in host_info:
            print(f"\nOpen TCP Ports:")
            print(f"{'Port':<8} {'State':<10} {'Service':<15} {'Version'}")
            print("-" * 50)
            
            for port in host_info['tcp']:
                port_info = host_info['tcp'][port]
                service = port_info.get('name', 'unknown')
                version = port_info.get('version', 'unknown')
                state = port_info.get('state', 'unknown')
                
                print(f"{port:<8} {state:<10} {service:<15} {version}")
    else:
        print(f"No results found for {target}")

def save_results_to_file(nm, target, filename):
    """
    Save scan results to a JSON file
    """
    results = {
        'timestamp': datetime.now().isoformat(),
        'target': target,
        'scan_info': nm.scaninfo(),
        'hosts': {}
    }
    
    if target in nm.all_hosts():
        host_info = nm[target]
        results['hosts'][target] = {
            'state': host_info.state(),
            'protocols': {}
        }
        
        for protocol in host_info.all_protocols():
            ports = host_info[protocol].keys()
            results['hosts'][target]['protocols'][protocol] = {}
            
            for port in ports:
                port_info = host_info[protocol][port]
                results['hosts'][target]['protocols'][protocol][port] = {
                    'state': port_info['state'],
                    'name': port_info.get('name', ''),
                    'version': port_info.get('version', ''),
                    'product': port_info.get('product', ''),
                    'extrainfo': port_info.get('extrainfo', '')
                }
    
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nResults saved to {filename}")

if __name__ == "__main__":
    target = "127.0.0.1"
    
    # Perform the scan
    scan_results = basic_scan(target)
    
    # Display results
    display_results(scan_results, target)
    
    # Save results to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"scan_results_{timestamp}.json"
    save_results_to_file(scan_results, target, filename)
