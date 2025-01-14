from functools import reduce
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(
                    reduce(
                        lambda acc, x: (x + min(acc), acc[0]), 
                        cost[-1::-1], 
                        (0, 0)
                    )
                )
