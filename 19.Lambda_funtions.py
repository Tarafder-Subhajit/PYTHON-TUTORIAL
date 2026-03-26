# Lambda Functions in Python
# Lambda is a small anonymous function that can take any number of arguments but only one expression

# Syntax: lambda arguments: expression

# Example 1: Simple lambda function
# Regular function
def add(x, y):
    return x + y

# Equivalent lambda function
add_lambda = lambda x, y: x + y

print("Example 1: Basic Lambda")
print(add(5, 3))           # Output: 8
print(add_lambda(5, 3))    # Output: 8

# Example 2: Lambda with single argument
square = lambda x: x ** 2
print("\nExample 2: Single Argument")
print(square(5))  # Output: 25

# Example 3: Lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("\nExample 3: Lambda with map()")
print(squared)  # Output: [1, 4, 9, 16, 25]

# Example 4: Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("\nExample 4: Lambda with filter()")
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Example 5: Lambda with sorted()
students = [('Alice', 25), ('Bob', 20), ('Charlie', 23)]
sorted_by_age = sorted(students, key=lambda x: x[1])
print("\nExample 5: Lambda with sorted()")
print(sorted_by_age)  # Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

# Key Points:
# - Lambda functions are anonymous (no name required)
# - Limited to a single expression
# - Often used with map(), filter(), sorted()
# - Good for short, simple operations
# - Less readable for complex logic (use regular functions instead)