MOD = 10**9 + 7
LIM = 10**5 + 2

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

fact = Factorial(LIM, MOD)
class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        totalMan = 0
        ## C(M-2, k-2) * (n^2 * C(m+1, 3) + m^2 * C(n+1, 3))
        totalMan = pow(n, 2, MOD) * fact.combi(m+1, 3) % MOD
        totalMan = ( totalMan + pow(m, 2, MOD) * fact.combi(n+1, 3) ) % MOD
        totalMan = fact.combi(m*n-2, k-2) * totalMan % MOD

        return totalMan
