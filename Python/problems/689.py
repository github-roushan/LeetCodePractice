from typing import List, Tuple
from functools import lru_cache
from itertools import accumulate


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Compute the prefix sum for efficient subarray sum calculations
        prefixSum = [0] + list(accumulate(nums))
        numElements = len(nums)
        
        @lru_cache(None)
        def maximizeSum(index: int, remainingSubarrays: int) -> Tuple[int, List[int]]:
            # Base case: If no subarrays left or index out of bounds
            if index >= numElements or remainingSubarrays == 0:
                return 0, []
            
            # Invalid case: When there's not enough space for a subarray
            if index + k > len(prefixSum) - 1:
                return 0, []

            # Calculate the sum of the current subarray
            currentSubarraySum = prefixSum[index + k] - prefixSum[index]

            # Option 1: Include the current subarray and the next remaining subarrays
            includedSum, includedIndices = maximizeSum(index + k, remainingSubarrays - 1)

            # Option 2: Skip the current index
            skippedSum, skippedIndices = maximizeSum(index + 1, remainingSubarrays)

            # Determine the better option
            if currentSubarraySum + includedSum >= skippedSum and len(includedIndices) == remainingSubarrays - 1:
                return currentSubarraySum + includedSum, [index] + includedIndices
            
            return skippedSum, skippedIndices

        # Start the dynamic programming process for 3 subarrays
        return maximizeSum(0, 3)[1]
