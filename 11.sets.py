# Python Sets Tutorial

# 1. Creating Sets
print("=== Creating Sets ===")
my_set = {1, 2, 3, 4, 5}
print(f"Set: {my_set}")

# Empty set must use set() - {} creates an empty dict
empty_set = set()
print(f"Empty set: {empty_set}")

# Creating from a list (removes duplicates)
from_list = set([1, 2, 2, 3, 3, 3])
print(f"Set from list: {from_list}")


# 2. Set Operations
print("\n=== Set Operations ===")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
print(f"Union: {set_a | set_b}")
print(f"Union: {set_a.union(set_b)}")

# Intersection
print(f"Intersection: {set_a & set_b}")
print(f"Intersection: {set_a.intersection(set_b)}")

# Difference
print(f"Difference (A - B): {set_a - set_b}")
print(f"Difference (B - A): {set_b - set_a}")

# Symmetric Difference
print(f"Symmetric Difference: {set_a ^ set_b}")


# 3. Adding and Removing Elements
print("\n=== Adding/Removing Elements ===")
my_set = {1, 2, 3}
my_set.add(4)
print(f"After add(4): {my_set}")

my_set.update([5, 6, 7])
print(f"After update([5, 6, 7]): {my_set}")

my_set.remove(3)  # Raises KeyError if not found
print(f"After remove(3): {my_set}")

my_set.discard(1)  # No error if not found
print(f"After discard(1): {my_set}")

popped = my_set.pop()  # Removes arbitrary element
print(f"Popped: {popped}, Set: {my_set}")

my_set.clear()
print(f"After clear(): {my_set}")


# 4. Set Methods
print("\n=== Set Methods ===")
set_x = {1, 2, 3}
set_y = {2, 3, 4}

print(f"set_x.issubset(set_y): {set_x.issubset(set_y)}")
print(f"set_x.issuperset(set_y): {set_x.issuperset(set_y)}")
print(f"set_x.isdisjoint(set_y): {set_x.isdisjoint(set_y)}")
print(f"set_x.copy(): {set_x.copy()}")


# 5. Membership Testing
print("\n=== Membership Testing ===")
my_set = {'a', 'b', 'c'}
print(f"'a' in my_set: {'a' in my_set}")
print(f"'z' in my_set: {'z' in my_set}")


# 6. Iteration
print("\n=== Iteration ===")
my_set = {1, 2, 3, 4}
for element in my_set:
    print(element)


# 7. Frozenset (Immutable Set)  
print("\n=== Frozenset ===")
frozen = frozenset([1, 2, 3])
print(f"Frozenset: {frozen}")                           
# Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.