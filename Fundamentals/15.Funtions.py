# Python Functions Tutorial

# 1. Basic Function Definition
def greet():
    """A simple function that prints a greeting."""
    print("Hello, World!")

greet()


# 2. Function with Parameters
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")


# 3. Function with Default Parameters
def greet_user(name="Guest"):
    """Greet a user with an optional name."""
    print(f"Hello, {name}!")

greet_user()
greet_user("Alice")


# 4. Function with Multiple Return Values
def get_min_max(numbers):
    """Return both minimum and maximum values."""
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {min_val}, Max: {max_val}")


# 5. Function with *args (Variable Length Arguments)
def sum_all(*numbers):
    """Sum any number of arguments."""
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))


# 6. Function with **kwargs (Keyword Arguments)
def print_info(**kwargs):
    """Print key-value pairs."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Bob", age=30, city="NYC")


# 7. Lambda Functions (Anonymous functions)
square = lambda x: x ** 2
print(f"Square of 4: {square(4)}")

# Using lambda with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")


# 8. Nested Functions
def outer(x):
    """Function containing a nested function."""
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
print(f"5 + 3 = {add_five(3)}")


# 9. Scope: Local and Global Variables
global_var = "I'm global"

def scope_example():
    local_var = "I'm local"
    print(local_var)
    print(global_var)

scope_example()


# 10. Decorators (Advanced)
def my_decorator(func):
    """A simple decorator that wraps a function."""
    def wrapper(*args, **kwargs):
        print("Something before the function")
        result = func(*args, **kwargs)
        print("Something after the function")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Charlie")
