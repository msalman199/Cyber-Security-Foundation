#!/usr/bin/env python3

import json
import os
from datetime import datetime

def generate_html_dashboard(json_file):
    """
    Generate an HTML dashboard from JSON scan results
    """
    
    # Read JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Threat Simulation Dashboard</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f5f5f5;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            .header {{
                text-align: center;
                color: #333;
                border-bottom: 2px solid #007bff;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }}
            .summary {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }}
            .summary-card {{
                background-color: #f8f9fa;
                padding: 15px;
                border-radius: 5px;
                text-align: center;
                border-left: 4px solid #007bff;
            }}
            .summary-card h3 {{
                margin: 0 0 10px 0;
                color: #007bff;
            }}
            .summary-card p {{
                margin: 0;
                font-size: 24px;
                font-weight: bold;
                color: #333;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            th, td {{
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #007bff;
                color: white;
            }}
            tr:hover {{
                background-color: #f5f5f5;
            }}
            .threat-high {{
                background-color: #ffebee;
                color: #c62828;
            }}
            .threat-medium {{
                background-color: #fff3e0;
                color: #ef6c00;
            }}
            .threat-low {{
                background-color: #e8f5e8;
                color: #2e7d32;
            }}
            .timestamp {{
                text-align: center;
                color: #666;
                font-style: italic;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Basic Threat Simulation Dashboard</h1>
                <p>Network Security Assessment Results</p>
            </div>
            
            <div class="summary">
                <div class="summary-card">
                    <h3>Target Host</h3>
                    <p>{data.get('host', 'N/A')}</p>
                </div>
                <div class="summary-card">
                    <h3>Host State</h3>
                    <p>{data.get('state', 'N/A')}</p>
                </div>
                <div class="summary-card">
                    <h3>Open Ports</h3>
                    <p>{len(data.get('open_ports', []))}</p>
                </div>
                <div class="summary-card">
                    <h3>Potential Threats</h3>
                    <p>{len(data.get('potential_threats', []))}</p>
                </div>
            </div>
            
            <h2>Open Ports and Services</h2>
            <table>
                <thead>
                    <tr>
                        <th>Port</th>
                        <th>Protocol</th>
                        <th>Service</th>
                        <th>Version</th>
                        <th>Product</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    # Add open ports data
    for port_data in data.get('open_ports', []):
        html_content += f"""
                    <tr>
                        <td>{port_data.get('port', 'N/A')}</td>
                        <td>{port_data.get('protocol', 'N/A')}</td>
                        <td>{port_data.get('service', 'N/A')}</td>
                        <td>{port_data.get('version', 'N/A')}</td>
                        <td>{port_data.get('product', 'N/A')}</td>
                    </tr>
        """
    
    html_content += """
                </tbody>
            </table>
            
            <h2>Potential Threats</h2>
            <table>
                <thead>
                    <tr>
                        <th>Port</th>
                        <th>Service</th>
                        <th>Severity</th>
                        <th>Threat Description</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    # Add threats data
    for threat in data.get('potential_threats', []):
        severity_class = f"threat-{threat.get('severity', 'low').lower()}"
        html_content += f"""
                    <tr class="{severity_class}">
                        <td>{threat.get('port', 'N/A')}</td>
                        <td>{threat.get('service', 'N/A')}</td>
                        <td>{threat.get('severity', 'N/A')}</td>
                        <td>{threat.get('threat_description', 'N/A')}</td>
                    </tr>
        """
    
    html_content += f"""
                </tbody>
            </table>
            
            <div class="timestamp">
                <p>Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Save HTML file
    html_filename = f"threat_dashboard_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    with open(html_filename, 'w') as f:
        f.write(html_content)
    
    print(f"HTML dashboard generated: {html_filename}")
    return html_filename

if __name__ == "__main__":
    # Find the most recent JSON file
    json_files = [f for f in os.listdir('.') if f.startswith('threat_analysis_') and f.endswith('.json')]
    
    if json_files:
        latest_file = max(json_files, key=os.path.getctime)
        print(f"Using latest JSON file: {latest_file}")
        generate_html_dashboard(latest_file)
    else:
        print("No JSON files found. Please run the threat scanner first.")
