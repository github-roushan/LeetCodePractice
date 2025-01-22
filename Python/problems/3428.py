from typing import List


class Factorial:
    def __init__(self, N, mod) -> None:
        N += 1
        self.mod = mod
        self.f = [1 for _ in range(N)]
        self.g = [1 for _ in range(N)]
        for i in range(1, N):
            self.f[i] = self.f[i - 1] * i % self.mod
        self.g[-1] = pow(self.f[-1], mod - 2, mod)
        for i in range(N - 2, -1, -1):
            self.g[i] = self.g[i + 1] * (i + 1) % self.mod

    def combi(self, n, m):
        if n < m or m < 0 or n < 0: return 0
        return self.f[n] * self.g[m] % self.mod * self.g[n - m] % self.mod

mod = 10 ** 9 + 7
f = Factorial(10 ** 5 + 1000, mod)

pre = [[0] * (10 ** 5 + 1) for _ in range(101)]
for i in range(101):
    for j in range(10 ** 5 + 1):
        pre[i][j] = pre[i - 1][j] + f.combi(j, i)
        pre[i][j] %= mod

class Solution:
    def minMaxSums(self, nums: List[int], v: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        
        for i in range(n):
            ans += (pre[v - 1][i] + pre[v - 1][n - i - 1]) * nums[i] % mod
        return ans % mod