#!/usr/bin/env python3
# Script Name:                 code challenge 27
# Author:                       Robert Gillespie
# Date of latest revision:      8/15/2023
# # Purpose:

import os
import zlib
import logging
from logging.handlers import RotatingFileHandler
from cryptography.fernet import Fernet

# Configure logging with rotation
log_file = 'encryption_tool.log'
log_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=3)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[log_handler])

def encrypt_file(filepath):
    # Generate encryption key
    key = Fernet.generate_key()
    cipher = Fernet(key)

    # Read file contents
    with open(filepath, 'rb') as file:
        data = file.read()

    # Encrypt data
    encrypted_data = cipher.encrypt(data)

    # Write encrypted data to new file
    with open(filepath + '.encrypted', 'wb') as file:
        file.write(encrypted_data)

    # Log and print success message
    logging.info(f"File encrypted: {filepath}")
    print(f"File encrypted successfully. Key: {key.decode()}")

def decrypt_file(filepath):
    # Prompt user for encryption key
    key = input("Enter the encryption key: ").encode()
    cipher = Fernet(key)

    # Read encrypted file contents
    with open(filepath, 'rb') as file:
        data = file.read()

    # Decrypt data
    decrypted_data = cipher.decrypt(data)

    # Write decrypted data to new file
    with open(filepath.replace('.encrypted', ''), 'wb') as file:
        file.write(decrypted_data)

    # Log and print success message
    logging.info(f"File decrypted: {filepath}")
    print("File decrypted successfully.")

def main():
    # Log tool start
    logging.info("Encryption tool started.")
    
    # Display user options
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")

    # Get user input
    mode = int(input("Enter mode number: "))

    try:
        if mode == 1 or mode == 2:
            # Prompt user for file path
            filepath = input("Enter the file path: ")

            if mode == 1:
                encrypt_file(filepath)  # Call encryption function
            else:
                decrypt_file(filepath)  # Call decryption function

    except Exception as e:
        # Log and handle errors
        logging.error(f"An error occurred: {str(e)}")

    # Log tool completion
    logging.info("Encryption tool completed.")

if __name__ == '__main__':
    main()
