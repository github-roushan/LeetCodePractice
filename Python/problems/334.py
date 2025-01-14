from typing import List
from math import inf

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        numi = inf
        numj = inf

        for num in nums:
            if num > numj:
                return True
            if num > numi:
                numj = min(numj, num)
            numi = min(numi, num)
        return False
