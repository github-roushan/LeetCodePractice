from typing import List
from collections import Counter


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        windowCounter = Counter(nums)
        needToRemove = set(el for el, v in windowCounter.items() if v >= 2)
        operationsDoneSoFar = 0
        windowHeadIndex = 0

        while needToRemove:
            operationsDoneSoFar += 1

            for i in range(windowHeadIndex, min(len(nums),windowHeadIndex+3)):
                ## remove nums[i], shring the window from left
                windowCounter[nums[i]] -= 1

                if windowCounter[nums[i]] == 1:
                    ## we have removed all but one occurance of nums[i]
                    needToRemove.remove(nums[i])
            if len(needToRemove) == 0:
                break
            windowHeadIndex = i+1
        return operationsDoneSoFar