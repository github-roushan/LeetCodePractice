from typing import List
from math import inf

class Solution:
    def maxBalancedShipments(self, weights: List[int]) -> int:
        max_balanced = 0
        previous_balanced = -1
        next_weight = inf

        for current_weight in reversed(weights):
            current_max = max_balanced

            # Check if current_weight can displace the previous next_weight
            if current_weight > next_weight:
                current_max = max(current_max, previous_balanced + 1)

            # Update tracking variables for next iteration
            next_weight = current_weight
            max_balanced, previous_balanced = current_max, max_balanced

        return max_balanced
