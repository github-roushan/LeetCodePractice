from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curNode = root
        while curNode:
            if curNode.val == val:
                return curNode
            elif val < curNode.val:
                curNode = curNode.left
            else:
                curNode = curNode.right
        return curNode