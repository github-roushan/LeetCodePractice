from typing import List
from collections import defaultdict
import sys

# Increase recursion limit to handle deep recursion on large trees
sys.setrecursionlimit(10**6)

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        discovery_time = [float("inf")] * n
        level = [-1] * n
        parent = [-1] * n
        graph = defaultdict(list)

        self.build_graph(edges, graph)
        self.assign_parents_and_levels(graph, parent, level)
        self.calculate_bob_discovery_times(bob, parent, discovery_time)
        
        return self.calculate_max_profit(0, -1, graph, level, discovery_time, amount)

    def build_graph(self, edges: List[List[int]], graph: defaultdict) -> None:
        """Constructs an undirected graph from the list of edges."""
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

    def assign_parents_and_levels(self, graph: defaultdict, parent: List[int], level: List[int]) -> None:
        """Performs DFS from the root to assign parent and level to each node."""
        def dfs(node: int, parent_node: int, current_level: int) -> None:
            parent[node] = parent_node
            level[node] = current_level
            for neighbor in graph[node]:
                if neighbor != parent_node:
                    dfs(neighbor, node, current_level + 1)

        dfs(0, -1, 0)

    def calculate_bob_discovery_times(self, bob: int, parent: List[int], discovery_time: List[int]) -> None:
        """Backtracks from Bob's starting node to the root, recording when Bob visits each node."""
        time = 0
        current = bob
        while current != -1:
            discovery_time[current] = time
            time += 1
            current = parent[current]

    def calculate_max_profit(
        self,
        node: int,
        parent_node: int,
        graph: defaultdict,
        level: List[int],
        discovery_time: List[int],
        amount: List[int]
    ) -> int:
        """Recursively computes the maximum profit path from the root to a leaf."""
        max_child_profit = float("-inf")
        
        for neighbor in graph[node]:
            if neighbor != parent_node:
                profit = self.calculate_max_profit(neighbor, node, graph, level, discovery_time, amount)
                max_child_profit = max(max_child_profit, profit)

        if max_child_profit == float("-inf"):
            max_child_profit = 0  # Leaf node

        # Determine how much of the amount can be collected
        if level[node] < discovery_time[node]:
            collected_amount = amount[node]
        elif level[node] == discovery_time[node]:
            collected_amount = amount[node] // 2
        else:
            collected_amount = 0

        return collected_amount + max_child_profit
