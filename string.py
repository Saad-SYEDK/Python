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

