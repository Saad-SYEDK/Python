# Generators

# A generator is a type of iterator that allows you to create an iterable sequence of values on the fly,
    # without having to store them all in memory at once.
# This can be very useful when working with large datasets or when you want to generate an infinite sequence of values.

# We use the yield keyword to create a generator function.
# When the generator function is called, it returns a generator object that can be iterated over.
def my_generator():
    yield 1
    yield 2
    yield 3

my_gen = my_generator()
print(my_gen) 
for i in my_gen:
    print(i)

print()
# or 
for i in my_generator():
    print(i)
# The yield keyword is used to produce a value and pause the execution of the generator function until the next value is requested.

print()
# We can also use a generator expression, which is similar to a list comprehension but uses parentheses instead of square brackets.
squares = (x**2 for x in range(10))
for square in squares:
    print(square)
    

# Generators are memory efficient because they only generate one value at a time.

print()
# They can be used to create infinite sequences of values.
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
    print(i)
    if i >= 10: # TO avoid infinite loop
        break