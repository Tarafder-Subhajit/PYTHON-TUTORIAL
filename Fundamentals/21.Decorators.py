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

def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

# *args and **kwargs

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

# Multiple Decorators
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

# Preserving Function Metadata & functools.wraps decorator

# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
# Normally, a function's name can be returned with the __name__ attribute:
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

# But, when a function is decorated, the metadata of the original function is lost.
# Try returning the name from a decorated function and you will not get the same result:
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

# To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.
import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)




