from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevHead = None
        slowPointer = fastPointer = head

        while fastPointer and fastPointer.next:
            prevHead = slowPointer
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        
        if prevHead == None:
            head = None
        else:
            prevHead.next = slowPointer.next
        return head