#!/usr/bin/env python3
# Script Name:                 code challenge 2
# Author:                       Robert Gillespie
# Date of latest revision:      7/11/2023
# # Purpose: In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.

import os
import platform
import subprocess
import time

def ping_host(ip_address):
    # ICMP packet transmission using the 'ping' command based on the platform
    if platform.system().lower() == "windows":
        command = ["ping", "-n", "1", "-w", "1000", ip_address]
    else:
        command = ["ping", "-c", "1", "-W", "1", ip_address]

    # Execute the ping command and capture the return code
    return_code = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    return return_code == 0

def main():
    ip_address = "8.8.8.8"  # Replace with the IP address you want to test

    while True:
        status = "Network Active" if ping_host(ip_address) else "Network Inactive"
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        print(f"{timestamp} {status} to {ip_address}")
        time.sleep(2)

if __name__ == "__main__":
    main()
