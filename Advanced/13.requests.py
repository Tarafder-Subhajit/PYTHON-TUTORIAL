"""
Use requests to call REST APIs. The Requests documentation describes it as a simple HTTP library for Python that allows HTTP requests easily.

DevOps use cases:

Call GitHub API
Call Jira API
Call ServiceNow API
Check application health URL
Call Azure DevOps API
Send webhook notifications
"""
# Install: pip install requests

# Simple GET Requests
import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.text)

# Convert JSON Response to a python dictionary
import requests

response = requests.get("https://api.github.com")

data = response.json()

print(data)

# Check website health
import requests

url = "https://example.com"

response = requests.get(url)

if response.status_code == 200:
    print("Application is UP")
else:
    print("Application is DOWN")

# Use timeout
import requests

try:
    response = requests.get("https://example.com", timeout=5)
    print(response.status_code)
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException as error:
    print("Request failed:", error)

# Send Header
import requests

headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Accept": "application/json"
}

response = requests.get(
    "https://api.github.com/user",
    headers=headers
)

print(response.status_code)
print(response.json())

# POST request
import requests

url = "https://example.com/api"

payload = {
    "server": "web01",
    "status": "running"
}

response = requests.post(url, json=payload)

print(response.status_code)