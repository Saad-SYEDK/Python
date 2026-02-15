# Sets are UNORDERED collection of UNIQUE elements.
# Sets are MUTABLE, but the elements contained in the set must be IMMUTABLE.
# Sets are defined using curly braces {} or the set() constructor.
# Example:
my_set = {1, 2, 3, 4, 5}

# Sets do not allow duplicate elements, if we try to add a duplicate element, it will be ignored.
my_set.add(5)

# Sets are unordered, which means that the elements in a set do not have a specific order.
# Therefore, We cannot access them using an index like in lists or tuples.


# We can check if an element is in a set using the 'in' keyword.
if 3 in my_set:
    pass

# Note
ss = {} # is an empty dictionary, not a set
print(type(ss))

#We have to add at least one element to create a set using curly braces, otherwise it will be considered as an empty dictionary.
ss = {1} # This is how we create a set with one element
# or 
ss = set() # This is how we create an empty set


