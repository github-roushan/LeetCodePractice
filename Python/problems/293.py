from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroInd = -1
        N = len(nums)
        for ind in range(N):
            if nums[ind] == 0:
                continue
            else:
                lastNonZeroInd += 1
                nums[lastNonZeroInd], nums[ind] = nums[ind], nums[lastNonZeroInd]
        return nums
         
        