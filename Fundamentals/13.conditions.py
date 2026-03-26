# Python Conditions Tutorial

# 1. Basic if statement
age = 18
if age >= 18:
    print("You are an adult")

# 2. if-else statement
temperature = 15
if temperature > 20:
    print("It's warm")
else:
    print("It's cold")

# 3. if-elif-else statement
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# 4. Nested conditions
username = "admin"
password = "secret123"
if username == "admin":
    if password == "secret123":
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("User not found")

# 5. Logical operators (and, or, not)
x = 10
y = 20
if x > 5 and y > 15:
    print("Both conditions are True")

if x > 15 or y > 15:
    print("At least one condition is True")

if not (x > 15):
    print("x is not greater than 15")

# 6. Ternary operator (conditional expression)
result = "Adult" if age >= 18 else "Minor"
print(result)

# 7. Membership operators (in, not in)
fruits = ["apple", "banana", "orange"]
if "apple" in fruits:
    print("Apple is in the list")

# 8. Identity operators (is, is not)
a = [1, 2, 3]
b = a
if a is b:
    print("a and b are the same object")

# 9. Match Statement (Structural Pattern Matching - Python 3.10+)
# The match statement is like a switch statement but more powerful
# It allows pattern matching against different cases

# Example 1: Simple value matching
def describe_number(num):
    match num:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case 2:
            return "Two"
        case _:  # _ is the default case (like default in switch)
            return "Other number"

print(describe_number(1))  # Output: One
print(describe_number(5))  # Output: Other number

