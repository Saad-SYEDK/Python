# Comprensions are a concise way to create lists, dictionaries and sets and  in Python.
# 
# They allow you to generate new collections by applying an expression to each item in an iterable, optionally filtering items using a condition.

# Example


numbers = [1, 2, 3, 4, 5, 6]

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



