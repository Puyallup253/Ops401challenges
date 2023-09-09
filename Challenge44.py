#!/usr/bin/python3
#Script Name:                 code challenge 44
# Author:                       Robert Gillespie
# Date of latest revision:      9/8/2023
# # Purpose:
import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# TODO: Set a timeout value here, for example, 2 seconds.
timeout = 2
sockmod.settimeout(timeout)

hostip = input("Enter the target host IP: ")  # Collect the host IP from the user.
portno = int(input("Enter the target port number: "))  # Collect and convert the port number to an integer.

def portScanner(portno):
    try:
        # Use the connect() function to attempt a connection to the specified host and port.
        sockmod.connect((hostip, portno))
        print(f"Port {portno} is open")
    except socket.error:
        print(f"Port {portno} is closed")

portScanner(portno)  # Call the portScanner function with the specified port number.

#Assisted by ChatGPT
