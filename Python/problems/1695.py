from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """Return the maximum score of a contiguous subarray with all unique elements.

        Args:
            nums: List of integers representing the array.

        Returns:
            The maximum sum obtainable from any subarray that contains only unique values.
        """
        last_seen: dict[int, int] = {}
        current_sum = 0
        left = 0  # Left boundary of the sliding window
        max_score = 0

        for right, value in enumerate(nums):
            current_sum += value

            # If the value is already within the current window, shrink the window
            # to exclude its previous occurrence.
            if value in last_seen and last_seen[value] >= left:
                duplicate_index = last_seen[value]
                while left <= duplicate_index:
                    current_sum -= nums[left]
                    left += 1

            # Record the most recent index of the current value.
            last_seen[value] = right
            max_score = max(max_score, current_sum)

        return max_score