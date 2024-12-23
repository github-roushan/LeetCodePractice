from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinSwaps(lis):
    sorted_indices = sorted(range(len(lis)), key=lambda x: lis[x])
    visited = [False] * len(lis)
    swaps = 0

    for i in range(len(lis)):
        if visited[i] or sorted_indices[i] == i:
            continue

        cycle_size, cur_node = 0, i
        while not visited[cur_node]:
            visited[cur_node] = True
            cur_node = sorted_indices[cur_node]
            cycle_size += 1

        swaps += cycle_size - 1
    return swaps

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def dfs(node, level, nodes):
            if not node:
                return
            nodes[level].append(node.val)
            dfs(node.left, level + 1, nodes)
            dfs(node.right, level + 1, nodes)

        nodes = defaultdict(list)
        dfs(root, 0, nodes)
        
        return sum(getMinSwaps(level) for level in nodes.values())
