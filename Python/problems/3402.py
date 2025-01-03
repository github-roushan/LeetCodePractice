from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        totalOperations = 0
        for j in range(len(grid[0])):
            prev = -1
            for i in range(len(grid)):
                v = max(0, prev - grid[i][j] + 1)
                totalOperations += v
                prev = grid[i][j] + v
        return totalOperations