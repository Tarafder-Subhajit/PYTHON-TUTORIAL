# Decorators in Python

# A decorator is a function that takes another function and extends its behavior without modifying it.
# A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.
# Define the decorator first, then apply it with @decorator_name above the function.

# Example 1: Simple decorator
def decorator(func): # defining a decorator function that takes another function as an argument 
    def wrapper(): # defining a wrapper function that will enhance the behavior of the original function
        print("Before calling the function.")
        func() # calling the original function inside the wrapper
        print("After calling the function.")
    return wrapper

@decorator # Applying the decorator to a function. @decorator syntax is a shorthand for greet = decorator(greet).
def greet(): # defining a function that will be decorated
    print("Hello, World!")

greet()

# Multiple Decorators calls

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

# Arguments in Decorated Functions

def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

@decorator_name
def add(a, b):
    return a + b

print(add(5, 3))

# Types of Decorators
# 1. Function Decorators: These are the most common type of decorators that modify the behavior of functions.
# 2. Class Decorators: These decorators modify the behavior of classes. They can be used to add methods, modify attributes, or change the class's behavior in some way.
# 3. Method Decorators: These decorators are used to modify the behavior of methods within  a class. They can be used to add functionality to methods, such as logging, timing, or access control.                                  

# Class Decorator Example


