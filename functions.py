# Functions in Python
# Functions are reusable blocks of code that perform a specific task.
# They help organize code and make it more modular.
# You can define a function using the def keyword.

# Here's an example of a simple function:
def greet(name):
    print("Hello,", name)

# You can call the function like this:
greet("Alice")
greet("Bob")
greet("Charlie")
# This will print the greeting message for each name.

# Functions can also return values using the return statement.
def add(a, b):
    return a + b

# You can call the function and store the result like this:
result = add(5, 3)
print("Addition Result:", result)
# This will print the result of the addition.

# Functions can have default parameters, which are used if no argument is provided.
def multiply(a, b=2):
    return a * b
# You can call the function with one or two arguments:
print("Multiplication Result with default b:", multiply(4))  # Uses default b=2
print("Multiplication Result with b=3:", multiply(4, 3))  # Uses b=3
# This will print the results of the multiplication with and without the default parameter.

# Functions can also accept a variable number of arguments using *args and **kwargs.
def print_args(*args):
    for arg in args:
        print("Argument:", arg)
print_args(1, 2, 3, "hello")
# This will print each argument passed to the function.

def print_kwargs(**kwargs):  # Accepts keyword arguments, which are passed as a dictionary->future topic.
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name="Alice", age=30)
# This will print each key-value pair passed to the function.

# Functions are a fundamental part of Python programming and are used extensively in various applications.
# Practice defining and using functions to become more comfortable with them!


""""Exercise: Functions

1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
    area = (1/2)*base*height
    Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
    rectangle area=length*width
    If no shape is supplied then it should take triangle as a default shape

2. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
    *
    **
    ***
    if input is 4 then it should print
    *   
    **
    ***
    ****
    Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

"""

# Solution 

# 1.
def calculate_area(h,w, shape):
    if shape == "rectangle":
        return h * w
    else:
        return (1/2) * h * w

# 2.
def print_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()