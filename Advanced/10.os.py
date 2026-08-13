"""
Use os when you want to interact with the operating system.

DevOps use cases:

Check current working directory
List files
Create folders
Read environment variables
Check OS type
Work with paths
"""
# Check Current Directory

import os


current_dir = os.getcwd()
print(current_dir)

#List files in a folder

files = os.listdir("C:/Downloads")

for file in files:
    print(file)

#Create a folder

os.mkdir("C:/Backup") # exist_ok=True means: if folder already exists, do not throw error.

#Check if file or folder exists

path = "C:/Backup"

if os.path.exists(path):
    print("Path exists")
else:
    print("Path does not exist")

# Read environment variable

api_key = os.environ.get("API_KEY")

if api_key:
    print("API key found")
else:
    print("API key missing")
