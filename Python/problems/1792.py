from typing import List
from sortedcontainers import SortedList


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        s = SortedList(classes, key = lambda tp: (tp[1] - tp[0])/(tp[1] * (tp[1] + 1)))
        while extraStudents:
            cur_class = s.pop() ## top element from maxheap
            cur_class[0] += 1
            cur_class[1] += 1

            s.add(cur_class)
            extraStudents -= 1

        sum_pass_ratio = 0
        while s:
            tp = s.pop()
            sum_pass_ratio += tp[0]/tp[1]
        return sum_pass_ratio / len(classes)