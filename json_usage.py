# JSON

# JSON (JavaScript Object Notation) is a lightweight data-interchange format.
# It is easy for humans to read and write, and easy for machines to parse and generate.
# It is commonly used for transmitting data in web applications.

# Let us see how this works

phone_book = {} # We are creating a dictionary to represent a book

phone_book['jon'] = {
    'name': 'jon',
    'phone': '123-456-7890',
    'address': '123 Main Street'
}
phone_book['sarah'] = {
    'name': 'sarah',
    'phone': '987-654-3210',
    'address': '456 Elm Street'
}
# We have created a phone book with two entries: Jon and Sarah.
# Now we want to save this phone book to a file in JSON format.
import json
s = json.dumps(phone_book) #dumps stands for "dump string" 
# This will convert the our phone book dictionary to a string, and we store it in 's'

# Now we can write this string to a file
with open('phone_book.txt', 'w') as f:
    f.write(s)
    # This will create a file called 'phone_book.txt' and write the string to it.

# Now let us read the file back and convert it back to a dictionary
with open('phone_book.txt', 'r') as f:
    new_s = f.read() # This will read the contents of the file and store it in 'new_s'

new_phone_book = json.loads(new_s) # This will convert the string back to a dictionary
print(new_phone_book) # This will print the new phone book dictionary


# This is how we use JSON for data exchange between different applications.