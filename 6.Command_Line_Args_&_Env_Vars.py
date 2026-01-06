import sys

print("Total arguments:", len(sys.argv))
print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])

total = 0
for arg in sys.argv[1:]:
    total += int(arg)

print("Sum =", total)
print("-------------------------------------------------------------------------------------------------------------------")

#Explanation:

#sys.argv[0]: script name (e.g., add.py).
#sys.argv[1:]: user-provided arguments (e.g., numbers).
#len(sys.argv): gives total count of arguments.
#A loop converts arguments to integers and sums them.


#ENVIRONMENT VARIABLE
#------------------------------------------------------------------------------------------------------------------------------------
# we cannot pass passwords or sensitive info through command line args
# thus we use env vars.
# just type the cmd "env" in terminal to check the environment variable
# to create manual env vars -> export password="subha" -> check in env
# To Access environment variables in Python's we can use the OS module
# import os module
import os

# display all environment variable
#print("PRINTING ALL THE ENV VARS")
#print("===============================================================================================================================")
#print(os.environ)
#print("===============================================================================================================================")

# access environment variable
home_dir = os.getenv('password')
print(home_dir)