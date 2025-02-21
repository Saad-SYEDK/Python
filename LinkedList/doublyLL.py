class Node:
    def __init__(self, prev, data, next):
        self.prev = prev
        self.data = data
        self.next = next

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def prepend(self, data):
        # When inserting at the beginning, the prev will always be None
        node = Node(None, data, self.head)
        # if the list is not empty, we need to upate the existing prev pointer
        if self.head:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node
    
    def append(self, data):
        node = Node(self.tail, data, None)
        # if the list is not empty, we need to upate the existing next pointer
        if self.tail:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node
    
    def display(self):
        if self.head is None:
            print("Empty List!")
            return
        current = self.head
        print("<-->", end="")
        while current:
            print(current.data, end="")
            print("<-->", end="")
            current = current.next
        
# Checking
list = DLL()
list.append(1)
list.prepend(0)
list.append(2)
list.display()