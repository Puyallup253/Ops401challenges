#!/usr/bin/env python3
# Script Name:                 code challenge 2
# Author:                       Robert Gillespie
# Date of latest revision:      7/17/2023
# # Purpose:Alter the desktop wallpaper on a Windows PC with a ransomware message
# Create a popup window on a Windows PC with a ransomware message

import os
from cryptography.fernet import Fernet
import subprocess

def encrypt_file(filepath, key):
    # Create a Fernet cipher object using the key
    cipher = Fernet(key)

    # Read the contents of the file to be encrypted
    with open(filepath, 'rb') as file:
        data = file.read()

    # Encrypt the data using the cipher
    encrypted_data = cipher.encrypt(data)

    # Write the encrypted data to a new file with the .encrypted extension
    with open(filepath + '.encrypted', 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(filepath, key):
    # Create a Fernet cipher object using the key
    cipher = Fernet(key)

    # Read the contents of the encrypted file
    with open(filepath, 'rb') as file:
        data = file.read()

    # Decrypt the data using the cipher
    decrypted_data = cipher.decrypt(data)

    # Write the decrypted data to a new file without the .encrypted extension
    with open(filepath.replace('.encrypted', ''), 'wb') as file:
        file.write(decrypted_data)

def encrypt_folder(folder_path, key):
    # Recursively encrypt files within the folder and its subdirectories
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

def decrypt_folder(folder_path, key):
    # Recursively decrypt files within the folder and its subdirectories
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)
 
def run_ransom(): 
    subprocess.run(['python', 'Ransomware.py'])
#  ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])

def main():
    # Display available modes
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    print("5. Recursively encrypt a folder and its contents")
    print("6. Recursively decrypt a folder encrypted by this tool")
    print("7. This is a Ransom letter")

    # Prompt the user to enter the mode number
    mode = int(input("Enter mode number: "))

    if mode in [1, 2]:
        # For file encryption/decryption modes, prompt for file path and generate a key
        filepath = input("Enter the file path: ")
        key = Fernet.generate_key()

        if mode == 1:
            # Encrypt the file
            encrypt_file(filepath, key)
        else:
            # Decrypt the file
            decrypt_file(filepath, key)

        # Print the result and encryption key
        print(f"File {'encrypted' if mode == 1 else 'decrypted'} successfully. Key: {key.decode()}")

    elif mode in [3, 4]:
        # For message encryption/decryption modes, prompt for the message and generate a key
        message = input("Enter the message: ")
        key = Fernet.generate_key()

        cipher = Fernet(key)

        if mode == 3:
            # Encrypt the message
            encrypted_message = cipher.encrypt(message.encode())
            print(f"Encrypted message: {encrypted_message.decode()}")
            print(f"Encryption key: {key.decode()}")

        else:
            # Decrypt the message
            decrypted_message = cipher.decrypt(message.encode()).decode()
            print(f"Decrypted message: {decrypted_message}")

    elif mode == 5:
        # For folder encryption mode, prompt for folder path and generate a key
        folder_path = input("Enter the folder path: ")
        key = Fernet.generate_key()

        # Encrypt the folder recursively
        encrypt_folder(folder_path, key)

        # Print the result and encryption key
        print("Folder recursively encrypted successfully. Key: {key.decode()}")

    elif mode == 6:
        # For folder decryption mode, prompt for folder path and encryption key
        folder_path = input("Enter the folder path: ")
        key = input("Enter the encryption key: ").encode()

        # Decrypt the folder recursively
        decrypt_folder(folder_path, key)

        # Print the result
        print("Folder recursively decrypted successfully.")
        elif mode == 7:
        # For folder decryption mode, prompt for folder path and encryption key
        folder_path = input("Enter the folder path: ")
        key = input("Enter the encryption key: ").encode()

        # Decrypt the folder recursively
        decrypt_folder(folder_path, key)

        # Print the result
        print("Folder recursively decrypted successfully.")

    else:
        # Invalid mode selected
        print("Invalid mode selected.")

if __name__ == '__main__':
    main()
