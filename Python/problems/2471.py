from collections import defaultdict
from typing import Optional

# TreeNode class representing a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to compute minimum swaps to sort a list
def getMinSwaps(lis):
    # Get indices of sorted elements
    sortedIndices = sorted(range(len(lis)), key=lambda x: lis[x])
    visited = [False] * len(lis)
    swapsNeeded = 0

    # Traverse the list and compute cycles
    for i in range(len(lis)):
        if visited[i] or sortedIndices[i] == i:
            continue  # Skip if already visited or in correct position

        cycleSize, curNode = 0, i
        # Follow the cycle and mark nodes as visited
        while not visited[curNode]:
            visited[curNode] = True
            curNode = sortedIndices[curNode]
            cycleSize += 1

        swapsNeeded += cycleSize - 1  # Add swaps needed for this cycle
    return swapsNeeded

# Main solution class
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        # Helper DFS function to collect node values at each level
        def dfs(node, level, nodes):
            if not node:
                return
            nodes[level].append(node.val)
            dfs(node.left, level + 1, nodes)
            dfs(node.right, level + 1, nodes)

        nodes = defaultdict(list)  # Dictionary to store nodes at each level
        dfs(root, 0, nodes)  # Start DFS from the root
        
        # Return the sum of minimum swaps needed at each level
        return sum(getMinSwaps(level) for level in nodes.values())
