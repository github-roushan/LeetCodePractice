from typing import Counter, List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        numsCounter = Counter()
        totalOperations = 0
        for el in nums:
            if k - el in numsCounter:
                totalOperations += 1
                numsCounter[k - el] -= 1
                if numsCounter[k - el] == 0:
                    del numsCounter[k - el]
            else:
                numsCounter[el] += 1
        return totalOperations
