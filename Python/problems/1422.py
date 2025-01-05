class Solution:
    def maxScore(self, s: str) -> int:
        # Count of '0's in the left substring
        zero = 0

        # count of '1's in the right substring
        ones = s.count("1")

        ans = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                # Increment '0' count for the left substring
                zero += 1  
            else:
                # Decrement '1' count for the right substring
                ones -= 1  

            ans = max(ans, zero + ones)
        return ans
