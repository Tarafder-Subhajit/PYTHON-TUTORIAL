"""
TUPLES IN PYTHON
A tuple is an immutable sequence type that can hold multiple items.
Once created, tuples cannot be modified (no adding, removing, or changing elements).
"""

# Creating tuples
empty_tuple = ()
single_element = (1,)  # Note: comma is required for single element
tuple_from_list = tuple([1, 2, 3])
my_tuple = (1, 2, 3, "hello", 3.14, True)
nested_tuple = (1, 2, (3, 4, 5))

print("Basic tuples:")
print(f"Empty: {empty_tuple}")
print(f"Single element: {single_element}")
print(f"Mixed types: {my_tuple}")
print(f"Nested: {nested_tuple}\n")

# Accessing elements (indexing and slicing)
print("Accessing elements:")
print(f"First element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")
print(f"Slice [1:3]: {my_tuple[1:3]}")
print(f"Every 2nd element: {my_tuple[::2]}\n")

# Tuple unpacking
print("Unpacking:")
a, b, c, *rest = (1, 2, 3, 4, 5)
print(f"a={a}, b={b}, c={c}, rest={rest}\n")

# Tuple methods
print("Tuple methods:")
numbers = (1, 2, 3, 2, 4, 2)
print(f"count(2): {numbers.count(2)}")
print(f"index(3): {numbers.index(3)}\n")

# Tuple iteration
print("Iteration:")
for i, value in enumerate(("apple", "banana", "cherry")):
    print(f"{i}: {value}")
print()

# Tuple concatenation and repetition
print("Concatenation and repetition:")
t1 = (1, 2)
t2 = (3, 4)
print(f"Concatenation: {t1 + t2}")
print(f"Repetition: {t1 * 3}\n")

# Checking membership
print("Membership:")
print(f"2 in (1, 2, 3): {2 in (1, 2, 3)}\n")

# Converting to tuple
print("Conversion:")
print(f"tuple('abc'): {tuple('abc')}")
print(f"tuple([1, 2, 3]): {tuple([1, 2, 3])}\n")

# Tuples as dictionary keys (immutable)
print("Tuples as dictionary keys:")
coords = {(0, 0): "origin", (1, 1): "diagonal"}
print(coords[(0, 0)])
