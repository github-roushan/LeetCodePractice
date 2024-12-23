from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        last_used_num = float("-inf")
        total_distinct_nums = 0
        
        # Sort the input list to process elements in ascending order
        for num in sorted(nums):
            # Determine the smallest value within the valid range [num - k, num + k] 
            # that can be used while maintaining distinctiveness
            candidate = max(last_used_num + 1, num - k)
            
            # Skip if the candidate exceeds the upper limit of the range
            if candidate > num + k:
                continue
            
            # Update the last used number and increment the count of distinct elements
            last_used_num = candidate
            total_distinct_nums += 1
        
        return total_distinct_nums