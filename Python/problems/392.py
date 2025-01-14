class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ## find element in s by sliding in t
        curSind = 0
        curTind = 0
        while curTind < len(t) and curSind < len(s):
            if t[curTind] == s[curSind]:
                curSind += 1
            curTind += 1
        return curSind == len(s)