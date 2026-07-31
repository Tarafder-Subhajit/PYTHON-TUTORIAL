"""
 File Handling in Python for DevOps Engineers
 ------------------------------------------------
 File handling is important in DevOps because scripts often need to:
 - read configuration files
 - write deployment logs
 - store server inventory
 - process reports or monitoring data

Python uses the built-in open() function. 
with open("server.txt", "a") as f:
    f.write("web-01\n")
 
"""
# 1. Reading files
# 1.1 Reading a whole file
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)
# 1.2 Reading line by line
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())
# 1.3 Reading into a list
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# 2. Writing files
# 2.1 Writing to a file (overwrites existing content)
with open("output.txt", "w") as f:
    f.write("This is a new file.\n")
    f.write("It will overwrite existing content.\n")
# 2.2 Appending to a file
with open("output.txt", "a") as f:
    f.write("This line will be appended.\n")
    f.write("Another appended line.\n")
# 2.3 Writing multiple lines
lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines_to_write)

# 3. Handling errors
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")    

# 4. Checking if a file exists
#using os module
import os
if os.path.exists("sample.txt"):
    print("File exists.")
else:
    print("File does not exist.")
# delete files
import os

if os.path.exists("old_log.txt"):
    os.remove("old_log.txt")

# 5. using pathlib module
from pathlib import Path
file_path = Path("sample.txt")
if file_path.is_file():
    print("File exists.")
else:
    print("File does not exist.")

# File handling with matplotlib
from pathlib import Path

log_file = Path("/var/log/app.log")

print(log_file.name)
print(log_file.parent)
print(log_file.suffix)

"""
Output:
app.log
/var/log
.log
"""
# create directory
from pathlib import Path

backup_dir = Path("backups")
backup_dir.mkdir(exist_ok=True)

#list files in a directory
from pathlib import Path

for file in Path("/var/log").iterdir():
    print(file)


# 6. Reading Large Log Files Efficiently
with open("application.log", "r") as log:
    for line in log:
        if "ERROR" in line:
            print(line)

# 7. JSON File Handling
import json
# Writing JSON data to a file
data = {
    "server": "web-01",
    "ip": "192.168.1.100"
}
with open("server_config.json", "w") as f:
    json.dump(data, f)
# Reading JSON data from a file
with open("server_config.json", "r") as f:
    config = json.load(f)
    print(config)

# 8. YAML File Handling
import yaml
# Writing YAML data to a file
yaml_data = {
    "server": "web-01",
    "ip": "192.168.1.100"
}
with open("server_config.yaml", "w") as f:
    yaml.dump(yaml_data, f)
# Reading YAML data from a file
with open("server_config.yaml", "r") as f:
    config = yaml.safe_load(f)
    print(config)

# 9. Log Rotation : Delete logs older than 7 days
import os
import time

path = "/var/log/myapp"

days = 7
current_time = time.time()

for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        age = current_time - os.path.getmtime(file_path)

        if age > (days * 86400):
            os.remove(file_path)
            print(f"Deleted: {file}")
# 10. Working with Environment Files (.env)
"""
example.env:
DB_HOST=localhost
DB_PORT=5432
"""
from dotenv import dotenv_values

config = dotenv_values(".env")

print(config["DB_HOST"])

# Install : pip install python-dotenv

