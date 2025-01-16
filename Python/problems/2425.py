from functools import reduce
from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        xor1, xor2 = 0, 0
        if m%2:
            xor1 = reduce(lambda acc, num: acc ^ num, nums1)
        if n%2:
            xor2 = reduce(lambda acc, num: acc ^ num, nums2)
        
        return xor1 ^ xor2