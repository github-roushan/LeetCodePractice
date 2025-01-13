from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        final = 0
        for k,v in c.items():
            final += 1
            if v%2 == 0:
                final += 1
        return final
