# Tuples
# A tuple is an ordered, immutable collection of items. Tuples are defined using parentheses () and can contain elements of different data types. Once a tuple is created, its contents cannot be changed.

# Here's an example of a tuple in Python:
my_tuple = (1, "Hello", 3.14, True)
print(my_tuple)  # Output: (1, 'Hello', 3.14, True)
# You can access elements in a tuple using indexing, just like with lists:
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: Hello

# Differences between lists and tuples:
# 1. Mutability: Lists are mutable, meaning you can change their contents (add, remove, or modify elements). Tuples are immutable, so once they are created, you cannot change their contents.
# 2. Syntax: Lists are defined using square brackets [], while tuples are defined using parentheses
# 3. Performance: Tuples can be more memory-efficient and faster than lists, especially when dealing with large collections of data, because they are immutable and can be optimized by the Python interpreter.
# 4. Use Cases: Tuples are often used for fixed collections of items, such as coordinates (x, y) or RGB color values (r, g, b). Lists are more suitable for collections of items that may need to be modified, such as a list of tasks or a list of user inputs.

#  You can also use tuples to return multiple values from a function:
def get_person_info():
    name = "Alice"
    age = 30
    return (name, age)

info = get_person_info()
print(info)  # Output: ('Alice', 30)