from cmath import inf
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        LinkedList1, LinkedList2 = self._bisect(head) ## cut linkedList in 2 same parts
        LinkedList2 = self._reverse(LinkedList2)

        linkedListHead1 = LinkedList1[0]
        linkedListHead2 = LinkedList2[0]
        maxPairSum = -inf
        while linkedListHead1 and linkedListHead2:
            maxPairSum = max(maxPairSum, linkedListHead1.val + linkedListHead2.val)
            linkedListHead1 = linkedListHead1.next
            linkedListHead2 = linkedListHead2.next
        
        LinkedList2 = self._reverse(LinkedList2)
        LinkedList1[1].next = LinkedList2[0]
        LinkedList2[1].next = None
        return maxPairSum
    
    def _bisect(self, linkedListHead):
        slowPointer = linkedListHead
        fastPointer = linkedListHead.next
        while fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        
        return (linkedListHead, slowPointer), (slowPointer.next, fastPointer)
    
    def _reverse(self, linkedList):
        curHead = linkedList[0]
        reversedHead = None
        while curHead:
            reversedHead, curHead.next, curHead = curHead, reversedHead, curHead.next
        return reversedHead, linkedList[0]