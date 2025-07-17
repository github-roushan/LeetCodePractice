from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # Initialize the DP table: dp[mod][rem] stores the max subsequence length
        # ending with mod value `mod` and total remainder `rem`
        dp = [[-1] * k for _ in range(k)]

        for num in nums:
            current_mod = num % k
            next_dp = [-1] * k
            next_dp[current_mod] = 1  # Start new subsequence with this number

            for remainder in range(k):
                required = (remainder - current_mod) % k
                if dp[required][remainder] == 0:
                    next_dp[remainder] = 2  # Start a pair
                else:
                    next_dp[remainder] = 1 + dp[required][remainder]  # Extend sequence

            # Update dp table with the best values
            for remainder in range(k):
                dp[current_mod][remainder] = max(dp[current_mod][remainder], next_dp[remainder])

        # Find the overall maximum length across the DP table
        return max(max(row) for row in dp)
