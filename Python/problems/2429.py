from collections import deque

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        oneBitsList = []
        zeroedBitsQueue = deque()

        curBitPos = 0
        while num1:
            if num1 & 1:
                oneBitsList.append(1 << curBitPos)
            else:
                zeroedBitsQueue.append(1 << curBitPos)
            curBitPos += 1
            num1 >>= 1
        
        setBitsNum2 = num2.bit_count()
        maxBit = oneBitsList[-1] if oneBitsList else 1
        result = 0

        while setBitsNum2 and oneBitsList:
            result |= oneBitsList.pop()
            setBitsNum2 -= 1
        
        while setBitsNum2 and zeroedBitsQueue:
            result |= zeroedBitsQueue.popleft()
            setBitsNum2 -= 1
        
        while setBitsNum2:
            maxBit <<= 1
            setBitsNum2 -= 1
            result |= maxBit
        
        return result