# Loops in Python
# Loops are used to execute a block of code repeatedly.
# The two main types of loops in Python are:
# - for loops
# - while loops

# Here's an example of a for loop in Python:
for i in range(5): # This will iterate from 0 to 4 (5 is excluded)
                   # We can also specify a start value like range(2, 5) which will iterate from 2 to 4
    print("Iteration:", i)

# Here's an example of a while loop in Python:
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# You can also use loops to iterate over lists:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)


# Nested loops are also possible:
for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)


# Remember! avoid infinite loops with loops by ensuring the condition will eventually be false.

# We also have break and continue statements can also be used to control loop execution.
# - break: exits the loop entirely
# - continue: skips the current iteration and moves to the next one
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print("Break Example - i:", i)
for i in range(5):
    if i == 3:
        continue  # Skip the iteration when i is 3
    print("Continue Example - i:", i)