from collections import defaultdict
from typing import List


def canVisitAllNodes(n, adj, maxWtAllowed):
    visited = [False]*n
    def dfs(node, visited):
        if visited[node]:
            return
        visited[node] = True
        for cnode, weight in adj[node]:
            if weight > maxWtAllowed:
                continue
            dfs(cnode, visited)
    dfs(0, visited)
    return all(visited)

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:        
        adj = defaultdict(list)
        ## Space is O(Edges)
        for u,v,w in edges:
            adj[v].append((u, w))
        
        LIM = 10**6 + 1
        ## binary search
        low, high = 0, LIM
        ## Time: O(n * log(LIM))
        ## Space: O(n)
        while low < high:
            mid = (low + high)//2
            stat = canVisitAllNodes(n, adj, mid)
            if stat:
                high = mid
            else:
                low = mid+1
        return -1 if low == LIM else low
