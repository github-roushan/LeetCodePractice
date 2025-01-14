from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        high = len(s)
        if k > high:
            return False
        if k == high:
            return True
        c = Counter(s)
        low = sum(1 for v in c.values() if v%2)

        return low <= k