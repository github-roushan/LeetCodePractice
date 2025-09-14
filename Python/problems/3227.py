class Solution:
    def doesAliceWin(self, s: str) -> bool:
        c = sum(1 for el in s if el in "aeiou")
        return c > 0
