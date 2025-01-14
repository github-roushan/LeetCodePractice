from cmath import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _count_good_nodes(self, node, max_value_in_chain):
        if node == None:
            return 0
        total = node.val >= max_value_in_chain
        total += self._count_good_nodes(node.left, max(max_value_in_chain, node.val))
        total += self._count_good_nodes(node.right, max(max_value_in_chain, node.val))
        return total

    def goodNodes(self, root: TreeNode) -> int:
        return self._count_good_nodes(root, -inf)
        