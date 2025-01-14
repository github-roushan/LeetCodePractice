from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListContainer:
    def __init__(self):
        self.headNode = None
        self.tailNode = None
    
    def addNode(self, node):
        if self.tailNode:
            self.tailNode.next = node
            self.tailNode = node
        else:
            self.headNode = node
            self.tailNode = node
        self.tailNode.next = None

    def getHead(self):
        return self.headNode

    def getTail(self):
        return self.tailNode

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddIndexedList = LinkedListContainer()
        evenIndexedList = LinkedListContainer()

        indexCounter = 1
        while head:
            nextNode = head.next
            if indexCounter % 2:
                oddIndexedList.addNode(head)
            else:
                evenIndexedList.addNode(head)
            head = nextNode
            indexCounter += 1
        
        if oddIndexedList.getHead() == None:
            return None
        oddIndexedList.getTail().next = evenIndexedList.getHead()
        return oddIndexedList.getHead()
