#!/usr/bin/env python3
# Script Name:                 code challenge 2
# Author:                       Robert Gillespie
# Date of latest revision:      7/17/2023
# # Purpose:Encryption of data at rest is a common need in security operations. Today you will begin development of a Python script that encrypts a single file.

import os
import zlib
from cryptography.fernet import Fernet

def encrypt_file(filepath):
    # Generate a random encryption key
    key = Fernet.generate_key()

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

    # Print the encryption key for future reference
    print(f"File encrypted successfully. Key: {key.decode()}")

def decrypt_file(filepath):
    # Prompt the user to enter the encryption key
    key = input("Enter the encryption key: ").encode()

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

    # Print a success message
    print("File decrypted successfully.")

def encrypt_message(message):
    # Generate a random encryption key
    key = Fernet.generate_key()

    # Create a Fernet cipher object using the key
    cipher = Fernet(key)

    # Encrypt the message by encoding it as bytes and using the cipher
    encrypted_message = cipher.encrypt(message.encode())

    # Print the encrypted message and the encryption key
    print(f"Encrypted message: {encrypted_message.decode()}")
    print(f"Encryption key: {key.decode()}")

def decrypt_message(message):
    # Prompt the user to enter the encryption key
    key = input("Enter the encryption key: ").encode()

    # Create a Fernet cipher object using the key
    cipher = Fernet(key)

    # Decrypt the message by encoding it as bytes and using the cipher
    decrypted_message = cipher.decrypt(message.encode())

    # Print the decrypted message
    print(f"Decrypted message: {decrypted_message.decode()}")

def compress_file(filepath):
    # Create the compressed file path by appending .zip extension
    compressed_filepath = filepath + '.zip'

    # Read the contents of the file to be compressed
    with open(filepath, 'rb') as file:
        data = file.read()

    # Compress the data using zlib with the highest compression level
    compressed_data = zlib.compress(data, level=zlib.Z_BEST_COMPRESSION)

    # Write the compressed data to a new file with .zip extension
    with open(compressed_filepath, 'wb') as file:
        file.write(compressed_data)

    # Remove the original file
    os.remove(filepath)

    # Print a success message with the compressed file path
    print(f"File compressed successfully. Compressed file: {compressed_filepath}")

def decompress_file(filepath):
    # Create the decompressed file path by removing the .zip extension
    decompressed_filepath = filepath.replace('.zip', '')

    # Read the contents of the compressed file
    with open(filepath, 'rb') as file:
        data = file.read()

    # Decompress the data using zlib
    decompressed_data = zlib.decompress(data)

    # Write the decompressed data to a new file without .zip extension
    with open(decompressed_filepath, 'wb') as file:
        file.write(decompressed_data)

    # Remove the original compressed file
    os.remove(filepath)

    # Print a success message with the decompressed file path
    print(f"File decompressed successfully. Decompressed file: {decompressed_filepath}")

def main():
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")

    # Prompt the user to enter the mode number
    mode = int(input("Enter mode number: "))

    if mode == 1 or mode == 2:
        # For modes 1 and 2, prompt the user to enter the file path
        filepath = input("Enter the file path: ")

        if mode == 1:
            # Encrypt the file
            encrypt_file(filepath)
        else:
            # Decrypt the file
            decrypt_file(filepath)

        # Prompt the user if they want to compress the file
        compress = input("Compress the file? (y/n): ")

        if compress.lower() == 'y':
            if mode == 1:
                # Compress the encrypted file
                compress_file(filepath + '.encrypted')
            else:
                # Compress the decrypted file
                compress_file(filepath)

    elif mode == 3 or mode == 4:
        # For modes 3 and 4, prompt the user to enter the message
        message = input("Enter the message: ")

        if mode == 3:
            # Encrypt the message
            encrypt_message(message)
        else:
            # Decrypt the message
            decrypt_message(message)

    else:
        # Invalid mode selected
        print("Invalid mode selected.")

if __name__ == '__main__':
    # Call the main function to start the script
    main()
