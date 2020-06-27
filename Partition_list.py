# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        self.A = A
        self.B = B
        if self.A.val == self.B and self.A.next==None:
            return A
        self.bigger_before = []
        self.bigger_after = []
        self.smaller = []
        self.mark = 0
        
        while self.A!=None:
            if self.A.val < self.B:
                self.smaller.append(self.A.val)
            elif self.A.val > self.B and self.mark==0:
                self.bigger_before.append(self.A.val)
            elif self.A.val == self.B:
                self.mark = 1
                self.bigger_after.append(self.A.val)
            else:
                self.bigger_after.append(self.A.val)
            self.A = self.A.next
            
        sorted(self.smaller)
        sorted(self.bigger_before)
        self.marker = 0
        if len(self.smaller)>0:
            node = ListNode(self.smaller[0])
            self.marker = 1
            start_node = node
            
        elif len(self.bigger_before)>0 and self.marker == 0:
            node = ListNode(self.bigger_before[0])
            self.marker = 2
            start_node = node
        elif len(self.bigger_after)>0 and self.marker == 0:
            node = ListNode(self.bigger_after[0])
            self.marker = 3
            start_node = node
        else:
            return self.A
            
        if self.marker != 0:
            i = 1
        while (i <len(self.smaller)):
            while node.next != None:
                node = node.next
            node.next = ListNode(self.smaller[i])
            i+=1
        
        if self.marker == 1:
            i = 0
        else:
            i = 1
        while (i <len(self.bigger_before)):
            while node.next != None:
                node = node.next
            node.next = ListNode(self.bigger_before[i])
            i+=1
        
        #node.next = ListNode(self.B)
        #print(self.smaller)
        
        if self.marker == 1 or self.marker==2:
            i = 0
        else:
            i = 1
        while (i <len(self.bigger_after)):
            while node.next != None:
                node = node.next
            node.next = ListNode(self.bigger_after[i])
            i+=1


        return start_node
