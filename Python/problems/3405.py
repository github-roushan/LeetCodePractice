MOD = 10**9 + 7
LIM = 10**5+1

factorial = [1]*LIM
for i in range(2, LIM):
    factorial[i] = i * factorial[i-1] % MOD
    
def C(N, R):
    if N < 0 or R > N:
        return 0
    den = factorial[R] * factorial[N-R] % MOD
    res = factorial[N] * pow(den, MOD-2, MOD) % MOD
    return res

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        res = C(n-1, k) * m * pow(m-1, n-k-1, MOD) % MOD
        return res