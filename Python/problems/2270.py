from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        cur = 0
        validSplits = 0
        total = sum(nums)
        for i in range(len(nums) - 1):
            cur += nums[i]
            if 2*cur >= total:
                validSplits += 1
        return validSplits