# List Comprehension Examples

# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)  # [1, 4, 9, 16, 25]

# With condition
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # [2, 4]

# String to list of characters
text = "hello"
chars = [char.upper() for char in text]
print(chars)  # ['H', 'E', 'L', 'L', 'O']

# Nested list comprehension
matrix = [[x * y for y in range(1, 4)] for x in range(1, 4)]
print(matrix)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# List comprehension with multiple conditions
filtered = [x for x in range(1, 11) if x % 2 == 0 if x > 5]
print(filtered)  # [6, 8, 10]

# With else clause
result = [x if x % 2 == 0 else x*2 for x in range(1, 6)]
print(result)  # [2, 2, 6, 4, 10]
