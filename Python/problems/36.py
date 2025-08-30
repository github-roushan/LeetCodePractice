def isDistinct(itr):
    data = [dat for dat in itr if dat != "."]
    return len(set(data)) == len(data)

def getBox(grid, i, j, l, b):
    data = []
    for di in range(l):
        ni = i + di
        if ni >= len(grid):
            break 
        for dj in range(b):
            nj = j + dj
            if nj >= len(grid[0]):
                break
            data.append(grid[ni][nj])
    return data

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## validate row
        for row in board:
            status = isDistinct(row)
            if status == False:
                return status
        ## validate col
        for col in zip(*board):
            status = isDistinct(col)
            if status == False:
                return status
        
        ## validate box
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                status = isDistinct(getBox(board, r, c, 3, 3))
                if status == False:
                    return status
        return True