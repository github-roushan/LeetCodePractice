from typing import List


class Solution:
    def minOperations(self, b: str) -> List[int]:
        ## find total moves needed for all the balls 
        ## on the left of i to move to i
        prev_balls, total_moves = 0, 0
        answer = [0]*len(b)
        for i in range(len(b)):
            total_moves += prev_balls
            answer[i] = total_moves
            if b[i]=="1":
                prev_balls += 1
        
        ## find total moves needed for all the balls 
        ## on the right of i to move to i
        prev_balls, total_moves = 0, 0
        for i in range(len(b)-1, -1,-1):
            total_moves += prev_balls
            answer[i] += total_moves
            if b[i] == "1":
                prev_balls += 1
        return answer