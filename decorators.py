# Decorators are wrapper funcctions used to modify other functions behaivior.

# let us understand the concept of decorators with an exercise.
'''
Exercise: Decorators
Create a decorator function to check that the argument passed to the function factorial is a non-negative integer:

Create a factorial function which finds the factorial of a number.

Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.

example: 

    factorial(1.354) : raise Exception or print error message
    factorial(-1) : raise Exception or print error message
    factorial(5) : 60
    
'''

# Let us create a wrapper function that takes our factorial function as argument
def check_positive(func):
    def wrapper(*args, **kwargs):
        n = args[0] if args else kwargs.get('n')
        
        if not isinstance(n, int) or n < 0:
            raise ValueError("Input must be a non-negative integer.")
        return func(n)
    return wrapper
    # Now if we have 10 different functions like fibocacci, power, etc, that require positve integers.
    # We can this decorator to all without writing the same code again and again. 
        

# THis is our factorial fucntion
@check_positive
def factorial(n):
    if n == 0 or n==1:
        return 1

    result = 1
    while n > 1:
        result *= n
        n -= 1
    
    return result


print(factorial(65))