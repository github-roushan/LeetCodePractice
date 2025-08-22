class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        countContZero = 0
        total = 0
        for el in nums:
            if el == 0:
                countContZero += 1
            else:
                if countContZero:
                    total += countContZero * (countContZero + 1) // 2
                countContZero = 0
        
        if countContZero:
            total += countContZero * (countContZero + 1) // 2
        return total