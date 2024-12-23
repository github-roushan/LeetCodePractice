from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Preorder traversal: Root -> Left -> Right (iterative approach)
        if not root:
            return []  # Return empty list if the tree is empty
        
        stack, output = [root], []  # Stack for DFS, output for result
        
        while stack:
            # Process the current node
            node = stack.pop()
            output.append(node.val)

            # Add right child to stack (processed later)
            if node.right:  
                stack.append(node.right)
            # Add left child to stack (processed next)
            if node.left:  
                stack.append(node.left)
        
        return output
