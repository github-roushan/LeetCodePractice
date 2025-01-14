from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_view = []
        if root == None:
            return right_side_view
        node_queue = deque([(root, 0)])

        while node_queue:
            node, level = node_queue.popleft()
            if level == len(right_side_view):
                right_side_view.append(node.val)
            right_side_view[level] = node.val

            if node.left:
                node_queue.append((node.left, level+1))
            if node.right:
                node_queue.append((node.right, level+1))
        
        return right_side_view