'''
For all exercises use Queue class implemented in main tutorial.

Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.


Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.
'''

class Queue:
    def __init__(self):
        self.buffer = []

    def insert(self, element):
        self.buffer.insert(0, element)

    def popq(self):
        self.buffer.pop()

    def sizeQ(self):
        return len(self.buffer)

    def is_empty(self):
        return True if len(self.buffer)==0 else False

orders = ['pizza','samosa','pasta','biryani','burger']
from time import sleep
import threading
q_obj = Queue()

def place_order(porders):
    for i in porders:
        q_obj.insert(i)
        sleep(0.5)
        #print(q_obj.buffer, 'Order Placed')

def server_order():
    while True:
        sleep(2)
        print(q_obj.buffer, 'Order Serving')
        q_obj.popq()
        if q_obj.is_empty():
            return
          
        

task_1 = threading.Thread(target=place_order, args=(orders,))
task_2 = threading.Thread(target=server_order, args=())

task_1.start()
task_2.start()

