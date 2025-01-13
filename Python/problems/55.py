from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canJumpUpto = 0
        for i, j in enumerate(nums):
            if i > canJumpUpto:
                return False
            canJumpUpto = max(canJumpUpto, i + j)
        return True