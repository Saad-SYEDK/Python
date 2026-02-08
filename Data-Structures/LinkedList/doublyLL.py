'''
    The only difference in doubly linked list is that it contains an extra pointer which points to
    the previous node, this requires us to make some changed in all of our methods of singly linked list
    to handle the prev pointer.
    No need to code for write all the methods from scratch, just implement basic mehtods like insertion and deletion
    and you will be good to go.
'''
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
    
    def delete_end(self):
        # We have maintained a tail pointer, which makes our work very simple, we just upatae the node at tail pointer
        
        # If the list is empty, return
        if self.head is None:
            return
        
        # If the list has only one node, update both pointers
        if self.head == self.tail:
            self.head = self.tail = None
            return
        
        # In all the other cases we just move the tail pointer to the previous node and update its next pointer to None.
        self.tail = self.tail.prev
        self.tail.next = None
        return
    
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

list.delete_end()
list.delete_end()
list.delete_end()
list.display()