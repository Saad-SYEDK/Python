# If else statements are used for conditional execution of code blocks based on whether a condition is true or false.

# Here's an example of how to use if-else statements in Python:

age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# You can also use elif (else if) to check multiple conditions:
age = 20
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# You can nest if-else statements as well:
score = 85
if score >= 90:
    print("Grade: A")
else:
    if score >= 80:
        print("Grade: B")
    else:
        print("Grade: C")
