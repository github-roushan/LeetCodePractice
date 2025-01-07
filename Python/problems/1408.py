from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        N = len(words)
        result = []
        for i in range(N):
            for j in range(N):
                if i==j:
                    continue
                if words[i] in words[j]:
                    result.append(words[i])
                    break
        return result