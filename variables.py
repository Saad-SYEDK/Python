# Variables are like a container to store data values.
# In Python, we do not need to declare the data type of variable.

# num is a variable
num = 200
# To print the value of variable, we use print() function.
print(num) # Output: 200 

# We can also change the value of variable.
num = 300 
print(num) # Output: 300

# We can store different data types in variables.
name = "Saad" # String data type    
age = 20       # Integer data type
height = 5.9   # Float data type
is_student = True # Boolean data type

# We can check the data type of variable using type() function.
print(type(name))       # Output: <class 'str'>
print(type(age))        # Output: <class 'int'>
print(type(height))    # Output: <class 'float'>
print(type(is_student)) # Output: <class 'bool'>


# Algebraic Operations with Variables
a = 10  
b = 5
sum_result = a + b          # Addition
diff_result = a - b         # Subtraction
prod_result = a * b         # Multiplication
quot_result = a / b         # Division
mod_result = a % b          # Modulus
exp_result = a ** b         # Exponentiation


"""Exercise - Variables
1. Create a variable called break and assign it a value 5. See what happens and find out the reason behind the behavior that you see.

2. Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables

3. Store your first, middle and last name in three different variables and then print your full name using these variables

4. Answer which of these are invalid variable names: _nation, 1record, record1, record_one record-one, record^one, continue .
"""

# Solution
# 1. The variable name 'break' is a reserved keyword, and it cannot be used as a variable name. If you try to assign a value to 'break', you will get a SyntaxError.

# 2.
birth_year = 2000
current_year = 2024
age = current_year - birth_year
print(age) # Output: 24

# 3.
first_name = "Saad" 
middle_name = "Syed"
last_name = "Kaleemulla"
full_name = first_name + " " + middle_name + " " + last_name
print(full_name) # Output: Saad Syed Kaleemulla

# 4. Invalid variable names: 1record, record-one, record^one, continue (because 'continue' is a reserved keyword in Python)

"""Exercise - Numbers
1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
4. Print binary representation of number 17
"""

# Solution
# 1.
length = 92
width = 48.8
area = length * width
print("Area of football field:", area, "square meters")

# 2.
packets = 9
cost_per_packet = 1.49
total_cost = packets * cost_per_packet
amount_given = 20
change = amount_given - total_cost
print("Change to be given back:", change, "dollars")

# 3.
side_length = 5.5
area_of_bathroom = side_length ** 2
cost_per_square_feet = 500
total_cost = area_of_bathroom * cost_per_square_feet
print("Total cost to replace tiles:", total_cost, "rupees")

# 4.
number = 17
binary_representation = bin(number)
print("Binary representation of", number, "is", binary_representation)