# LinkedList is a linear datastructure that stores elements in a non-contigious fashion.
# Array stores data in contigious, this makes insertion and deletion of elements difficult as we have to shift all the elements forward/backward.
#  
class Node:
    def __init__(self, data , next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Prepend - insert at the beginning of the list
    def prepend(self, data): 
        node = Node(data, self.head)
        # Just create a new node and update the head.
        self.head = node
    # Append - Insert at the end of the list
    def append(self, data):
        node = Node(data, None)
        # We have 2 cases:
        # Case 1 : if it is a empty list then we have to initialize head pointer
        if not self.head:
            self.head = node
            return
        # Case 2 : if there are existing nodes then we have to itrerate till the last node and update its next pointer to our new node.
        current = self.head # iterator named current
        while current.next: # While we reach the last node i.e a node whose next pointer is None
            current = current.next 
        current.next = node # update the last node's next pointer.
    
    # Insert at a given index
    def insert_at(self, index, data):
        # If the given index is 0 we have to prepend.
        if index == 0:
            self.prepend(data)
            return
        # Else we iterate till we reach one node before the index and update its next pointer
        current = self.head
        while index > 1:
            current = current.next
            index -= 1
        node = Node(data, current.next)
        current.next = node
    
    # insert after a given value, if there are multiple values we will insert after the first one.
    def insert_after(self, value, data):
        # If the list is empty return
        if self.head is None:
            print("Value not found: Empty list!")
            return
        
        # Itereate till we find the node containing the value
        current = self.head
        while current:
            if current.data == value:
                node = Node(data, current.next)
                current.next = node
                return
            current = current.next
        # If we iterated through the whole list and are not able to find the value, return 
        print("Value not found: Reached end of list!")
    
    # Delete a node which contains the value, if there are multiple nodes with the same value, delete the first one
    def delete_node(self, value):
        # if the list is empty return
        if self.head is None:
            print("Empty List!")
            return
        # if the value is present in the head node, we have to update the head pointer
        elif self.head.data == value:
            self.head = self.head.next
            return
        
        current = self.head
        # We need to stop at a node before the node containing the value inorder to delete that node
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next        
        # If we reach the end without finding the value, return
        print("Value does not exists")
    
    
    def display(self):
        # If there are no elements in the list.
        if self.head is None:
            print("List Empty!")
            return

        current = self.head # Iterator
        while current: # Till we reach null
            print(current.data, end="")
            print("->", end="")
            current = current.next
        print("NULL")
    

# Testing the LinkedList
ll = LinkedList() 

ll.append(1)
ll.append(2)
ll.append(4)

ll.insert_at(2, 3)

ll.prepend(0)
ll.display()


ll.insert_after(4, 5)
ll.display()


ll.delete_node(3)
ll.display()

        