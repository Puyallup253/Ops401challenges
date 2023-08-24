#!/usr/bin/env python3
# Script Name:                 code challenge 32
# Author:                       Robert Gillespie
# Date of latest revision:      8/22/2023
# # Purpose: This script searches files, computes unique codes for their contents, and provides details about each file's properties.


import os
import platform
import hashlib
import time

def search_and_hash(directory):
    hits = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            hits += 1
            file_path = os.path.join(root, file)
            print("Scanned File:", file_path)
            md5_hash = hashlib.md5()
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    md5_hash.update(chunk)
            print("Timestamp:", time.ctime(os.path.getmtime(file_path)))
            print("File Name:", file)
            print("File Size:", os.path.getsize(file_path), "bytes")
            print("MD5 Hash:", md5_hash.hexdigest())
            print()
    return hits

def main():
    my_os = platform.system()
    os.system("cls" if my_os == "Windows" else "clear")

    directory = input("Enter the directory to search in: ")

    total_hits = search_and_hash(directory)

    print("\nSearch completed.")
    print("Files searched:", total_hits)

if __name__ == "__main__":
    main()

#Assisted by ChatGPT