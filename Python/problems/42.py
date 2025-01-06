from typing import List
from itertools import accumulate


class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeftHeight = [0] + list(accumulate(height, max))
        maxRightHeight = list(accumulate(height[-1::-1], max))[-1::-1] + [0]
        maxTrappableWater = 0
        for i, h in enumerate(height):
            maxTrappableWater += max(0 , min(maxLeftHeight[i], maxRightHeight[i]) - h)

        return maxTrappableWater