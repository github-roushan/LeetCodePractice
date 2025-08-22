from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        prevRow = [0]*(C+1) ## 1 indexed

        totalSquares = 0
        for i in range(R):
            prevValue = 0
            curRow = [0]*(C+1)
            for j in range(C):
                ## at i,j look top left and daig left
                mn = prevValue ## looking left
                mn = min(mn, prevRow[j+1]) ## looking top
                mn = min(mn, prevRow[j]) ## looking main diag left

                if matrix[i][j]:
                    curRow[j+1] = matrix[i][j] + mn

                prevValue = curRow[j+1]
                totalSquares += curRow[j+1]
            prevRow = curRow
        
        return totalSquares