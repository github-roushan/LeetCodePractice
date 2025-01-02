from typing import List

def isvowel(char):
    return char in "aeiou" 

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        N = len(words)
        prefix = [0]*(N+1)
        for i in range(N):
            prefix[i+1] = prefix[i]
            if isvowel(words[i][0]) and isvowel(words[i][-1]):
                prefix[i+1] += 1
    
        result = []
        for l,r in queries:
            result.append(prefix[r+1] - prefix[l])
        return result