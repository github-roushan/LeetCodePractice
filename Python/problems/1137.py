class Solution:
    def tribonacci(self, n: int) -> int:
        trib0, trib1, trib2 = 0, 1, 1
        for _ in range(n):
            trib2, trib1, trib0 = trib2 + trib1 + trib0, trib2, trib1
        return trib0

