from functools import reduce
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda acc, num: acc ^ num, nums)
        