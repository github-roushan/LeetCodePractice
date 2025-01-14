from cmath import inf
from collections import deque
from typing import Counter, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelSumCounter = Counter()

        node_queue = deque([(root, 1)])
        while node_queue:
            node, level = node_queue.popleft()
            levelSumCounter[level] += node.val
            if node.left:
                node_queue.append((node.left, level+1))
            if node.right:
                node_queue.append((node.right, level+1))

        curMaxLevelSum = -inf
        bestLevel = inf
        for level, levelSum in levelSumCounter.items():
            if levelSum > curMaxLevelSum:
                curMaxLevelSum = levelSum
                bestLevel = level
            elif levelSum == curMaxLevelSum:
                bestLevel = min(bestLevel, level)

        return bestLevel
