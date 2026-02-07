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
    
    
    
"""Exercise: loops
1. After flipping a coin 10 times you got this result,
    result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
    Using for loop figure out how many times you got heads

2. Print square of all numbers between 1 to 10 except even numbers

3. Your monthly expense list (from Jan to May) looks like this,
    expense_list = [2340, 2500, 2100, 3100, 2980]
    Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
    If expense is not found then it should print that as well.

4. Lets say you are running a 5 km race. Write a program that,
    Upon completing each 1 km asks you "are you tired?"
    If you reply "yes" then it should break and print "you didn't finish the race"
    If you reply "no" then it should continue and ask "are you tired" on every km
    If you finish all 5 km then it should print congratulations message

5. Write a program that prints following shape
    *
    **
    ***
    ****
    *****

"""

# Solutions

#1. 
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count_head = 0
for i in result:
    if i == "heads":
        count_head+=1
print(count_head)

#2.
square = lambda x : x*x
is_even = lambda x : x % 2 == 0 
for i in range(11):
    if not is_even(i):
        print(square(i))
        # or
for i in range(11):
    if i % 2 != 0:
        print(i * i)

# 3.
expense_list = [2340, 2500, 2100, 3100, 2980]
n = int(input("Enter expense to check:"))
if n in expense_list:
    for i in range(len(expense_list)):
        if expense_list[i] == n :
            print("Expense found in month", i+1)
else:
    print("Expense not found")

# 4.
Race_length_kms = 5
while Race_length_kms > 1:
    Race_length_kms -= 1
    ip = input("Are you tired? ")
    if ip == "yes":
        print("You didn't finish the race")
        break
    else:
        continue
if Race_length_kms == 1:
    print("You finished the race")
    
# 5.
for i in range(5):
    for j in range(i):
        print("*",sep="")
    print()