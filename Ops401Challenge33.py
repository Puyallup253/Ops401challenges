#!/usr/bin/env python3
# Script Name:                 code challenge 33
# Author:                       Robert Gillespie
# Date of latest revision:      8/23/2023
# # Purpose:


import os
import platform
import hashlib
import time
import requests
import dotenv 
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("VIRUSTOTAL_KEY")
def search_and_hash(directory,key):
    hits = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            hits += 1
            file_path = os.path.join(root, file)
            print("Scanned File:", file_path)
            md5_hash = hashlib.md5()
            api(md5_hash,key)
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    md5_hash.update(chunk)
            print("Timestamp:", time.ctime(os.path.getmtime(file_path)))
            print("File Name:", file)
            print("File Size:", os.path.getsize(file_path), "bytes")
            print("MD5 Hash:", md5_hash.hexdigest())
            print()
    return hits
def api(hash,key):
    
    headers = {
        'x-apikey': key,
    }

    response = requests.get(f'https://www.virustotal.com/api/v3/files/{hash}', headers=headers)
    result = response.content        
    print(result.decode("utf-8"))
    print(response.status_code)
def main(key):
    my_os = platform.system()
    os.system("cls" if my_os == "Windows" else "clear")

    directory = input("Enter the directory to search in: ")

    total_hits = search_and_hash(directory,key)

    print("\nSearch completed.")
    print("Files searched:", total_hits)

if __name__ == "__main__":
    main(key)