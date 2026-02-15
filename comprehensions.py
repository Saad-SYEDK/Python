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

"""Exercise: List Set Dict Comprehensions
Create a Dictionary which contains the Binary values mapping with numbers found in the below integer and binary and save it in binary_dict.
Example :
    integer = [0, 1, 2, 3, 4]
    binary = ["0", "1", "10", "11", "100"]
    binary_dict = {0:"0", 1:"1", 2:"10", 3: "11", 4:"100"}



Create a List which contains additive inverse of a given integer list. An additive inverse a for an integer i is a number such that:
a + i = 0
Example:
integer = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-1, 1, -2, -3, -5, 0, 7]



Create a set which only contains unique sqaures from a given a integer list.
integer = [1, -1, 2, -2, 3, -3]
sq_set = {1, 4, 9}
"""