from typing import List
from sortedcontainers import SortedList


class Solution:
    def maxFreeTime(self, eventTime: int, S: List[int], E: List[int]) -> int:
        total_events = len(S)
        max_free = 0
        last_end = 0
        gaps: List[int] = []
        for i in range(total_events):
            gaps.append(S[i] - last_end)
            last_end = E[i]

        # Gap after the last event.
        gaps.append(eventTime - last_end)

        # Balanced search trees for fast lower-bound queries.
        left_gaps = SortedList()
        right_gaps = SortedList(gaps[1:])

        for i in range(total_events):
            if i > 0:
                left_gaps.add(gaps[i - 1])
            right_gaps.remove(gaps[i + 1])

            # Case 1: keep the event in its current position.
            max_free = max(max_free, gaps[i] + gaps[i + 1])

            # Case 2: attempt to move the event into another gap.
            duration = E[i] - S[i]

            idx = left_gaps.bisect_left(duration)
            if idx < len(left_gaps):
                max_free = max(max_free, gaps[i] + gaps[i + 1] + duration)
                continue

            idx = right_gaps.bisect_left(duration)
            if idx < len(right_gaps):
                max_free = max(max_free, gaps[i] + gaps[i + 1] + duration)

        return max_free
