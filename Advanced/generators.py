"""
Python Generators Tutorial
Generators are functions that return an iterator object using the 'yield' keyword.
They produce values one at a time and are memory efficient.
"""

# Basic Generator Example
def simple_generator():
    """A simple generator that yields numbers 0 to 2"""
    yield 0
    yield 1
    yield 2

print("=== Basic Generator ===") # Using the generator
for value in simple_generator():
    print(value)


# Generator with Range
def count_up_to(n):
    """Generator that counts from 1 to n"""
    i = 1
    while i <= n:
        yield i
        i += 1


print("\n=== Generator with Range ===")
for num in count_up_to(5):
    print(num)


# Generator Expression
print("\n=== Generator Expression ===")
gen_expr = (x * 2 for x in range(5))
print(list(gen_expr))


# Generator with State
def fibonacci(n):
    """Generator that yields Fibonacci numbers up to n terms"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


print("\n=== Fibonacci Generator ===")
for fib in fibonacci(7):
    print(fib, end=" ")
print()


# Generator with send() method
def counter():
    """Generator that receives values via send()"""
    count = 0
    while True:
        x = yield count
        if x is not None:
            count = x
        else:
            count += 1


print("\n=== Generator with send() ===")
gen = counter()
print(next(gen))  # 0
print(next(gen))  # 1
print(gen.send(10))  # 10
print(next(gen))  # 11


# Generator Delegation with yield from
def gen1():
    """First sub-generator"""
    yield 1
    yield 2


def gen2():
    """Second sub-generator"""
    yield 3
    yield 4


def combined_gen():
    """Delegates to multiple generators"""
    yield from gen1()
    yield from gen2()


print("\n=== Generator Delegation ===")
for val in combined_gen():
    print(val, end=" ")
print()


# Memory Efficiency Comparison
print("\n=== Memory Efficiency ===")
import sys

# List vs Generator
list_comp = [x ** 2 for x in range(1000)]
gen_comp = (x ** 2 for x in range(1000))

print(f"List size: {sys.getsizeof(list_comp)} bytes")
print(f"Generator size: {sys.getsizeof(gen_comp)} bytes")
