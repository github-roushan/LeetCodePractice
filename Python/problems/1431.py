from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        result = []
        for candy in candies:
            if candy + extraCandies >= mx:
                result.append(True)
            else:
                result.append(False)
        return result