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


# If we want to create a immotable set, we can use the frozenset() constructor.
my_frozenset = frozenset([1, 2, 3, 4, 5])
# my_frozenset.add(6) # This will raise an error because frozensets are immutable


# Sets operations:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# union - returns a set that contains all the elements from both sets, without duplicates.
set3 = set1.union(set2) # or set3 = set1 | set2 (or)

# intersection - returns a set that contains all the elements that are common to both sets.
set4 = set1.intersection(set2) # or set4 = set1 & set2 (and)

# difference
set5 = set1.difference(set2) # or set5 = set1 - set2 (minus)    

#  symmetric difference - returns a set that contains all the elements that are in either set1 or set2, but not in both.
set6 = set1.symmetric_difference(set2) # or set6 = set1 ^ set2 (xor)


# Look at the set methods for more operations like issubset(), issuperset(), isdisjoint(), etc. 

"""
Exercise: Sets and Frozen Sets
create any set anf try to use frozenset(setname)

Find the elements in a given set that are not in another set
Example:
    set1 = {1,2,3,4,5}
    set2 = {4,5,6,7,8}

    ans:  {1,2,3}
"""