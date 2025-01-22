from typing import List


class MyIterator:
    def __init__(self, nums):
        self.container = nums
        self.Rows = len(self.container)
        self.Cols = len(self.container[0])

    def __iter__(self):
        self.curRow = 0
        self.curCol = 0
        return self
    
    def __next__(self):
        if self.curRow == self.Rows:
            raise StopIteration
        el = self.container[self.curRow][self.curCol]
        if self.curRow % 2 == 0:
            if self.curCol == self.Cols-1:
                self.curRow += 1
            else:
                self.curCol += 1
        else:
            if self.curCol == 0:
                self.curRow += 1
            else:
                self.curCol -= 1
        return el

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        myIter = MyIterator(grid)
        return [el for i, el in enumerate(myIter) if i%2==0]
        