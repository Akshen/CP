class Node:
    def __init__(self, data=None, nexT=None, prev=None):
        self.data = data
        self.nexT = nexT
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head == None:
            self.head = Node(value)
            return    

        itr = self.head
        while itr:
            if itr.nexT == None:
                itr.nexT = Node(value, None, itr)
                break
            itr = itr.nexT

    def print_dll(self):
        if self.head:
            dll =''
            itr = self.head
            while itr:
                dll +=str(itr.data) + '-->'
                itr = itr.nexT
            print(dll)
            return
        return

    def print_reverse_dll(self):
        if self.head:
            dll = ''
            itr = self.head
            while itr:
                temp  = itr
                itr = itr.nexT
            itr = temp
            while itr:
                dll +=str(itr.data)+ '-->'
                itr = itr.prev
            print(dll)
            return
        return

    def get_length(self):
        count = 0
        if self.head:
            itr = self.head
            while itr:
                count+=1
                itr = itr.nexT
        return count

    def delete(self, value):
        if self.head.data == value:
            if self.head.nexT:
                self.head.nexT.prev = None
                self.head = self.head.nexT
                return
            else:
                self.head = None
                return
        
        count = 1
        itr = self.head
        while itr:
            if itr.data == value and count < self.get_length():
                itr.prev.nexT = itr.nexT
                itr.nexT.prev = itr.prev
                break
            if itr.data == value and count == self.get_length():
                itr.prev.nexT = None
                break
            count +=1
            itr = itr.nexT
        return


dll = DoublyLinkedList()
dll.insert(2)
dll.insert(3)
dll.insert(4)
dll.insert(5)
dll.delete(2)
dll.print_dll()
dll.print_reverse_dll()