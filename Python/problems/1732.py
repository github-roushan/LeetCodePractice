from itertools import accumulate
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(max(accumulate(gain)), 0)