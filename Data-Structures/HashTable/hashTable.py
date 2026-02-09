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
    

    # The below fucntions do not handle collison, first understand the below code then moveon.
    # We have to modify the same functions to handle collison 
    """    
    def setItem(self, key, value):
        h = self.getHash(key)     
        self.arr[h] = (key, value)
    
    def getItem(self, key):
        h = self.getHash(key)
        return self.arr[h] 
    """

    # We will implement linear probing to Handle Collision, look at different collision handling techniques 
    
    def setItem(self, key, value):
        h = self.getHash(key) 
        if self.arr[h] == None or self.arr[h][0] == key:
            self.arr[h] = (key, value)
        else: # Linear Probing - search for the next bucket below, if at last index go to first
            full_counter = 0 # We will use this to flag if the array does not have any remaining space
            while True:
                if h ==self.Max-1:
                
                    if full_counter > 1: # If we have iterated through the loop twice
                        raise Exception("The Underlying array in full !")
                    full_counter+=1
                
                    h=0 # If we reached end of array we will start from begining
                else:
                    h+=1
                    
                if self.arr[h] == None or self.arr[h][0] == key:
                    self.arr[h] = (key, value)
                    break
                 
    def getItem(self, key):
        h = self.getHash(key)
        
        if self.arr[h][0] == key:
            return self.arr[h]
        else:
            full_counter = 0
            while True:
                if h == self.Max-1:
                    if full_counter > 1:
                        print("Key does not Exist!")
                        return
                    full_counter+=1                
                    
                    h = 0
                else:
                    h+=1
                
                if self.arr[h][0] == key:
                    return self.arr[h]    
            
    
    
ht = HashTable()

for _ in range(100):
    ht.setItem(str("saad"),69) 

# ht.setItem(str("saad"),69) 
print(ht.arr)