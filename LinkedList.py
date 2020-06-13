class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    
class LinkedList:
    def __init__(self):
        self.start = None

    def insertLast(self, value):
        newNode = node(value)
        if self.start==None:
            self.start = newNode
        else:
            temp = self.start
            while(temp.next!=None):
                temp = temp.next
            temp.next = newNode
    
    def deleteFirst(self):
        if self.start == None:
            return 0
        self.start = self.start.next

    def viewList(self):
        if self.start == None:
            print('Empty List')
        else:
            temp = self.start
            while temp != None:
                print(temp.data)
                temp = temp.next

nn = LinkedList()
d =0
ans = '002'
while d<len(ans):
    nn.insertLast(ans[d])
    d+=1
nn.viewList()