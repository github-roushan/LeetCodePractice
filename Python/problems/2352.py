from typing import Counter, List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowC = Counter(tuple(row) for row in grid)
        
        totalPairs = 0
        for col in zip(*grid):
            totalPairs += rowC[col]
        return totalPairs