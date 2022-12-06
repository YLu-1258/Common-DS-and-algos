class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
    
    def appendFront(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
    
    def printList(self):
        while (self.head.next != None):
            print(self.head.val, end="->")
            self.head = self.head.next
        print(self.head.val)
    


ll1 = LinkedList()
ll1.appendFront(3)
ll1.appendFront(4)
ll1.appendFront(5)
ll1.appendFront(6)
ll1.printList()
