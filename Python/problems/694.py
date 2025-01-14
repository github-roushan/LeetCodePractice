from queue import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        N = len(senate)
        turn_order = deque(range(N))

        radiant_count = senate.count("R")
        dire_count = senate.count("D")
        
        radiant_pending_removals = 0
        dire_pending_removals = 0

        while True:
            ## remove all pending radiant removals
            while turn_order and senate[turn_order[0]]== "R" and radiant_pending_removals:
                radiant_pending_removals -= 1
                radiant_count -= 1
                turn_order.popleft()
            
            ## remove all pending dire removals
            while turn_order and senate[turn_order[0]] == "D" and dire_pending_removals:
                dire_pending_removals -= 1
                dire_count -= 1
                turn_order.popleft()
            
            
            if senate[turn_order[0]] == "R":
                if dire_count == 0:
                    return "Radiant"
                dire_pending_removals += 1
                turn_order.append(turn_order.popleft())
            else:
                if radiant_count == 0:
                    return "Dire"
                radiant_pending_removals += 1
                turn_order.append(turn_order.popleft())
