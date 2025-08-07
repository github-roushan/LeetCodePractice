from typing import List


class Solution:
    def _getInd(self, nums, cur_ind, increasing = True):
        N = len(nums)
        if cur_ind == N:
            return N

        for i in range(cur_ind, N-1):
            if increasing and nums[i] >= nums[i + 1]:
                return i
            elif not increasing and nums[i] <= nums[i+1]:
                return i

        return N
                
    def isTrionic(self, nums: List[int]) -> bool:
        N = len(nums)
        p = self._getInd(nums, 0)
        if p >= N-2 or p == 0:
            return False
        q = self._getInd(nums, p, increasing = False)
        if q >= N-1:
            return False
        r = self._getInd(nums, q)
        return r == N