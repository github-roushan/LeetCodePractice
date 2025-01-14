from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for ind, el in enumerate(nums):
            right -= el
            if left == right:
                return ind
            left += el
        return -1