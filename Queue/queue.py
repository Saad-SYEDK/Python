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

# Exercise 1 - Producer-Consumer problem
'''
    Read the question here :
    https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue_exercise.md

    Design a food ordering system where your python program will run two threads, Place Order: This thread
        will be placing an order and inserting that into a queue. This thread places new order every 0.5 
        second. (hint: use time.sleep(0.5) function)
    Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. 
    This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
    Pass following list as an argument to place order thread,
        orders = ['pizza','samosa','pasta','biryani','burger']
    This problem is a producer,consumer problem where place_order thread is producing orders whereas 
    server_order thread is consuming the food orders.
'''

# Import threading and time module
import threading
import time

#Create a queue for order
orders = Queue()

# Place-order function
def place_order(order):
    for item in order:
        # Add item into the queue
        print("Placing order for", item)
        orders.enqueue(item)
        # Place new order into queue every 0.5 sec
        time.sleep(0.5)

# Server-order function
def serve_order():
    while not orders.isEmpty():
        print("serving", orders.dequeue())
        time.sleep(2)

# Arguments for place_order
order = ['pizza','samosa','pasta','biryani','burger']

# Create two threads for place order and serve order
place_thread = threading.Thread(target=place_order, args=(order,    ))
serve_thread = threading.Thread(target=serve_order)

# Start place_order thread
place_thread.start()

#one second after the place order thread, start the serve thread
time.sleep(1)
serve_thread.start()


        
    