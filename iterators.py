# We have been using loops in this way,
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)
    
# Here i is an iterator, in other programming languages like c or java, we manually access each element using index.
# But in python we have an iterator method that gives us the next element in the list, and we can use it in a for loop to iterate through the list.

print(dir(a))
# We can see that there is an __iter__ method in the list, which is used to create an iterator object for the list.

# List, tuple, set, string, files, dictionaries, are all iterable objects in python, which means they have an __iter__ method that returns an iterator object.

# We can also create our own iterable objects by defining a class and implementing the __iter__ method.

class MyIterable:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]
        self.index = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]


my_iterable = MyIterable()
for i in my_iterable:
    print(i)    
# This is how the for loop works in python, it calls the __iter__ method to get an iterator object, and then calls the __next__ method to get the next element until it raises a StopIteration exception.

# Self Learning: find out more about iterators, check out the reverse() how is it implemented.

    
