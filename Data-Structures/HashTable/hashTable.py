# Hash Tables

# A Hash Table stores key-value pairs.
# It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.
# It all0ws for fast data retrieval, as the average time complexity for search, insert, and delete operations is O(1).
# In python, the built-in dictionary data type is implemented as a hash table.

# However, we will manually implemnent a hash table with arrays to understand the underlying mechanics.


class HashTable:
    def __init__(self):
        self.Max = 100 # size of array
        self.arr = [None for _ in range(self.Max)]

    # THe magic of Hash Table is in its Hash Funciton- a takes any value and returns a hash value.
    # THe Logic can be any thing, but it guarentees that it will return the same hash value for a same input
    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char) # our logic is to add ascii value of each charactor and modulo
        return h % self.Max # we do this to ensure that our values lies within the array index
    
    
    def setItem(self, key, value):
        h = self.getHash(key)
        
        self.arr[h] = (key, value)
    
    def getItem(self, key):
        h = self.getHash(key)
        
        return self.arr[h]

ht = HashTable()
ht.setItem("Name", "saad")

print(ht.getItem("Name"))