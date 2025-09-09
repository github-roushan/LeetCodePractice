MOD = 10**9 + 7
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        dp_window_sum = 0
        for d in range(2, n+1):
            if d-delay >= 0:
                dp_window_sum += dp[d - delay]
            if d-forget >= 0:
                dp_window_sum -= dp[d-forget]
            dp[d] += dp_window_sum
            dp[d] %= MOD
            
        return sum(dp[n-forget+1:]) % MOD

