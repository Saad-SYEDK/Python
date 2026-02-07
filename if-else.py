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

"""Exercise: Condition
Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
1.Write a program that asks user to enter a city name and it should tell which country the city belongs to
2. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
3. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
    Ask user to enter his fasting sugar level
    If it is below 80 to 100 range then print that sugar is low
    If it is above 100 then print that it is high otherwise print that it is normal"""
    
# Solution:
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# 1. 
city = input("Enter City name:")
if city in india:
    print("india")
elif city in pakistan:
    print("Pakistan")
elif city in bangladesh:
    print("bangladesh")
else:
    print("CIty not in list")
    
# 2. 
c1 = input("Enter city 1")
c2 = input("Enter city 2")

if c1 and c2 in india:
    print("Both in india")
elif c1 and c2 in pakistan:
    print("Both in Pakistan")
elif c1 and c2 in bangladesh:
    print("Both in bangladesh")
else:
    print("Both are not in same country")
    
#3 
sugar = int(input("Enter fasting sugar level:"))
if sugar < 80:
    print("Low sugar")
elif sugar > 100:
    print("High Sugar")
else:
    print("Normal Sugar")