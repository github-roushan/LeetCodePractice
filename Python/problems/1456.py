class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curWindowVowelCount = 0
        result = 0
        vowels = set("aeiou")
        for ind, el in enumerate(s):
            curWindowVowelCount += el in vowels
            if ind >= k:
                curWindowVowelCount -= s[ind-k] in vowels
            if ind >= k-1:
                result = max(result, curWindowVowelCount)
        return result