from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        cur_start, cur_end = 0, -1
        result = []
        for s,e in sorted(intervals):
            if s <= cur_end:
                cur_end = max(cur_end, e)
            else:
                if cur_start <= cur_end:
                    result.append((cur_start, cur_end))
                cur_start, cur_end = s, e
            
        if cur_start <= cur_end:
            result.append((cur_start, cur_end))
        
        return result
    