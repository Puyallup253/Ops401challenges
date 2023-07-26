#!/usr/bin/env python3
# Script Name:                 code challenge 11
# Author:                       Robert Gillespie
# Date of latest revision:      7/24/2023
# # Purpose: 

from scapy.all import sr1, IP, TCP, ICMP
from ipaddress import IPv4Network

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

def icmp_ping_sweep(network):
    hosts_online = 0
    for host in IPv4Network(network):
        if host == network.network_address or host == network.broadcast_address:
            continue

        response = sr1(IP(dst=str(host)) / ICMP(), timeout=1, verbose=0)
        if response is None:
            print(f"Host {host} is down or unresponsive.")
        elif response.haslayer(ICMP) and response.getlayer(ICMP).type in [1, 2, 3, 9, 10, 13]:
            print(f"Host {host} is actively blocking ICMP traffic.")
        else:
            print(f"Host {host} is responding.")
            hosts_online += 1

    print(f"Total hosts online: {hosts_online}")

def main():
    print("Network Security Tool")
    print("1. TCP Port Range Scanner Mode")
    print("2. ICMP Ping Sweep Mode")
    choice = input("Enter your choice: ")

    if choice == "1":
        host = "scanme.nmap.org"
        port_range = range(1, 90)

        for port in port_range:
            scan_port(host, port)

    elif choice == "2":
        network = input("Enter the network address ( 10.10.0.0/24): ")
        icmp_ping_sweep(IPv4Network(network))

    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
