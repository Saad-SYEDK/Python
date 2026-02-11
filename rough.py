class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class linkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_start(self, data):
        self.head = node(data, self.head)
        
    def insert_at_end(self, data):
        if self.head:
            i = self.head
            
            while i.next:
                i = i.next
            
            i.next = node(data)
        else:
            self.head = node(data, self.head)
    
    def del_start(self):
        if self.head:
            self.head = self.head.next
        else:
            print("List Empty!")
    
    
    def display_list(self):
        i = self.head
        while i:
            print(i.data, "--> ", end="")
            i=i.next
        print("NULL")


# ll = linkedList()

# ll.insert_at_end(0)

# ll.del_start()

# ll.display_list()

print(-1 % 3)