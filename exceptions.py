# Exception Handling

# An exception is an error that occurs during the execution of a program.
# When an exception occurs, the normal flow of the program is interrupted and the program may crash.
# To avoid this, we can use exception handling to catch and handle exceptions gracefully.
# The basic syntax for exception handling in Python is as follows:
try:
    pass # using pass to avoid syntax error, replace with actual code
    # Code that may raise an exception
except ExceptionType:  # type: ignore
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



"""Exercise:
 Write a Python program that takes a numeric grade from the user (between 0 and 100), and prints the corresponding letter grade:
90-100 → A  
80-89  → B  
70-79  → C  
60-69  → D  
<60    → F
Your program should handle the following exceptions:

If the user enters a non-numeric value, catch the ValueError and display a user-friendly message.
If the user enters a number outside the valid range (0 to 100), raise a ValueError yourself with a custom message.

Use the try-except-else-finally structure:

try: Attempt to parse the input and compute the letter grade.
except: Handle conversion errors and invalid ranges.
else: Print the final grade if everything was successful.
finally: Print a goodbye message like "Thank you for using the Grade Calculator. Goodbye!" no matter what. """

# Solution

try: 
    val = input("Enter your marks: ")
except ValueError as ve:
    print("You DUMB! You were supposed to enter your marks, i wont be surprised if you fail")
else:
    if 0< val > 100:
        print("WOW! Looks like your'e dreaming")
    else :
        if val > 90:
            print("A")
        elif 80 < val < 90 :
            print("B")
        elif 70 < val < 80 :
            print("C")
        elif 60 < val < 70 :
            print("D")
        else :
            print("F")
finally:
    print("Thanks for using the grade calculator")