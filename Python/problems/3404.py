from typing import List
from collections import Counter
from math import gcd


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        totalSubsequences = 0
        rightCounter = Counter()
        N = len(nums)
        
        for i in range(1, N):
            for j in range(i+2, N):
                d = gcd(nums[i], nums[j])
                tup = nums[j]//d, nums[i]//d
                rightCounter[tup] += 1
     
        for j in range(N):
            for r in range(j+3, N):
                d = gcd(nums[j+1], nums[r])
                tup = nums[r]//d, nums[j+1]//d
                rightCounter[tup] -= 1
            
            for i in range(j-1):
                d = gcd(nums[i], nums[j])
                tup = nums[i]//d, nums[j]//d
                totalSubsequences += rightCounter[tup]
        
        return totalSubsequences