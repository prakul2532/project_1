"""
1.) Exception Handling:
    Try to open a non-existent file and handle FileNotFoundError
    Handle PermissionError when trying to write to a read-only file
    Use try-except-finally to ensure file is always closed
"""
try:
    with open("heavy.txt","r") as hv:
        content = hv.read()
        print(content)
except FileNotFoundError:
    print("file not found")
try:
    with open("file.txt","w") as file:
        file.write("hello everyone")
except PermissionError:
    print("file is in read only mode")
try:
    with open("heavy.txt","r") as hv:
        content = hv.read()
        print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("file is closed")
"""
2.) File Management:
    Check if a file exists before opening
    Get file size and modification time
    Rename and delete files
"""

import os

if os.path.exists("data.txt"):
    with open("data.txt", "r") as f:
        print(f.read())
else:
    print("File does not exist")


size = os.path.getsize("Create_file.txt")
print("File size:", size, "bytes")
import time

mod_time = os.path.getmtime("Create_file.txt")
print("Last modified:", time.ctime(mod_time))

import os

os.rename("file.txt", "new_name.txt")

os.remove("new_file.txt")