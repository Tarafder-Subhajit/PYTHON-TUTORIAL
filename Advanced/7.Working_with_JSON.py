"""
JSON = JavaScript Object Notation. It's simply a way to represent structured data.
data = {
    "server": "web01",
    "cpu": 85,
    "healthy": True
}


aws ec2 describe instances
Output:
{
  "Reservations": [
    {
      "Instances": [
        {
          "InstanceId": "i-12345"
        }
      ]
    }
  ]
}
"""
# To work with JSON we need to import JSON module
import json

server = {
    "hostname": "web01",
    "ip": "10.0.0.5",
    "status": "running"
}

json_data = json.dumps(server) #Convert Python object to JSON string.
print(json_data)
# Output: {"hostname": "web01", "ip": "10.0.0.5", "status": "running"}

print(json.dumps(server, indent=4))
"""
Output:
{
    "hostname": "web01",
    "ip": "10.0.0.5",
    "status": "running"
}
"""

# JSON String → Python Dictionary
json_response = '''                  # This stores a JSON-formatted string inside a variable.
{
    "hostname": "web01",
    "status": "running"
}
'''
import json

data = json.loads(json_response)    # loads the JSON string and converts it into a Python object (in this case, a dictionary as its a key-value structure).

print(data)

# Accessing Values
data = {
    "hostname": "web01",
    "status": "running"
}
print(data["hostname"])
print(data.get("hostname")) # Safer Approach to access values. It will return None if the key doesn't exist instead of throwing an error.

# Nested JSON
nested_json = {
    "server": {
        "hostname": "web01",
        "status": "running"
    },
    "cpu": 85,
    "healthy": True
}
print(nested_json["server"]["hostname"])
print(nested_json["cpu"])

#JSON Arrays
data = {
    "servers": [
        "web01",
        "web02",
        "web03"
    ]
}
print(data["servers"][0])

#loop through
for server in data["servers"]:
    print(server)


# Writing JSON To a File
import json

data = {
    "hostname": "web01",
    "status": "running"
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)



"""
Note:
json.load() -> Read JSON file
json.loads() -> Read JSON string
json.dump() -> Write JSON file
json.dumps() -> Write JSON string
"""