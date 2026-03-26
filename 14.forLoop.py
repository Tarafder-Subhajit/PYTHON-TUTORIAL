# For Loop Examples in Python

# 1. Basic for loop with range
print("1. Basic for loop with range:")
for i in range(5):
    print(i)

print("\n2. For loop with range(start, stop, step):")
for i in range(1, 10, 2):
    print(i)

print("\n3. For loop through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\n4. For loop with index using enumerate:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print("\n5. For loop through a string:")
for char in "Python":
    print(char)

print("\n6. For loop with dictionary:")
student = {"name": "John", "age": 20, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")

print("\n7. Nested for loop:")
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()

print("\n8. For loop with break and continue:")
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    print(i)

print("\n9. For loop with else:")
for i in range(5):
    print(i)
else:
    print("Loop completed!")