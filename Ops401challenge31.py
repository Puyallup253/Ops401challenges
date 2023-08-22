#!/usr/bin/env python3
# Script Name:                 code challenge 31
# Author:                       Robert Gillespie
# Date of latest revision:      8/21/2023
# # Purpose:

import os
import platform

# Define search function for Linux
def linux_search(filename, directory):
    hits = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if filename in file:
                hits += 1
                print("Hit:", os.path.join(root, file))
    return hits

# Define search function for Windows
def windows_search(filename, directory):
    hits = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if filename in file:
                hits += 1
                print("Hit:", os.path.join(root, file))
    return hits

def main():
    my_os = platform.system()

    print(my_os)

    if my_os == "Linux":
        os.system("clear")
    elif my_os == "Windows":
        os.system("cls")
    else:
        print("Your OS is not compatible with this script!")
        return

    filename = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    if my_os == "Linux":
        total_hits = linux_search(filename, directory)
    elif my_os == "Windows":
        total_hits = windows_search(filename, directory)

    print("\nSearch completed.")
    print("Files searched:", total_hits)

if __name__ == "__main__":
    main()

#Assisted by ChatGPt