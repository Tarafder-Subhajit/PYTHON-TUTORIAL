# Given three inputs that are stored in the variables a, b, and c. 
# You need to print a a times and b b times  in a single line separated by c.



a = input()
b = input()
c = input()

print(a * int(a) + c + b * int(b))

#int(a) converts the first input to a number
# a * int(a) repeats the string a that many times