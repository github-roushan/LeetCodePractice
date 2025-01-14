from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        return [cur.bit_count() for cur in range(n+1)]