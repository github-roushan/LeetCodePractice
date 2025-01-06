from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListCreator:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addNode(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.tail.next = None

    def getLinkedList(self):
        return self.head

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)
        if l == 0:
            return None
        if l == 1:
            return lists[0]
        leftMergedList = self.mergeKLists(lists[:l//2])
        rightMergedList = self.mergeKLists(lists[l//2:])

        ## merge this 2 linked lists using mergeSort Algorithm
        myCreator = LinkedListCreator()
        lhead = leftMergedList
        rhead = rightMergedList

        while lhead and rhead:
            if lhead.val <= rhead.val:
                nxt = lhead.next
                myCreator.addNode(lhead)
                lhead = nxt
            else:
                nxt = rhead.next
                myCreator.addNode(rhead)
                rhead = nxt

        while lhead:
            nxt = lhead.next
            myCreator.addNode(lhead)
            lhead = nxt
        
        while rhead:
            nxt = rhead.next
            myCreator.addNode(rhead)
            rhead = nxt
        
        combinedLinkedList = myCreator.getLinkedList()
        return combinedLinkedList
