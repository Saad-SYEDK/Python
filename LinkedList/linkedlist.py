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
    
    # Delete a node at a givin indez
    def delete_at_position(self, index):
        # IF the list is empty return
        if self.head is None:
            print("Empty List!")
            return
        # If the index is first node, update head 
        elif index == 0:
            self.head = self.head.next
            return
        
        current = self.head
        # Iterate till we reach one node before the node we have to delete
        while current.next:
            if index == 1:
                current.next = current.next.next
                return
            index -=1
            current = current.next
        # if we reach the end before reaching the index, return
        print("Indext out of range!")
    
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
    
    # Return the length of list 
    def get_length(self) -> int:
        # If the list is empty, print 0 and return
        if self.head is None:
            return 0
        
        counter = 0 # To keep the count of the nodes
        current = self.head # to itereate through the nodes
        # While there are nodes in the list
        while current:
            counter += 1
            current = current.next
        return counter
    
    # Find an index of a given data and return it, else -1 
    def find(self, data) -> int:
        # If the list is empty, return -1 
        if self.head is None:
            return -1
        
        counter = 0
        current = self.head
        while current:
            if current.data == data:
                return counter
            current = current.next
            counter += 1
        # If we reach the end without finding the data, return -1
        return -1

# Advanced Mehods:
    # reverse, sort, remove_duplicates, has_cycle, find middle, merge_sorted, nth from end
# Try to implement this method wihtout watching the code, do some research to understand what these methods are supposed to do and implement them
    
    # Reverse the order of the given linked list, change the links/next pointers and update the head to the last node 
    def reverse(self):
        # If the list is empty, return
        if self.head is None:
            return
        
        current = self.head
        # If the list has only one node, no need to do anything
        if current.next is None:
            return
        # Logic - we will itereate through every node and update their next pointer to point to the previous pointer.
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    # Given a linked list remove all the nodes which contains data that already exists
    def remove_duplicates(self):
        if self.head is None:
            return
        # In order to keep the information about data which we already have, we will make a dictionary which will have keys as the data, if a data key already exists in the dictionary we will delete that node.
        seen = {}
        current = self.head
        seen[current.data] = 1
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen[current.next.data] = 1
                current = current.next
    
    # If the list contains cycle i.e if any node is connected to a node before it, the list contains a loop/cycle and will be any infinite loop. If the list contains cycle, return true else false 
    def contains_cycle(self) -> bool:
        # Floyd's cycle detection or Tortoise and Hare Algorithm
        # if the list is empty or there is only single node. Return False
        if self.head is None or self.head.next is None:
            return False
        
        # Initialize two pointers at head
        slow = fast = self.head
        while fast and fast.next:
            # Slow pointer moves 1 step at a time
            slow = slow.next
            # Fast pointer moves 2 steps at a time
            fast = fast.next.next
            
            # If the two pointers end up in the same node it means there is a cyclee
            if slow == fast:
                return True
        # If we reach the end of the list, it means there is no cycle hence return False 
        return False
    
    # Return the middle index of the list
    def find_middle(self) -> int:
        # If the list is empty return -1
        if self.head is None:
            return -1
        
        # Two pointers starting at head
        slow = fast = self.head
        counter = 0
        
        while fast and fast.next:
        # Slow pointer moves one step while the fast pointer moves two steps at a time
            slow = slow.next
            fast = fast.next.next
            counter += 1
        # Logic - when the fast pointer reaches the end, the slow pointer will be at the middle
        # There is no need for slow pointer if we want to return the index, but if we want to return the middle node, we can return the slow pointer
        return counter
    
    # Given two sorted lists, merge both
    def merge_sorted(self, given_list):
        # Works only if both lists are sorted, better if you add a logic to check if both lists are sorted
        
        # Note : we use given_list to access the second list
        #        "self" will be used to access the first list 
        
        # If anyone of the list is empty, we return the other list.
        # Works correctly even if both lists are empty, None will be returned
        if self.head is None:
            return given_list.head
        elif given_list.head is None:
            return self.head

        # We find need to create a head pointer for the new list. 
        new_head = None
        
        # iterators for each lists
        list1 = None
        list2 = None
        
        # The smallest node should be the head.
        # Once we select which list should be the head, we shall move its iterator to the next node
        if self.head.data > given_list.head.data:
            new_head = given_list.head
            list2 = given_list.head.next 
            list1 = self.head
        else:
            new_head = self.head
            list1 = self.head.next
            list2 = given_list.head
        
        # Iterator for new list
        current = new_head
        
        # Basic merge_sort logic - while both the list have elements, compare and select the smaller node.
        # Once any one of the list is iterated, connect the rest with the remaining list
        while list1 and list2:
            if  list1.data > list2.data:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        if list1:
            current.next = list1      
        if list2:
            current.next = list2
        
        # Creating a new linkedlist and setting its head node
        new_list = LinkedList()
        new_list.head = new_head
        # Returning the new list
        return new_list
    
    # Find the return the nth node or its index from the end 
    def nth_from_end(self, n):
        if self.head is None:
            pass
        
# Testing the LinkedList
ll = LinkedList() 


# ll.delete_at_position(2)
# ll.display()

# print(ll.get_length())

# print(ll.find(4))

# ll.display()
# ll.reverse()
# ll.display()

# ll.append(1)
# ll.append(4)
# ll.insert_after(3,3)
# ll.display()
# ll.remove_duplicates()
# ll.display()

# Creating a cycle manually

#     ll.head.next.next = ll. head
#     print(ll.contains_cycle())

# print(ll.find_middle())
ll.append(0)
ll.append(2)
ll.append(4)
ll.display()

l2 = LinkedList()
l2.append(1)
l2.append(3)
l2.append(5)

l2.display()

l3 = ll.merge_sorted(l2)

l3.display()