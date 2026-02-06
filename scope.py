# Scope of Variables
'''
In Python, the scope of a variable is determined by where it is defined. 
Variables defined inside a function are local to that function.
While variables defined outside of any function are global.
'''

global_var = "I am global"
def my_function():
    local_var = "I am local"
    print(global_var)  # This will work

print(local_var)   # This will raise an error because local_var is not defined in this scope

