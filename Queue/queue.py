# No need for implentation of queue from scratch, Understanding concepts is enough

from collections import deque
class Queue:
    
    def __init__(self):
        self.list = deque()
    
    def enqueue(self, data):
        self.list.appendleft(data)
    
    def dequeue(self):
        return self.list.pop()
    
    def isEmpty(self):
        return len(self.list) == 0
    
    def size(self):
        return len(self.list)

    