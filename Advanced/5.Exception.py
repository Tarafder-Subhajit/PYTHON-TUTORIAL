"""
An exception is an error that occurs while a program is running. 
Python distinguishes between syntax errors, which happen when code cannot be parsed, and exceptions, 
which happen during execution even if the syntax is valid.
ex: print(10 / 0)
o/p: ZeroDivisionError: division by zero

Syntax:
try:                         -> Runs the risky code that might cause an error.
      # Code 
except SomeException:        -> Catches and handles the error if one occurs.
      # Code 
else:                         -> Executes only if no exception occurs in try.
     # Code 
finally:                      -> Runs regardless of what happens , useful for cleanup tasks like closing files.
    # Code 

ex: 
n = 0
try:
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")

"""

# 1. Specific Exceptions:
# Ex 1:
try:
    x = int("str")  # This will cause ValueError
    inv = 1 / x   # Inverse calculation
    
except ValueError:
    print("Not Valid!")
    
except ZeroDivisionError:
    print("Zero has no inverse!")

# Ex 2:
import os
try:
    region = os.environ["AWS_REGION"]
except KeyError:
    print("AWS_REGION environment variable is missing")


# 2. Multiple Exceptions:
# Ex 1:
a = ["10", "twenty", 30]
try:
    total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int
    
except (ValueError, TypeError) as e:
    print("Error", e)
    
except IndexError:
    print("Index out of range.")

# Ex 2:
try:
    with open("/var/log/app.log", "r") as file:
        logs = file.readlines()
except FileNotFoundError:
    print("Log file does not exist")
except PermissionError:
    print("Permission denied while reading log file")

# 3. Catching multiple exceptions in one block
try:
    with open("/secure/config.json", "r") as file:
        data = file.read()
except (FileNotFoundError, PermissionError) as error:
    print(f"Could not read config file: {error}")

# 4. Using as e to capture exception details
try:
    with open("/tmp/deployment_status.txt", "r") as file:
        status = file.read()
except FileNotFoundError as e:
    print(f"Deployment status file missing: {e}")

# 5: Raising exceptions manually with raise: Python allows user code to raise built-in exceptions or custom exceptions.
def validate_replicas(count):
    if count < 1:
        raise ValueError("Replica count must be at least 1")
    return count

try:
    validate_replicas(0)
except ValueError as e:
    print(f"Validation error: {e}")

# 6. Re-raising the exceptions: Re-raising means raising the same exception again from inside an except block.
try:
    risky_operation()
except SomeException as e:
    print(f"Something failed: {e}")
    raise                   # raise sends the same exception upward again

# 7. Exception chaining with raise ... from : Python supports exception chaining using raise new_exception from original_exception, 
# which records the original cause of the new exception.
try:
    port = int("abc")
except ValueError as e:
    raise RuntimeError("Invalid application configuration") from e

# 8. Custom Exceptions:

class KubernetesDeploymentError(Exception):
    pass

def check_rollout_status(status):
    if status != "success":
        raise KubernetesDeploymentError(f"Rollout failed with status: {status}")

try:
    check_rollout_status("failed")
except KubernetesDeploymentError as e:
    print(f"Kubernetes deployment failed: {e}")

# 9. Common Exceptions : FileNotFoundError, PermissionError, KeyError, ValueError, TimeoutError, OSError
