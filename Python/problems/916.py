from typing import List
from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        lcmB = Counter()
        for word in words2:
            curCounter = Counter(word)
            for k,v in curCounter.items():
                lcmB[k] = max(lcmB[k], v)
        
        result = []
        for word in words1:
            curCounter = Counter(word)
            isUniversal = True
            for k,v in lcmB.items():
                if v > curCounter[k]:
                    isUniversal = False
                    break
            if isUniversal:
                result.append(word)
        return result