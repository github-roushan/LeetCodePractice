from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListCreator:
    def __init__(self):
        self.head = None
        self.tail = None

    def appendFront(self, node):
        if self.head == None:
            self.tail = node
        node.next = self.head
        self.head = node
        #print("called", self.head.val, self.anteriorTail)
    
    def getHead(self):
        return self.head
    
    def getTail(self):
        return self.tail

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        curHead = head
        linkedListReverser = LinkedListCreator()
        curTaken = 0

        ## reverse First K nodes
        while curHead and curTaken < k:
            curTaken += 1
            nxtNode = curHead.next
            linkedListReverser.appendFront(curHead)
            curHead = nxtNode
        
        leftLLHead = linkedListReverser.getHead()
        leftLLTail = linkedListReverser.getTail()

        ## if it falls short of k nodes reverse it again to return it to original state
        if curTaken != k:
            newReverser = LinkedListCreator()
            while leftLLHead:
                nxt = leftLLHead.next
                newReverser.appendFront(leftLLHead)
                leftLLHead = nxt
            leftLLHead = newReverser.getHead()
            leftLLTail = newReverser.getTail()
             
        ## from k+1 node onwards recurively call the reverseKGroup to solve the subproblem
        rightLLHead = self.reverseKGroup(curHead, k)

        if leftLLTail == None:
            return rightLLHead
        else:
            leftLLTail.next = rightLLHead
        
        return leftLLHead