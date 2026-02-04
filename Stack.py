# Implementing Basic Stack Data Structure using deque.
# Note : We can use deque directly without implementing the stack but we will not have specific
# methods like peek (we will have to use -1 index to access view last element)

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, data):
        self.container.append(data)
        return
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)