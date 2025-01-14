from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result = [1]*N
        prev = 1
        for i in range(N):
            result[i] *= prev
            prev *= nums[i]
        prev = 1
        for i in range(N-1, -1, -1):
            result[i] *= prev
            prev *= nums[i]
        return result
    