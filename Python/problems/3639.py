from typing import List
from sortedcontainers import SortedSet

class Solution:
    def minTime(self, s: str, insertionOrder: List[int], k: int) -> int:
        n = len(s)
        starPositions = SortedSet([n])  # Initially only a sentinel at the end
        starDistances = [0] * n         # Distance to the next star for each position

        totalCost = 0
        steps = 0

        for currentPos in insertionOrder:
            # Find the next star index after currentPos
            nextIndex = starPositions.bisect_right(currentPos)
            nextStarPos = starPositions[nextIndex]
            
            # Distance from current star to the next star
            starDistances[currentPos] = nextStarPos - currentPos
            starPositions.add(currentPos)

            # Add contribution of this new star
            totalCost += (currentPos + 1) * starDistances[currentPos]
            
            # Update the previous segment if any
            if nextIndex > 0:
                previousStarPos = starPositions[nextIndex - 1]
                originalDist = starDistances[previousStarPos]
                updatedDist = currentPos - previousStarPos
                removedDist = originalDist - updatedDist

                totalCost -= (previousStarPos + 1) * removedDist
                starDistances[previousStarPos] = updatedDist

            # Check if total cost has reached or exceeded k
            if totalCost >= k:
                return steps

            steps += 1

        return -1
