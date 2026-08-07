# Python does not include YAML support by default. -> pip install pyyaml
import yaml

"""
config.yaml:
app:
  name: nginx
  replicas: 3
"""

# Reading YAML Files
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)  # safe_load is used to load YAML data safely without executing arbitrary code.
    print(config)

# Accessing Values
print(config["app"]["name"])
print(config["app"]["replicas"])

# YAML Lists
"""
config.yaml:
servers:
  - web01
  - web02
  - web03
"""

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

for server in config["servers"]:
    print(server)

# Writing YAML from Python
import yaml

config = {
    "app": {
        "name": "payment-service",
        "environment": "prod",
        "replicas": 5
    },
    "database": {
        "host": "prod-db.internal",
        "port": 5432
    }
}

with open("generated-config.yaml", "w") as file:
    yaml.safe_dump(config, file, sort_keys=False) # By default, PyYAML may sort dictionary keys alphabetically during dumping. Using sort_keys=False helps preserve the insertion order, which is useful when generating readable DevOps config files.


# Practical DevOps Example: Modify Kubernetes Deployment YAML
"""
Suppose you have a Kubernetes deployment YAML file named deployment.yaml:
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-service
spec:
  replicas: 2
  template:
    spec:
      containers:
        - name: payment-service
          image: myregistry/payment-service:v1
          ports:
            - containerPort: 8080
"""
# Now you want Python to update: replicas from 2 to 5 & image tag from v1 to v2
import yaml

with open("deployment.yaml", "r") as file:
    deployment = yaml.safe_load(file)

deployment["spec"]["replicas"] = 5

containers = deployment["spec"]["template"]["spec"]["containers"]
containers[0]["image"] = "myregistry/payment-service:v2"

with open("deployment-updated.yaml", "w") as file:
    yaml.safe_dump(deployment, file, sort_keys=False)


# Validate YAML Structure
import yaml

required_top_level_keys = ["apiVersion", "kind", "metadata", "spec"]

with open("deployment.yaml", "r") as file:
    data = yaml.safe_load(file)

for key in required_top_level_keys:
    if key not in data:
        raise ValueError(f"Missing required key: {key}")

if data["kind"] != "Deployment":
    raise ValueError("This YAML is not a Kubernetes Deployment")

if "name" not in data["metadata"]:
    raise ValueError("Deployment metadata.name is missing")

print("YAML validation passed")

