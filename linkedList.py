class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self) -> None:
            self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node

    def insert_at(self, index, data):
        # If we have to insert at index 0 (i.e. insert at the beginning)
        if index == 0:
            self.insert_at_beginning(data)
            return

        before_index = self.__get_node_at_index(index - 1)
        node = Node(data, before_index.next)
        before_index.next = node

    def print_linked_list(self):
        if not self.head:
            print("Linked List is empty")
            return

        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print()

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __get_node_at_index(self, index):
        current = self.head
        current_index = 0
        while current:
            if current_index == index:
                return current
            current = current.next
            current_index += 1
        raise Exception("Index does not exist!")

    def get_element_by_index(self, index):
        node = self.__get_node_at_index(index)
        return node.data

    def remove_at(self, index):
        if index == 0:
            self.head = self.head.next
            return
        else:
            to_remove = self.__get_node_at_index(index - 1)
            to_remove.next = to_remove.next.next

    def __get_node_by_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        raise Exception("Value does not exist in the given Linked List!")

    def insert_after_value(self, value, data):
        current = self.head
        while current:
            if current.data == value:
                node = Node(data, current.next)
                current.next = node
                break
            current = current.next
        else:
            raise Exception("Value does not exist!")

    def remove_by_value(self, value):
        current = self.head
        # If value is in the head node, we need to update the head
        if current.data == value:
            self.head = self.head.next
            return

        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
        raise Exception("Value does not exist!")

    def reverse_list(self):
        before = None
        current = self.head
        while current:
            after = current.next
            current.next = before
            before = current
            current = after
        self.head = before
        
    def reverse_list_recursive(self, head):
        if (head is None) or (head.next is None):
            return head
        new_head = self.reverse_list_recursive(head.next)
        current = head.next
        current.next = head
        head.next = None
        self.head = new_head
        return  new_head
    
    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
    
    def find_cycle(self):
        slow = self.head
        fast = self.head
        cycle_present = False
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle_present = True
                break
        if cycle_present:
            slow = self.head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        else:
            return None
        
    def add_cycle(self, start, end):
        s = self.__get_node_at_index(start)
        e = self.__get_node_at_index(end)
        
        s.next = e

# Testing the LinkedList
ll = LinkedList()
ll.insert_at_beginning(1)
ll.insert_at_beginning(2)
ll.insert_at_end(0)
ll.insert_at_beginning(4) 

ll.print_linked_list()
print(ll.detect_cycle())
ll.add_cycle(3, 1)
print(ll.detect_cycle())

cycle_begin = ll.find_cycle()

print(cycle_begin.data)