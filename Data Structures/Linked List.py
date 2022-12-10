class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
    
    def push(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
    
    def append(self, value):
        headNode = self.head
        while (headNode.next):
            headNode = headNode.next
        headNode.next = Node(value)
    
    def printList(self):
        headNode = self.head
        while (headNode.next):
            print(headNode.val, end="->")
            headNode = headNode.next
        print(headNode.val)
    
    def pop(self):
        prev = None
        headNode = self.head
        while (headNode.next):
            prev = headNode
            headNode = headNode.next
        prev.next = None
        temp = headNode
        del headNode
        return temp

    def insert(self, val, idx):
        counter = 0
        headNode = self.head
        while counter < idx-1:
            headNode = headNode.next
            counter+=1
        temp = headNode.next
        headNode.next = Node(val)
        headNode.next.next = temp
        

ll1 = LinkedList()
ll1.push(3)
ll1.push(4)
ll1.push(5)
ll1.push(6)
ll1.printList()
ll1.pop()
ll1.printList()
ll1.insert(7,2)
ll1.printList()
ll1.append(10)
ll1.printList()
