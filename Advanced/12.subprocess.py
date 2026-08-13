"""
Use subprocess to run system commands from Python. Python docs say subprocess.run() is the recommended approach for many common command execution use cases.

DevOps use cases:

Run git status
Run kubectl get pods
Run docker ps
Run az commands
Run aws commands
Run PowerShell commands
"""
# Basic Command
import subprocess

subprocess.run(["hostname"])

# Capture Windows Command Output
import subprocess

result = subprocess.run(
    ["hostname"],
    capture_output=True,
    text=True               # gives output as string instead of bytes
)

print(result.stdout)

# Run git command
import subprocess

result = subprocess.run(
    ["git", "status"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("Command successful")
else:
    print("Command failed")
    print(result.stderr)

# Check K8s pods
import subprocess

result = subprocess.run(
    ["kubectl", "get", "pods"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print(result.stdout)
else:
    print("Error running kubectl")
    print(result.stderr)