class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class CLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, data):
        node = Node(data, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self.tail.next = self.head 
    
    def append(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
        if self.tail is None:
            self.tail = node
        else:
            self.tail.next = node
        self.tail = node
        self.tail.next = self.head
    
    def display(self):
        if self.head is None:
            print("Empty List!")
            return
        current = self.head
        while True:
            print(current.data, end="->")
            if current == self.tail:
                print()
                return
            current = current.next
    

# Checking
list = CLL()
list.append(1)
list.append(2)

list.prepend(0)

list.display()