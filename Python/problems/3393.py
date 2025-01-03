from typing import List
from collections import Counter
MOD = 10**9 + 7


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        N, M = len(grid), len(grid[0])
        li = [Counter() for i in range(M)]
        for i in range(N-1, -1, -1):
            nli = [Counter() for i in range(M)]
            for j in range(M-1, -1, -1):
                val = grid[i][j]
                if i == N-1 and j == M-1:
                    nli[j][val] += 1
                if i < N-1:
                    for vals, valsFre in li[j].items():
                        nli[j][vals ^ val] += valsFre
                        nli[j][vals ^ val] %= MOD
                if j < M-1:
                    for vals, valsFre in nli[j+1].items():
                        nli[j][vals ^ val] += valsFre
                        nli[j][vals ^ val] %= MOD
            li = nli
        
        return li[0][k]