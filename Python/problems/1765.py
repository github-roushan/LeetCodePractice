from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        N, M = len(isWater), len(isWater[0])
        ## multi source bfs
        visited = {}

        line = deque()
        for i in range(N):
            for j in range(M):
                if isWater[i][j] == 1:
                    line.append((i, j, 0))
                    visited[(i, j)] = True
        
        result = [[0]*M for i in range(N)]
        while line:
            i, j, d = line.popleft()
            result[i][j] = d

            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if ni < 0 or N <= ni  or nj < 0 or M <= nj:
                    continue
                if (ni, nj) in visited:
                    continue
                line.append((ni, nj, d+1))
                visited[(ni, nj)] = True
        return result