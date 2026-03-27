#----------------------------------------------------ITERATOR & ITERABLE--------------------------------------------------------------

# We are using "for item in sequence". But how does Python get each item?

"""
ITERABLE - An object that can be looped over e.g. lists, sets, tuples, dictionary etc. 
An object is considered iterable if it implements the __iter__() special method.
__iter__() returns an iterator.
ITERATOR produces the next value in the sequence.
An object is considered iterable if it implements the __next__() special method. When there are no more items, the method raises StopIteration exception.
"""


