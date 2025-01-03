from typing import List


def countNonOverlapping(rangeList):
    rangeList.sort()
    prevEnd = rangeList[0][1]
    totalRanges = 1
    for curStart, curEnd in rangeList:
        if prevEnd <= curStart:
            prevEnd = curEnd
            totalRanges += 1
        else:
            prevEnd = max(prevEnd, curEnd)        
    return totalRanges

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        horRanges = []
        verRanges = []
        for startx, starty, endx, endy in rectangles:
            horRanges.append((startx, endx))
            verRanges.append((starty, endy))
        
        return countNonOverlapping(horRanges) >= 3 or countNonOverlapping(verRanges) >= 3