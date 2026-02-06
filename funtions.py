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