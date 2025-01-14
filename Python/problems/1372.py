from cmath import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def _maxZigZagLengthFinder(node):
            max_zigzag_data = [-1, -1, -inf]  # left, right, max
            if node == None:
                return max_zigzag_data

            # curDire == 0
            max_zigzag_data_left = _maxZigZagLengthFinder(node.left)
            max_zigzag_data[0] = max(
                max_zigzag_data[0], 1 + max_zigzag_data_left[1])

            # curDire == 1
            max_zigzag_data_right = _maxZigZagLengthFinder(node.right)
            max_zigzag_data[1] = max(
                max_zigzag_data[1], 1 + max_zigzag_data_right[0])

            max_zigzag_data[2] = max(
                *max_zigzag_data,
                max_zigzag_data_left[2],
                max_zigzag_data_right[2]
            )
            return max_zigzag_data

        return _maxZigZagLengthFinder(root)[2]
