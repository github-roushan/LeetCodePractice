from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        revHead = None
        curHead = head
        while curHead:
            revHead, curHead.next, curHead = curHead, revHead, curHead.next
        return revHead