# Modules

#  Modules are a prewritten code for specific tasks. They are used to save time and effort.
#  To use a module, you need to import it first. You can import a module using the import statement.
#  Some modules are built-in, while others can be installed using pip.

#  To import a module, you can use the following syntax:
#  import module_name

import math # Importing the math module, it has many functions for mathematical operations.

print(dir(math)) # This will show all the functions and variables available in the math module.

# A better way to familiarize yourself with a module is to look up the documentation on the internet.

math.sqrt(16) # This will return the square root of 16, which is 4.0
math.pi # This will return the value of pi, which is approximately 3.14159
math.sin(math.pi/2) # This will return the sine of pi/2, which is 1.0
math.cos(0) # This will return the cosine of 0, which is 1.0
math.tan(math.pi/4) # This will return the tangent of pi/4, which is 1.0
# and many more...

# One other module is calendar, which has functions related to calendars and dates.
import calendar
print(calendar.month(2024, 6)) # This will print the calendar for June 2024.

print(calendar.isleap(2024)) # This will return True, because 2024 is a leap year.




# There are many other modules available in Python, chance are you will find a module for almost any task you want to perform. 

# You can also create your own modules using the following steps:
# 1. Create a new Python file and write your code in it.
# 2. Save the file with a .py extension.
# 3. Import the module in another Python file using the import statement.
        # if the module is in the same directory, you can simply use import module_name
        # if the module is in a different directory, you can use import sys and sys.path.append('path_to_module_directory') to add the directory to the system path, and then import the module.
# 4. Use the functions and variables defined in the module as needed.


