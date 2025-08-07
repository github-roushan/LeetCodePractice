from itertools import accumulate
from typing import List, Tuple
import enum

class Trend(enum.Enum):
    EQUAL = "E"
    INCREASING = "I"
    DECREASING = "D"
    SAME = "S"

class Solution:
    def _get_range(self, nums: List[int], start: int) -> Tuple[int, int, str]:
        n = len(nums)
        if start >= n - 1:
            return (n, n, Trend.EQUAL)

        end = start
        if nums[start] == nums[start + 1]:
            trend = Trend.SAME
            while end + 1 < n and nums[end + 1] == nums[start]:
                end += 1
        elif nums[start] < nums[start + 1]:
            trend = Trend.INCREASING
            while end + 1 < n and nums[end] < nums[end + 1]:
                end += 1
        else:
            trend = Trend.DECREASING
            while end + 1 < n and nums[end] > nums[end + 1]:
                end += 1

        return (start, end, trend)

    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = list(accumulate(nums, initial=0))

        result = float("-inf")
        prev_prev_range = prev_range = None
        good_ranges = []
        index = 0

        # Identify good ranges
        START = 0
        END = 1
        TREND = 2
        while index < n:
            current_range = self._get_range(nums, index)

            if (prev_prev_range and prev_prev_range[TREND] == Trend.INCREASING and
                prev_range and prev_range[TREND] == Trend.DECREASING and
                current_range[TREND] == Trend.INCREASING):
                good_ranges.append((prev_prev_range, current_range))

            index = current_range[END]
            prev_prev_range, prev_range = prev_range, current_range

        # Calculate max sum for each good range
        for first, last in good_ranges:
            s1, e1 = first[START], first[END]
            s2, e2 = last[START], last[END]

            # Sum positive tail of the first range
            left_sum = nums[e1 - 1]
            for i in range(e1 - 2, s1 - 1, -1):
                if nums[i] <= 0:
                    break
                left_sum += nums[i]

            # Combine with right side
            for j in range(s2 + 1, e2 + 1):
                total = prefix_sum[j + 1] - prefix_sum[e1] + left_sum
                result = max(result, total)

        return result