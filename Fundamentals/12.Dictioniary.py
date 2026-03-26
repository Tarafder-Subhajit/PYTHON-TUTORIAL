# Python Dictionary Tutorial

# 1. Creating Dictionaries
# Empty dictionary
empty_dict = {}
empty_dict2 = dict()

# Dictionary with initial values
person = {
    "name": "John",
    "age": 30,
    "city": "New York",ghu
    "is_student": False
}

# 2. Accessing Dictionary Values
print(person["name"])  # Output: John
print(person.get("age"))  # Output: 30
print(person.get("email", "Not found"))  # Output: Not found

# 3. Modifying Dictionaries
person["age"] = 31  # Update value
person["email"] = "john@example.com"  # Add new key-value pair

# 4. Dictionary Methods
print(person.keys())  # Get all keys
print(person.values())  # Get all values
print(person.items())  # Get key-value pairs

# 5. Iterating through Dictionary
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")

# 6. Checking if Key Exists
if "name" in person:
    print("Name key exists")

# 7. Removing Items
del person["is_student"]  # Delete specific key
person.pop("email")  # Remove and return value

# 8. Dictionary Comprehension
numbers = {x: x**2 for x in range(5)}
print(numbers)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 9. Merging Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(merged)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 10. Nested Dictionaries
student = {
    "name": "Alice",
    "grades": {"math": 95, "english": 88},
    "contact": {"email": "alice@example.com", "phone": "123-456-7890"}
}
print(student["grades"]["math"])  # Output: 95
