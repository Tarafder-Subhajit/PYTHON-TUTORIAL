# ============================================================================
# Enumerate and ZIP Functions in Python
# ============================================================================

# ====================
# 1. ENUMERATE FUNCTION
# ====================
# enumerate() adds a counter to an iterable, returning (index, value) pairs

print("=== ENUMERATE ===\n")

# Basic example
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print()

# With custom start value
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

print()

# Converting to list
result = list(enumerate(fruits))
print("enumerate() as list:", result)

print("\n" + "="*50 + "\n")

# ====================
# 2. ZIP FUNCTION
# ====================
# zip() combines multiple iterables element-wise

print("=== ZIP ===\n")

# Basic example
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

print()

# Converting to list
result = list(zip(names, ages, cities))
print("zip() as list:", result)

print()

# Different lengths (zip stops at shortest)
short_list = ['a', 'b']
long_list = [1, 2, 3, 4, 5]
result = list(zip(short_list, long_list))
print("Different lengths:", result)

print("\n" + "="*50 + "\n")

# ====================
# 3. COMBINING ENUMERATE AND ZIP
# ====================

print("=== ENUMERATE + ZIP ===\n")

for index, (name, age) in enumerate(zip(names, ages), start=1):
    print(f"#{index}: {name} is {age} years old")

print()

# Unpacking zip for matrix operations
matrix_rows = list(zip(names, ages, cities))
# Transpose
names_back, ages_back, cities_back = zip(*matrix_rows)
print("Transposed names:", names_back)
print("Transposed ages:", ages_back)
