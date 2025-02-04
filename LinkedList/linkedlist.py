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
        pass