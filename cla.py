# We can take and parse input form command line arguments using the argparse module.

import argparse

parser = argparse.ArgumentParser()

# Add Arguments with their description
parser.add_argument("num1", help="first number")
parser.add_argument("num2", help="Second number")
parser.add_argument("operation", help="Operation")

args =  parser.parse_args()
# The arguments will be parsed, we can our arguments using args.Num1, argss.Num2, etc

# Now, in Command Line if we run "python file_name.py -h" we will get the description

n1 = int(args.num1)
n2 = int(args.num2)

if args.operation == "add":
    result = n1+n2
elif args.operation == "sub":
    result = n1-n2

print(result)
# In Command Line if we run "python file_name.py 1 2 add" we will get 3 

# we have different types of arguments like optional, positional, etc
# THe above example is of positional arguments, we can also have optional arguments with default values, etc
# We can also have different types of arguments like int, float, etc, we can also have choices for arguments, etc
# We also have optional arguments.

# Look into the documentation for more details on argparse module.
# https://docs.python.org/3/library/argparse.html