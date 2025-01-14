from typing import List

def getMaxContinous(lis):
    cont = [0]
    c = 0
    for el in lis:
        if el == 0:c = 0
        else:c += 1
        cont.append(c)
    return cont

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        pref = getMaxContinous(nums)[:-1]
        suff = getMaxContinous(nums[-1::-1])[-2::-1]
        ans = max(*pref, *suff)
        for i,el in enumerate(nums):
            if el == 1:
                continue
            ans = max(pref[i] + suff[i], ans)
        return ans