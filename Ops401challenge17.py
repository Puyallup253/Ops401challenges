#!/usr/bin/env python3
# Script Name:                 code challenge 13
# Author:                       Robert Gillespie
# Date of latest revision:      7/31/2023
# # Purpose:




# Sample SSH authentication script
import time
import paramiko
import sys
import os
import socket
import getpass

def main():
    # Get input from user
    host = input("Please provide an IP address to connect to: ")
    user = input("Please provide a username: ")
    password = getpass.getpass(prompt="Please provide a password: ")
    port = 22

    # Create object of SSHClient and connect to SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port, user, password)

        # Execute commands and print the output
        execute_and_print_output(ssh, "whoami")
        execute_and_print_output(ssh, "ls -l")
        execute_and_print_output(ssh, "uptime")

    except paramiko.AuthenticationException as e:
        print("Authentication Failed!")
        print(e)

    ssh.close()

def execute_and_print_output(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    time.sleep(3)
    output = stdout.read().decode("utf-8")
    print(output)

if __name__ == "__main__":
    main()

