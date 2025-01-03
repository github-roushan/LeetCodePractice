from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        totalSubarrays = 0
        for j in range(1, len(nums)-1):
            if 2 * (nums[j-1] + nums[j+1]) == nums[j]:
                totalSubarrays += 1
        return totalSubarrays
        