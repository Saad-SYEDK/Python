# Dictionary in Python

# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# Dictionaries are defined using curly braces {} and key-value pairs are separated by commas. The key and value are separated by a colon :.
# They are unordered, mutable, and indexed. You can use any immutable data type as a key (like strings, numbers, tuples) and any data type as a value (like strings, numbers, lists, other dictionaries).

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Accessing values in a dictionary
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York

# Adding a new key-value pair to the dictionary
my_dict["country"] = "USA"

# Updating an existing key-value pair
my_dict["age"] = 31

# Removing a key-value pair from the dictionary
del my_dict["city"]

# Iterating through a dictionary
for key in my_dict:
    print(key, ":", my_dict[key])

# You can also use the items() method to iterate through key-value pairs
for key, value in my_dict.items():
    print(key, ":", value)
    
# Deleting the entire dictionary
del my_dict 

# We can also use the clear() method to remove all items from the dictionary without deleting it entirely.
my_dict.clear()
