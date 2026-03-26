# Python Lists Tutorial

# 1. Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [1, [2, 3], [4, 5, 6]]

# 2. Accessing elements
first = numbers[0]  # 1
last = numbers[-1]  # 5
slice_list = numbers[1:4]  # [2, 3, 4] i.e. includes index 1, 2, 3 but not 4

# 3. Modifying lists
numbers.append(6)  # Add to end
numbers.insert(0, 0)  # Insert at index
numbers.remove(3)  # Remove first occurrence
popped = numbers.pop()  # Remove and return last item

# 4. List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]
repeated = list1 * 2  # [1, 2, 3, 1, 2, 3]

# 5. List methods
numbers.sort()  # Sort in place
reversed_list = sorted(numbers, reverse=True)  # Sorted copy
numbers.reverse()  # Reverse in place
count = numbers.count(2)  # Count occurrences
index = numbers.index(2)  # Find index

# 6. List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# 7. Iterating through lists
for item in numbers:
    print(item)

for i, item in enumerate(numbers):
    print(f"Index {i}: {item}")
