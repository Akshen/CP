"""
Stack Implementation
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == [] 

    def pop_specific(self, item):
        temp = []
        i = len(self.items)-1
        while self.items[i] != item:
            temp.append(self.items.pop())
            i-=1
        print('Item {} removed '.format(self.items.pop()))
        while len(temp)>0:
            self.items.append(temp.pop())

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def display(self):
        for i in self.items: print(i)

'''
obj = Stack()
obj.push(3)
obj.push(31)
obj.push(4)
obj.push(5)
obj.display()
print('*'*10)
obj.pop_specific(31)
obj.display()
print('*'*10)
obj.pop_specific(3)
obj.push(8)
obj.display()
'''