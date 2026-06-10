#!/usr/bin/env python3

import nmap
import json
import csv
import argparse
import logging
from datetime import datetime
import os

class ThreatScanner:
    def __init__(self, log_level=logging.INFO):
        """
        Initialize the ThreatScanner with logging configuration
        """
        self.nm = nmap.PortScanner()
        self.setup_logging(log_level)
        
    def setup_logging(self, log_level):
        """
        Setup logging configuration
        """
        log_filename = f"threat_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_filename),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"ThreatScanner initialized. Log file: {log_filename}")
    
    def port_scan(self, target, port_range="1-1000", scan_type="sV"):
        """
        Perform port scanning with specified parameters
        """
        self.logger.info(f"Starting port scan of {target}")
        self.logger.info(f"Port range: {port_range}, Scan type: {scan_type}")
        
        try:
            arguments = f"-{scan_type}"
            self.nm.scan(target, port_range, arguments=arguments)
            self.logger.info("Port scan completed successfully")
            return True
        except Exception as e:
            self.logger.error(f"Port scan failed: {str(e)}")
            return False
    
    def vulnerability_scan(self, target):
        """
        Perform vulnerability scanning using Nmap scripts
        """
        self.logger.info(f"Starting vulnerability scan of {target}")
        
        try:
            self.nm.scan(target, arguments="--script vuln")
            self.logger.info("Vulnerability scan completed")
            return True
        except Exception as e:
            self.logger.error(f"Vulnerability scan failed: {str(e)}")
            return False
    
    def analyze_results(self, target):
        """
        Analyze scan results and identify potential threats
        """
        if target not in self.nm.all_hosts():
            self.logger.warning(f"No scan results found for {target}")
            return {}
        
        host_info = self.nm[target]
        analysis = {
            'host': target,
            'state': host_info.state(),
            'open_ports': [],
            'services': [],
            'potential_threats': []
        }
        
        # Analyze open ports and services
        for protocol in host_info.all_protocols():
            ports = host_info[protocol].keys()
            
            for port in ports:
                port_info = host_info[protocol][port]
                
                if port_info['state'] == 'open':
                    port_data = {
                        'port': port,
                        'protocol': protocol,
                        'service': port_info.get('name', 'unknown'),
                        'version': port_info.get('version', 'unknown'),
                        'product': port_info.get('product', 'unknown')
                    }
                    
                    analysis['open_ports'].append(port_data)
                    analysis['services'].append(port_info.get('name', 'unknown'))
                    
                    # Identify potential threats
                    self.identify_threats(port, port_info, analysis['potential_threats'])
        
        self.logger.info(f"Analysis completed. Found {len(analysis['open_ports'])} open ports")
        return analysis
    
    def identify_threats(self, port, port_info, threats_list):
        """
        Identify potential security threats based on open ports and services
        """
        service = port_info.get('name', '').lower()
        version = port_info.get('version', '').lower()
        
        # Common threat indicators
        threat_indicators = {
            'ssh': {
                'ports': [22],
                'threat': 'SSH service exposed - potential brute force target',
                'severity': 'Medium'
            },
            'http': {
                'ports': [80, 8080],
                'threat': 'HTTP service exposed - potential web application vulnerabilities',
                'severity': 'Medium'
            },
            'https': {
                'ports': [443],
                'threat': 'HTTPS service exposed - check for SSL/TLS vulnerabilities',
                'severity': 'Low'
            },
            'ftp': {
                'ports': [21],
                'threat': 'FTP service exposed - potential anonymous access or weak credentials',
                'severity': 'High'
            },
            'telnet': {
                'ports': [23],
                'threat': 'Telnet service exposed - unencrypted communication',
                'severity': 'High'
            },
            'smtp': {
                'ports': [25, 587],
                'threat': 'SMTP service exposed - potential email relay abuse',
                'severity': 'Medium'
            }
        }
        
        for threat_service, threat_info in threat_indicators.items():
            if (service == threat_service or port in threat_info['ports']):
                threat = {
                    'port': port,
                    'service': service,
                    'threat_description': threat_info['threat'],
                    'severity': threat_info['severity']
                }
                threats_list.append(threat)
    
    def save_results(self, analysis, output_format='json'):
        """
        Save analysis results in specified format
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if output_format.lower() == 'json':
            filename = f"threat_analysis_{timestamp}.json"
            with open(filename, 'w') as f:
                json.dump(analysis, f, indent=2)
        
        elif output_format.lower() == 'csv':
            filename = f"threat_analysis_{timestamp}.csv"
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                
                # Write header
                writer.writerow(['Port', 'Protocol', 'Service', 'Version', 'Product'])
                
                # Write port data
                for port_data in analysis['open_ports']:
                    writer.writerow([
                        port_data['port'],
                        port_data['protocol'],
                        port_data['service'],
                        port_data['version'],
                        port_data['product']
                    ])
        
        self.logger.info(f"Results saved to {filename}")
        return filename
    
    def generate_report(self, analysis):
        """
        Generate a comprehensive security report
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_filename = f"security_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_filename, 'w') as f:
            f.write("="*60 + "\n")
            f.write("BASIC THREAT SIMULATION REPORT\n")
            f.write("="*60 + "\n")
            f.write(f"Generated: {timestamp}\n")
            f.write(f"Target: {analysis['host']}\n")
            f.write(f"Host State: {analysis['state']}\n\n")
            
            # Open Ports Summary
            f.write("OPEN PORTS SUMMARY\n")
            f.write("-"*30 + "\n")
            f.write(f"Total Open Ports: {len(analysis['open_ports'])}\n\n")
            
            if analysis['open_ports']:
                f.write(f"{'Port':<8} {'Protocol':<10} {'Service':<15} {'Version'}\n")
                f.write("-"*60 + "\n")
                
                for port_data in analysis['open_ports']:
                    f.write(f"{port_data['port']:<8} {port_data['protocol']:<10} "
                           f"{port_data['service']:<15} {port_data['version']}\n")
            
            # Potential Threats
            f.write("\n\nPOTENTIAL THREATS IDENTIFIED\n")
            f.write("-"*35 + "\n")
            
            if analysis['potential_threats']:
                for i, threat in enumerate(analysis['potential_threats'], 1):
                    f.write(f"{i}. Port {threat['port']} ({threat['service']})\n")
                    f.write(f"   Severity: {threat['severity']}\n")
                    f.write(f"   Description: {threat['threat_description']}\n\n")
            else:
                f.write("No specific threats identified based on current scan.\n")
            
            # Recommendations
            f.write("\nRECOMMENDATIONS\n")
            f.write("-"*20 + "\n")
            f.write("1. Review all open ports and disable unnecessary services\n")
            f.write("2. Ensure all services are running latest versions\n")
            f.write("3. Implement proper firewall rules\n")
            f.write("4. Use strong authentication mechanisms\n")
            f.write("5. Regular security updates and patches\n")
            f.write("6. Monitor logs for suspicious activities\n")
        
        self.logger.info(f"Security report generated: {report_filename}")
        return report_filename

