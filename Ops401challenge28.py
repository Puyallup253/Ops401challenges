#!/usr/bin/env python3
# Script Name:                 code challenge 28
# Author:                       Robert Gillespie
# Date of latest revision:      8/16/2023
# # Purpose:
import os
import logging
from logging.handlers import RotatingFileHandler
from cryptography.fernet import Fernet

# Configure logging with rotation
log_file = 'encryption_tool.log'
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=3)
log_handler.setFormatter(log_formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)

logger = logging.getLogger('encryption_tool')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)
logger.addHandler(stream_handler)

def encrypt_file(filepath):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    with open(filepath, 'rb') as file:
        data = file.read()
    encrypted_data = cipher.encrypt(data)
    with open(filepath + '.encrypted', 'wb') as file:
        file.write(encrypted_data)
    logger.info(f"File encrypted: {filepath}")
    print(f"File encrypted successfully. Key: {key.decode()}")

def decrypt_file(filepath):
    key = input("Enter the encryption key: ").encode()
    cipher = Fernet(key)
    with open(filepath, 'rb') as file:
        data = file.read()
    decrypted_data = cipher.decrypt(data)
    with open(filepath.replace('.encrypted', ''), 'wb') as file:
        file.write(decrypted_data)
    logger.info(f"File decrypted: {filepath}")
    print("File decrypted successfully.")

def main():
    logger.info("Encryption tool started.")
    print("Select a mode:\n1. Encrypt a file\n2. Decrypt a file")
    mode = int(input("Enter mode number: "))
    try:
        if mode == 1 or mode == 2:
            filepath = input("Enter the file path: ")
            if mode == 1:
                encrypt_file(filepath)
            else:
                decrypt_file(filepath)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
    logger.info("Encryption tool completed.")

if __name__ == '__main__':
    main()
