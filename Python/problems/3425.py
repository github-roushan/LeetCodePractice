from collections import defaultdict


class Solution:
    def __init__(self):
        self.res = (0, 1)
        self.depth = [0] * 50001

    def dfs(self, node, pnode, al, nums, left, cur_depth, cumm_wt_sum):
        prev_depth = self.depth[nums[node]]
        self.depth[nums[node]] = cur_depth
        left = max(left, prev_depth)
        self.res = min(self.res, (-(cumm_wt_sum[-1] - cumm_wt_sum[left]), cur_depth - left))
        
        for cnode, edgeWt in al[node]:
            if cnode != pnode:
                cumm_wt_sum.append(cumm_wt_sum[-1] + edgeWt)
                self.dfs(cnode, node, al, nums, left, cur_depth + 1, cumm_wt_sum)
                cumm_wt_sum.pop()
        
        self.depth[nums[node]] = prev_depth

    def longestSpecialPath(self, edges, nums):
        adj = defaultdict(list)
        
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        self.dfs(0, -1, adj, nums, 0, 1, [0])
        
        return [-self.res[0], self.res[1]]

