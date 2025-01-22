from cmath import inf
from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        ROWS = len(coins)
        COLS = len(coins[0])
        down = [[-inf]*3 for i in range(COLS)]
        
        for r in range(ROWS-1, -1, -1):
            newDown = [[-inf]*3 for i in range(COLS)]
            side = [-inf]*3
            if r == ROWS-1:
                side[0] = 0
            for c in range(COLS-1, -1, -1):
                if coins[r][c] < 0:
                    ## either neutralize this or get robbed
                    ## neutralize
                    newDown[c][1] = max(side[0], down[c][0])
                    newDown[c][2] = max(side[1], down[c][1])
                    
                    ## getRobbed with neutralization before
                    newDown[c][0] = max(side[0], down[c][0]) + coins[r][c]
                    newDown[c][1] = max(max(side[1], down[c][1]) + coins[r][c], newDown[c][1])
                    newDown[c][2] = max(max(side[2], down[c][2]) + coins[r][c], newDown[c][2])
                    
                else:
                    ## i am gonna take all the coins
                    newDown[c][0] = coins[r][c] + max(side[0], down[c][0])
                    newDown[c][1] = coins[r][c] + max(side[1], down[c][1])
                    newDown[c][2] = coins[r][c] + max(side[2], down[c][2])
                
                side = newDown[c]
            down = newDown
        return max(down[0])
