#----------------------------------------------------ITERATOR & ITERABLE--------------------------------------------------------------

# We are using "for item in sequence". But how does Python get each item?

"""
ITERABLE - An object that can be looped over e.g. lists, sets, tuples, dictionary etc. 
An object is considered iterable if it implements the __iter__() special method.
__iter__() returns an iterator.
ITERATOR produces the next value in the sequence.
An object is considered iterable if it implements the __next__() special method. When there are no more items, the method raises StopIteration exception.
"""

s = "GFG"
it = iter(s)

print(next(it)) # s is an iterable (string).
print(next(it)) # iter(s) creates an iterator.
print(next(it)) # next(it) retrieves characters one by one.

"""
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

As you will learn in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.

The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence.
"""

class EvenNumbers:
    def __iter__(self): # Initialization: The __iter__() method initializes the iterator at 2, the first even number.
        self.n = 2  # Start from the first even number
        return self

    def __next__(self): #Iteration: The __next__() method retrieves the current number and then increases it by 2, ensuring the next call returns the subsequent even number.
        x = self.n
        self.n += 2  # Increment by 2 to get the next even number
        return x

# Create an instance of EvenNumbers
even = EvenNumbers()
it = iter(even)

# Print the first five even numbers
print(next(it))  
print(next(it)) 
print(next(it))  
print(next(it)) 
print(next(it))

"""
StopIteration Exception:

StopIteration exception is integrated with Python’s iterator protocol. It signals that the iterator has no more items to return. Once this exception is raised, further calls to next() on the same iterator will continue raising StopIteration.
"""
li = [100, 200, 300]
it = iter(li)

# Iterate until StopIteration is raised
while True:
    try:
        print(next(it))
    except StopIteration:
        print("End of iteration")
        break
