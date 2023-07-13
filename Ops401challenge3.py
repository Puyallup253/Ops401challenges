#!/usr/bin/env python3
# Script Name:                 code challenge 3
# Author:                       Robert Gillespie
# Date of latest revision:      7/12/2023
# # Purpose:  writing an uptime sensor tool that checks systems are responding by adding a feature that notifies you of interesting status changes.

import os
import platform
import subprocess
import time
import smtplib
from email.mime.text import MIMEText
from getpass import getpass
def ping_host(ip_address):
    # ICMP packet transmission using the 'ping' command based on the platform
    if platform.system().lower() == "windows":
        command = ["ping", "-n", "1", "-w", "1000", ip_address]
    else:
        command = ["ping", "-c", "1", "-W", "1", ip_address]

    # Execute the ping command and capture the return code
    return_code = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    return return_code == 0

def send_email(sender_email, sender_password, receiver_email, subject, message):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

def main():
    ip_address = "8.8.8.8"  
    sender_email = input("Enter your email address: ")
    sender_password = getpass("Enter your email password: ")
    receiver_email = input("Enter the recipient email address: ")

    status = ping_host(ip_address)
    status_changed = False

    while True:
        current_status = ping_host(ip_address)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        if current_status != status:
            status_changed = True
            subject = f"""
            Host Status Change: {ip_address}
            """
            message = f"""
            Host status changed from {'up' if status else 'down'} to {'up' if current_status else 'down'} at {timestamp}.
            """
            send_email(sender_email, sender_password, receiver_email, subject, message)
        else:
            continue

        if status_changed:
            print(f"{timestamp} Host status changed from {'up' if status else 'down'} to {'up' if current_status else 'down'}.")
            status_changed = False
        else:
            continue
        status = current_status
        time.sleep(2)

main()
