from typing import Counter, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def _pathSumHelper(node, pathSumFre, currentPathSum):
            if node == None:
                return 0

            currentPathSum += node.val
            totalPaths = pathSumFre[currentPathSum - targetSum]

            pathSumFre[currentPathSum] += 1
            totalPaths += _pathSumHelper(node.left, pathSumFre, currentPathSum)
            totalPaths += _pathSumHelper(node.right,
                                         pathSumFre, currentPathSum)

            pathSumFre[currentPathSum] -= 1
            currentPathSum -= node.val
            return totalPaths

        return _pathSumHelper(root, Counter([0]), 0)
