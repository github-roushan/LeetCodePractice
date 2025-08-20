from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda tp: tp[0]**2 + tp[1]**2)
        return points[:k]