def main():
    parser = argparse.ArgumentParser(description="Basic Threat Simulation Scanner")
    parser.add_argument("target", nargs="?", default="127.0.0.1", 
                       help="Target IP address (default: 127.0.0.1)")
    parser.add_argument("-p", "--ports", default="1-1000", 
                       help="Port range to scan (default: 1-1000)")
    parser.add_argument("-f", "--format", choices=['json', 'csv'], default='json',
                       help="Output format (default: json)")
    parser.add_argument("-v", "--verbose", action="store_true",
                       help="Enable verbose logging")
    
    args = parser.parse_args()
    
    # Initialize scanner
    log_level = logging.DEBUG if args.verbose else logging.INFO
    scanner = ThreatScanner(log_level)
    
    print("Starting Basic Threat Simulation...")
    print(f"Target: {args.target}")
    print(f"Port Range: {args.ports}")
    
    # Perform scans
    if scanner.port_scan(args.target, args.ports):
        # Analyze results
        analysis = scanner.analyze_results(args.target)
        
        if analysis:
            # Display summary
            print(f"\nScan Summary:")
            print(f"Host State: {analysis['state']}")
            print(f"Open Ports: {len(analysis['open_ports'])}")
            print(f"Potential Threats: {len(analysis['potential_threats'])}")
            
            # Save results
            scanner.save_results(analysis, args.format)
            
            # Generate report
            scanner.generate_report(analysis)
            
            print("\nThreat simulation completed successfully!")
        else:
            print("No results to analyze.")
    else:
        print("Scan failed. Check logs for details.")

if __name__ == "__main__":
    main()
