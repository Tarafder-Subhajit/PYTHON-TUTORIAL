import array
import numpy as np

# Creating arrays with different types
int_array = array.array('i', [1, 2, 3, 4, 5])
float_array = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])

print("Integer Array:", int_array)
print("Float Array:", float_array)

# Accessing elements
print("\nFirst element:", int_array[0])
print("Last element:", int_array[-1])

# Modifying elements
int_array[2] = 30
print("Modified array:", int_array)

# Array methods
int_array.append(6)
print("After append:", int_array)

int_array.extend([7, 8, 9])
print("After extend:", int_array)

# Using lists as arrays (more flexible alternative)
list_array = [10, 20, 30, 40, 50]
print("\nList as array:", list_array)
print("Length:", len(list_array))
print("Slice [1:4]:", list_array[1:4])

# Iterating through array
print("\nIterating through array:")
for item in int_array:
    print(item, end=" ")
print()

# Using NumPy arrays (more powerful for numerical computing)
try:
    np_array = np.array([1, 2, 3, 4, 5])
    print("\nNumPy array:", np_array)
    print("Array shape:", np_array.shape)
    print("Array dtype:", np_array.dtype)
except ImportError:
    print("\nNumPy not installed")
