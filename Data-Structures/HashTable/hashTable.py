# Hash Tables

# A Hash Table stores key-value pairs.
# It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.
# It all0ws for fast data retrieval, as the average time complexity for search, insert, and delete operations is O(1).
# In python, the built-in dictionary data type is implemented as a hash table.

# However, we will manually implemnent a hash table with arrays to understand the underlying mechanics.


class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [None for _ in range(self.Max)]
        self.count = 0 # required to check the avilability of buckets in closed hashing(liner probing, quad probing, etc)

    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char) # we will be using ascii value to generate hash value, we can use any logic
        return h % self.Max

    def setItem(self, key, value):
        if self.count >= self.Max:
            raise Exception("Hash Table is full")
    
        h = self.getHash(key)
        while self.arr[h] is not None and self.arr[h] != "DELETED":
            if self.arr[h][0] == key: # Update existing key
                break
            h = (h + 1) % self.Max #Resets h to 0 if it gets larger than max
        
        if self.arr[h] is None or self.arr[h] == "DELETED":
            self.count += 1
        self.arr[h] = (key, value)

    def getItem(self, key):
        h = self.getHash(key)
        start_h = h # To know if we have iterated thorugh all the buckets in the array
        while self.arr[h] is not None:
            if self.arr[h] != "DELETED" and self.arr[h][0] == key:
                return self.arr[h][1]
            h = (h + 1) % self.Max
            if h == start_h: # Cycled back to start
                break
        return None

    def removeItem(self, key):
        h = self.getHash(key)
        start_h = h
        while self.arr[h] is not None:
            if self.arr[h] != "DELETED" and self.arr[h][0] == key:
                self.arr[h] = "DELETED"
                self.count -= 1
                return True
            h = (h + 1) % self.Max
            if h == start_h:
                break
        return False
"""Exercise:
Implement hash table where you handle collision with other techniques like seprate chaining or quadratic probing.
"""
