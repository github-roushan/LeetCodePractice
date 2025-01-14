from cmath import inf
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        kElementRunningSum = 0
        maxRunningSum = -inf
        for ind, el in enumerate(nums):
            kElementRunningSum += el
            if ind >= k:
                kElementRunningSum -= nums[ind-k]
            if ind >= k-1:
                maxRunningSum = max(maxRunningSum, kElementRunningSum)
        return maxRunningSum / k
    