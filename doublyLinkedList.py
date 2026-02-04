class Node:
    def __init__(self, prev, data, next) -> None:
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def print_forward(self):
        if self.head is None:
            print("Linked List is empty!")
            return
        
        current = self.head
        print(end="None<-->")
        while current:
            print(current.data, end="<-->")
            current = current.next
        print("None")
    
    def print_backward(self):
        if self.head is None:
            print("Linked List is empty!")
            return
        
        current = self.tail
        print(end="None<-->")
        while current:
            print(current.data, end="<-->")
            current = current.prev
        print("None")
    
    def get_length(self) -> int:
        if self.head is None:
            return 0
        
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def insert_at_begining(self, data):
        node = Node(None, data, self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node
        
    def insert_at_end(self, data):
        node = Node(self.tail, data, None)
        self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node
            
    def __get_node_by_index(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            count+=1
            current = current.next
        raise Exception("Index does not exists!")
    
    def insert_at(self, index, data):
        if index == 0:
            self.insert_at_begining(data)
            return
        nodeBeforeIndex = self.__get_node_by_index(index-1)
        node = Node(nodeBeforeIndex, data, nodeBeforeIndex.next)
        nodeBeforeIndex.next = node
        
    def remove_at(self, index):
        if (index == 0):
            self.head.next.prev = None
            self.head = self.head.next
            return
        node_before_index = self.__get_node_by_index(index-1)
        #if we have to remove tail node
        if node_before_index.next == self.tail:
            node_before_index.next = None
            self.tail = node_before_index
            return
        
        node_after_index = node_before_index.next.next
        node_before_index.next = node_after_index
        node_after_index.prev = node_before_index
         

#Testing
ll = DoublyLinkedList()
ll.insert_at_begining(4)
ll.insert_at_begining(3)
ll.insert_at_begining(2)
ll.insert_at_begining(1)
ll.insert_at_end(5)

ll.remove_at(4)

ll.print_forward()
ll.print_backward()

print(ll.get_length())