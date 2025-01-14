from collections import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = set()
        b = set()

        C = []
        for i in range(len(A)):
            a.add(A[i])
            b.add(B[i])
            C.append(len(a.intersection(b)))
        return C