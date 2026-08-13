"""
Use shutil for high-level file and folder operations like copy, move, delete, backup, and disk usage checks. Python docs describe shutil as a module for high-level operations on files and collections of files.

DevOps use cases:

Backup files
Move logs
Archive reports
Delete old folders
Check disk usage
"""
# Copy a File
import shutil

source = "C:/Source/app.log"
destination = "C:/Backup/app.log"

shutil.copy(source, destination)

print("File copied")

# Copy a File with Metadata
import shutil

shutil.copy2("C:/Source/app.log", "C:/Backup/app.log")

# Move a File
import shutil

shutil.move("C:/Downloads/report.pdf", "C:/Documents/report.pdf")

print("File moved")

# Copy entire Folder
import shutil

shutil.copytree("C:/SourceFolder", "C:/BackupFolder")

# Delete entire folder
import shutil

shutil.rmtree("C:/TempFiles")

print("Folder deleted")

# Check disk usage
import shutil

usage = shutil.disk_usage("C:/")

free_percent = usage.free / usage.total * 100

print(f"Free Space: {free_percent:.2f}%")

if free_percent < 20:
    print("WARNING: Low disk space")
else:
    print("Disk space is okay")
