import collections
import string
import bisect


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        f = collections.defaultdict(lambda : -1)
        l = collections.defaultdict(lambda : -1)
        seenAt = collections.defaultdict(list)
        for ind, el in enumerate(s):
            if el not in f:
                f[el] = ind
            seenAt[el].append(ind)
            l[el] = ind
        
        ans = 0
        for alpha in string.ascii_lowercase:
            if f[alpha] == -1:
                continue
            s, e = f[alpha], l[alpha]
            for midAlpha in string.ascii_lowercase:
                ind = bisect.bisect_right(seenAt[midAlpha], s)
                if ind >= len(seenAt[midAlpha]):
                    continue
                if s < seenAt[midAlpha][ind] < e:
                    ans += 1
        return ans