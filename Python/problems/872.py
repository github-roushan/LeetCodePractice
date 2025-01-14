from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderLeafOrderGen(root):
    current = root
    stack = []
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        if current.left == current.right == None:
            yield current.val
        current = current.right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1LeafOrderGen = inorderLeafOrderGen(root1)
        root2LeafOrderGen = inorderLeafOrderGen(root2)

        while True:
            try:
                v1 = next(root1LeafOrderGen)
            except:
                try:
                    v2 = next(root2LeafOrderGen)
                    return False
                except:
                    return True
            try:
                v2 = next(root2LeafOrderGen)
            except:
                return False
            else:
                if v1 != v2:
                    return False