from itertools import groupby


def minOperationsNeeded(s, L, maxSimilarityThreshold):
    if maxSimilarityThreshold == 1:
        ## total changes if we make s of the work 1010...
        res = sum(int(el) == i%2 for i,el in enumerate(s))
        return min(res, len(s) - res) ## either keep 1010..  or 0101..
        
    return sum(l // (maxSimilarityThreshold + 1) for l in L)

class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        low, high = 1, len(s) + 1
        L = [len(list(arr)) for i, arr in groupby(s)]
        while low < high:
            mid = (low + high) // 2
            if minOperationsNeeded(s, L, mid) > numOps:
                low = mid + 1
            else:
                high = mid
        return low
