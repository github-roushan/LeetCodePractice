from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    """Node of a singly-linked list representing a single binary digit."""

    val: int = 0
    next: Optional["ListNode"] = None


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        """Return the decimal value of the binary number represented by the linked list.

        The most significant bit is at the head of the list.
        """

        result = 0
        current = head
        while current:
            result = (result << 1) | current.val
            current = current.next
        return result