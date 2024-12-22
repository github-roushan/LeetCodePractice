from collections import defaultdict
from typing import List

LIM = 5 * 10**4 + 1  # Maximum range limit

class SegTree:

    def __init__(self):
        self.tree = [float("inf")] * (4 * LIM)  # Initialize segment tree with infinity

    def update(self, index, value):
        """Update the segment tree with a new value at a specific index."""
        ss, se, si = 0, LIM - 1, 0  # Segment start, end, and current index
        while ss < se:
            self.tree[si] = min(self.tree[si], value)
            mid = (ss + se) // 2
            if index <= mid:
                si = 2 * si + 1
                se = mid
            else:
                ss = mid + 1
                si = 2 * si + 2
        self.tree[si] = min(self.tree[si], value)

    def rangeHelper(self, ss, se, si, left, right):
        """Recursively find the minimum value in a range."""
        if left <= ss and se <= right:  # Range completely within bounds
            return self.tree[si]
        if se < left or right < ss:  # Range completely outside bounds
            return float("inf")

        mid = (ss + se) // 2
        left_min = self.rangeHelper(ss, mid, 2 * si + 1, left, right)
        right_min = self.rangeHelper(mid + 1, se, 2 * si + 2, left, right)
        return min(left_min, right_min)

    def rangeMin(self, left, right):
        """Get the minimum value in the specified range."""
        return self.rangeHelper(0, LIM - 1, 0, left, right)

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], tasks: List[List[int]]) -> List[int]:
        # Group indices by heights
        height_map = defaultdict(list)
        for i, h in enumerate(heights):
            height_map[h].append(i)

        # Normalize heights to sorted keys
        sorted_keys = sorted(height_map.keys())
        for i, key in enumerate(sorted_keys):
            for index in height_map[key]:
                heights[index] = i

        # Group tasks by their max and min bounds
        task_map = defaultdict(lambda: defaultdict(list))
        for index, (x, y) in enumerate(tasks):
            lower, upper = min(x, y), max(x, y)
            task_map[upper][lower].append(index)

        sorted_task_keys = sorted(task_map.keys(), reverse=True)
        hind = len(heights) - 1
        seg_tree = SegTree()
        results = [-1] * len(tasks)

        for upper in sorted_task_keys:
            # Update segment tree for heights up to the current upper bound
            while hind >= upper:
                seg_tree.update(heights[hind], hind)
                hind -= 1

            for lower, indices in task_map[upper].items():
                # Resolve each task using the segment tree
                current_result = -1
                if lower == upper or heights[lower] < heights[upper]:
                    current_result = upper
                else:
                    max_height = max(heights[lower], heights[upper]) + 1
                    current_result = seg_tree.rangeMin(max_height, LIM - 1)
                    if current_result == float("inf"):
                        current_result = -1

                for result_index in indices:
                    results[result_index] = current_result

        return results
