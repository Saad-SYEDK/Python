class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.array = [[] for i in range(self.MAX)]
    
    def __hash_function(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        
        return hash % 100
    
    def __setitem__(self, key, value):
        hash = self.__hash_function(key)
        for 
    
    def __getitem__(self, key):
        hash = self.__hash_function(key)
        return self.array[hash]

    def __delitem__(self, key):
        hash = self.__hash_function(key)
        self.array[hash] = None

#testing hash table
table = HashTable()

table["saad"] = 7
table["saad"] = 8

print(table["saad"])
