from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxResult = 0
        N = len(height)
        i, j = 0, N-1
        while i < j:
            ## find the area here
            h = min(height[i], height[j])
            curResult = (j - i) * h
            maxResult = max(maxResult, curResult)
            if h == height[i]:
                i += 1
            else:
                j -= 1
        return maxResult
