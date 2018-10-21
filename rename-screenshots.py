#!/usr/bin/env python3

#Screenshot from YYYY-MM-DD HH-MM-SS.png

import os
import sys
import time

assert len(sys.argv) == 2

PATH = sys.argv[1]
OUTPUT_NAME = "Screenshot from {}"

print("\n<#> LICENSE: This software is licensed to you under the terms of the")
print("             MIT License and comes with ABSOLUTELY NO WARRANTY!")
print("             Use this software at your own risk. For more information,")
print("             see the LICENSE file that came with this program.")

print("\n<!> WARNING: This will irreversibly rename files on your hard disk and ")
print("             WILL NOT ask for confirmation before each operation. Be sure")
print("             you have a backup of this data before using this utility.")

print("\nTo accept the terms and continue, type 'I ACCEPT' and press return.")
response = input(">> ")

if response != "I ACCEPT":
    print("\n<!> ERROR: You did not accept. Abort.\n")
    raise SystemExit

print("\nFiles at the path you provided will be renamed.")
print("\nFORMAT: Screenshot from YYYY-MM-DD HH-MM-SS.{extension}")
print("PATH: {}\n".format(PATH))

print("To start the operation, press return.")
input()


SIZE_FILEPATH = len(PATH) + 50
SIZE_TIMESTAMP = 19
SIZE_SEPARATOR = 3
TABLE_SIZE = ( (2 * SIZE_FILEPATH) + 
               SIZE_TIMESTAMP + 
               (2 * SIZE_SEPARATOR) )

TABLE = ( "{:" + str(SIZE_FILEPATH) + 
          "s} | {:" + str(SIZE_TIMESTAMP) + 
          "s} | {:" + str(SIZE_FILEPATH) + "s}" )
         
OUTPUT_NAME = "Screenshot from {}"


files = os.listdir(PATH)

print(TABLE.format("INPUT FILE PATH", "LAST MODIFIED", "MOVED TO"))
print("-" * TABLE_SIZE)

for input_filename in files:
    
    extension = input_filename[input_filename.rfind(".")+1:]
    
    input_file_path = "{}/{}".format(PATH, input_filename)
    
    timestamp = time.localtime(os.path.getmtime(input_file_path))
    pretty_timestamp = time.strftime("%Y-%m-%d %H-%M-%S", timestamp)
    
    output_file_path = "{}/{}.{}".format(PATH, 
                                         OUTPUT_NAME.format(pretty_timestamp), 
                                         extension)
    
    print(TABLE.format(input_file_path, pretty_timestamp, output_file_path))
    
    os.rename(input_file_path, output_file_path)

print("\n\nOperation complete.")
