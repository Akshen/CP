class Node:
    def __init__(self, data=None, nexT=None):
        self.data  = data
        self.nexT = nexT

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_ll(self):
        if self.head is None:
            print('Linked List is empty')
            return
        
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.nexT

        print(listr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        else:
            itr = self.head
            while itr.nexT:
                itr = itr.nexT
            itr.nexT = Node(data, None)
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        if self.head:
            itr = self.head
            while itr:
                count +=1
                itr = itr.nexT
        return count

    def remove_element(self, idx):
        count = 0
        if idx < 0 or idx >= self.get_length():
            raise Exception('Not a valid index')
        if idx == 0:
            self.head = self.head.nexT
            return
        itr = self.head
        while itr:
            if count == idx-1:
                itr.nexT = itr.nexT.nexT
                break
            count+=1
            itr = itr.nexT


    def insert_at(self, idx, element):
        if idx < 0 or idx >= self.get_length():
            raise Exception('Not a valid index')
        if idx == 0:
            self.insert_at_begining(element)
            return 
        count = 0
        itr = self.head
        while itr:
            if count == idx -1:
                node = Node(element, itr.nexT)
                itr.nexT = node
                break
            count+=1
            itr = itr.nexT

    def remove_by_value(self, data):
        if data == self.head.data:
            self.remove_element(0)
            return
        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                self.remove_element(count)
                break
            count+=1
            itr = itr.nexT


    def insert_after_value(self, data_after, data_to_insert):
        count = 1
        if data_after == self.head.data:
            self.insert_at(count,data_to_insert)
            return
        itr = self.head
        while itr:
            if data_after == itr.data and count < self.get_length():
                self.insert_at(count, data_to_insert)
                break
            elif count == self.get_length():
                node = Node(data_to_insert, None)
                itr.nexT = node
                break
            count +=1
            itr = itr.nexT


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['mango','orange', 'pear', 'apple', 'banana', 'grapes'])
    ll.print_ll()
    ll.insert_after_value('pear', 'raspberry')
    ll.insert_after_value('grapes', 'cherry')
    ll.insert_after_value('mango', 'jackfruit')
    ll.print_ll()
