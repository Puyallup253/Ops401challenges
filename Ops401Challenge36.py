#!/usr/bin/env python3
# Script Name:                 code challenge 32
# Author:                       Robert Gillespie
# Date of latest revision:      8/22/2023
# # Purpose:

import socket
import telnetlib
import subprocess

# Function to perform banner grabbing using netcat
def netcat_scan(addr, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket1:
        socket1.connect((addr, port))
        command = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(addr)
        socket1.sendall(command.encode())
        response = socket1.recv(4096)
        print("[Netcat Banner]\n" + response.decode())

# Function to perform banner grabbing using telnet
def telnet_scan(addr, port):
    try:
        with telnetlib.Telnet(addr, port) as tn:
            print("[Telnet Banner]\n" + tn.read_all().decode())
    except Exception as e:
        print("[Telnet Error]", str(e))

# Function to perform banner grabbing using Nmap
def nmap_scan(addr):
    try:
        nmap_output = subprocess.getoutput("nmap -p- -sV " + addr)
        print("[Nmap Scan]\n" + nmap_output)
    except Exception as e:
        print("[Nmap Error]", str(e))

# Main function
def main():
    addr = input("Enter the target URL or IP address: ")
    port = int(input("Enter the target port number: "))
    
    # Perform banner grabbing using netcat
    netcat_scan(addr, port)
    
    # Perform banner grabbing using telnet
    telnet_scan(addr, port)
    
    # Perform banner grabbing using Nmap
    nmap_scan(addr)

if __name__ == "__main__":
    main()

#Assisted by ChatGPT
