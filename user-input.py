# We can take input from the user using the input() function.
user_input = input("Please enter something: ")
print("You entered:", user_input)

# The input() function always returns a string. 


# If you want to convert it to another type, you can use the appropriate type conversion functions.
age = input("Please enter your age: ")
age = int(age)  # Convert the input to an integer
print("Your age is:", age)

# You can also use the input() function to get multiple values at once by splitting the input string.
name, city = input("Please enter your name and city (separated by a space): ").split()
print("Your name is:", name)
print("Your city is:", city)
# You can also specify a different separator for splitting the input.
name, city = input("Please enter your name and city (separated by a comma): ").split(",")
print("Your name is:", name.strip())
print("Your city is:", city.strip())