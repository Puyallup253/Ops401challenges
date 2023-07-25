#!/usr/bin/env python3
# Script Name:                 code challenge 11
# Author:                       Robert Gillespie
# Date of latest revision:      7/24/2023
# # Purpose: In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed.

from scapy.all import sr1, IP, TCP

def scan_port(host, port):
    src_port = 85  
    response = sr1(IP(dst=host) / TCP(sport=src_port, dport=port, flags='S'), timeout=1, verbose=0)

    if response is None:
        print(f"Port {port}/TCP is filtered and silently dropped.")
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        send_rst = sr1(IP(dst=host) / TCP(sport=src_port, dport=port, flags='AR'), timeout=1, verbose=0)
        print(f"Port {port}/TCP is open.")
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
        print(f"Port {port}/TCP is closed.")

def main():
    host = "scanme.nmap.org"  
    port_range = range(1, 90)  

    for port in port_range:
        scan_port(host, port)

if __name__ == "__main__":
    main()

   