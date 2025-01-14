from queue import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        N = len(senate)
        turnOrder = deque(range(N))

        radiantCount = senate.count("R")
        direCount = senate.count("D")
        
        radiantPendingRemovals = 0
        direPendingRemovals = 0

        while True:
            ## execute all pending radiant removals
            while turnOrder and senate[turnOrder[0]]== "R" and radiantPendingRemovals:
                radiantPendingRemovals -= 1
                radiantCount -= 1
                turnOrder.popleft()
            
            ## execute all pending dire removals
            while turnOrder and senate[turnOrder[0]] == "D" and direPendingRemovals:
                direPendingRemovals -= 1
                direCount -= 1
                turnOrder.popleft()
            
            
            if senate[turnOrder[0]] == "R":
                if direCount == 0:
                    return "Radiant"
                direPendingRemovals += 1
                turnOrder.append(turnOrder.popleft())
            else:
                if radiantCount == 0:
                    return "Dire"
                radiantPendingRemovals += 1
                turnOrder.append(turnOrder.popleft())
