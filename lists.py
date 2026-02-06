#LIST

# Imagine you are going to a grocery store and you need to buy some items. You can create a list of items you need to buy.
grocery_list = ["milk", "eggs", "bread", "butter"]

# We can access items in the list using their index. Remember that indexing starts at 0.
print(grocery_list[0])  # Output: milk

# We can also add items to the list using the append() method.
grocery_list.append("cheese")

# We can remove items from the list using the remove() method.
grocery_list.remove("eggs")

# We can change items in the list by assigning a new value to a specific index.
grocery_list[1] = "orange juice"
# Remember! We cannot do this with a string because strings are immutable, meaning they cannot be changed after they are created.


# we can inset items at a specific index using the insert() method.
grocery_list.insert(1, "yogurt")

# We can also find the length of the list using the len() function.
print(len(grocery_list))  # Output: 5

# We can concatenate two lists using the + operator.
fruits = ["apple", "banana", "orange"]
combined_list = grocery_list + fruits

# There are many other methods and operations we can perform on lists, such as sorting, slicing, and more. Lists are a fundamental data structure in Python and are very versatile for storing and manipulating collections of items.l