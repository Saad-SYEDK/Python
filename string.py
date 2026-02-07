# Strings 
text = "Hello, World!"
print(text)  # Output: Hello, World!

# We can access individual characters in a string using indexing starting from 0
first_char = text[0]
print(first_char)  # Output: H

# We can also use negative indexing to access characters from the end
last_char = text[-1]
print(last_char)  # Output: !
# Strings are immutable, which means we cannot change them after they are created
# We can change the whole string, but not individual characters
# text[0] = 'h'  # This will raise a TypeError: 'str' object does not support item assignment


# However, we can create a new string by concatenating existing strings
new_text = text + " How are you?"
print(new_text)  # Output: Hello, World! How are you?

#SUBSTRINGS
# We can also acess a substring using slicing
substring = text[0:5]  # This will get characters from index 0 to 4 (0 is inclusive, 4 is exclusive)
print(substring)  # Output: Hello

# if we omit the start index, it defaults to 0
substring_from_start = text[:5] # output: Hello

# if we omit the end index, it defaults to the length of the string
substring_to_end = text[7:] # output: World!

#Multiline Strings
# We can create multiline strings using triple quotes (''' or """)
multiline_text = """This is a string that spans
multiple lines.
Name: John Doe
Age: 30"""
print(multiline_text)
# Output:   This is a string that spans
#           multiple lines.
#           Name: John Doe
#           Age: 30

#interger to string
age = 30
age_str = str(age) # Convert integer to string

'''Exercise - Strings
1. Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
2. Create a variable to store the string "Earth revolves around the sun"
3. Print "revolves" using slice operator
4. Print "sun" using negative index
5. Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
6. I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.'''

#Solution
#1.
street = "123 Main St"
city = "New York"
country = "USA"
# Using + operator
address = street + "\n" + city + "\n" + country
print(address)
# Using f-string
print(f"The address is {street}\n{city}\n{country}")
# or
address_f = f"{street}\n{city}\n{country}"
print(address_f)

#2.
sentence = "Earth revolves around the sun"
print(sentence[6:14])  # Output: revolves
print(sentence[-3:])  # Output: sun

#3.
x = 5  # number of fruits
y = 3  # number of vegetables
print(f"I eat {y} veggies and {x} fruits daily")  # Output: I eat 3 veggies and 5 fruits daily

#4.
s = 'maine 200 banana khaye'
new_s = s.replace("200", "10").replace("banana", "samosa")
print(new_s)  # Output: maine 10 samosa khaye


