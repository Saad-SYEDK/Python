# Comprensions are a concise way to create lists, dictionaries and sets and  in Python.
# 
# They allow you to generate new collections by applying an expression to each item in an iterable, optionally filtering items using a condition.

# Example


numbers = [1, 2, 3, 4, 5, 6, 8, 10, 2, 6]

# without list comprehesion
even = []
for i in numbers:
    if i%2 == 0:
        even.append(i)
        
print(even)

# using list comprehensions
even = [i for i in numbers if i%2 == 0]
print(even)

# or even better (The logic is upto you) 
odd = [i for i in range(10) if i%2 != 0]

# for squares
squares = [i * i for i in range(10)]




##############################################################################
#  Set Comprehension
######################################################################
## Same as above for SETS COMPREHENSION - We only use {} brackets instead of []
# Example:
num = [1, 2, 3, 4,2, 4, 5,  5, 6, 6, 7, 6]
# lets take even set of this list
even_set = {i for i in num if i%2 == 0}
print(even_set)




############################################
# Dictionary Comprehension
###########################################

city = ["Delhi", "Dubai", "New York"]
Country = ["India", "UAE", "USA"]

z = zip(Country, city) # This creates a zip object, which we can itereate through
print(z)
for i in z:
    print(i)
    
# Dict comprehension
dictionary = {co:ci for co,ci in zip(Country, city)}
print(dictionary)


#####################
#Comprehension is a very powerful feature, the litmit is the sky, we can use complex logic to create required list without having to write tones of code