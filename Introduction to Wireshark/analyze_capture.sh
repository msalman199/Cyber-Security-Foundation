#!/bin/bash

PCAP_FILE="capture.pcap"
REPORT_FILE="network_analysis_report.txt"

echo "Network Traffic Analysis Report" > $REPORT_FILE
echo "Generated on: $(date)" >> $REPORT_FILE
echo "=================================" >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "1. TOTAL PACKETS CAPTURED:" >> $REPORT_FILE
tshark -r $PCAP_FILE -q -z io,stat,0 | grep "Packets" >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "2. PROTOCOL DISTRIBUTION:" >> $REPORT_FILE
tshark -r $PCAP_FILE -q -z io,phs >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "3. TOP CONVERSATIONS:" >> $REPORT_FILE
tshark -r $PCAP_FILE -q -z conv,tcp | head -20 >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "4. DNS QUERIES:" >> $REPORT_FILE
tshark -r $PCAP_FILE -Y "dns.flags.response == 0" -T fields -e dns.qry.name | sort | uniq -c | sort -nr | head -10 >> $REPORT_FILE

echo "" >> $REPORT_FILE
echo "5. HTTP HOSTS:" >> $REPORT_FILE
tshark -r $PCAP_FILE -Y "http" -T fields -e http.host | sort | uniq -c | sort -nr >> $REPORT_FILE

echo "Analysis complete. Report saved to $REPORT_FILE"
