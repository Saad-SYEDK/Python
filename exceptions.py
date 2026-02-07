# Exception Handling

# An exception is an error that occurs during the execution of a program.
# When an exception occurs, the normal flow of the program is interrupted and the program may crash.
# To avoid this, we can use exception handling to catch and handle exceptions gracefully.
# The basic syntax for exception handling in Python is as follows:
try:
    pass # using pass to avoid syntax error, replace with actual code
    # Code that may raise an exception
except ExceptionType: 
    pass
    # Code to handle the exception
    # Required if finally is not used
else:
    pass
    # Code to execute if no exception occurs
    # Optional
finally:
    pass 
    # Code to execute regardless of whether an exception occurs or not
    # Optional


# Example of exception handling - Division by zero
# We cannot divide a number by zero, it will raise a ZeroDivisionError and the program will crash.
try:
    a = 1
    b = 0
    result = a / b
except ZeroDivisionError: # If we know the exception type, we can catch it specifically
                          # we can use generic Exception to catch all exceptions like except Exception:
                          # it is not recommended as it may hide other exceptions that we did not anticipate.
    print("Cannot divide by zero!")
else:
    print("The result is:", result)
finally:
    print("This will always be executed.")
    
# There are many built-in exceptions, search for them.
# We can also create custom exceptions.