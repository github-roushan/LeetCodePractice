# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

def guess(num: int, lim = 100, guessNumber = None) -> int:
    if guessNumber == None:
        import random
        guessNumber = random.randint(1, lim)
    if num > guessNumber:
        return -1
    if num == guessNumber:
        return 0
    if num < guessNumber:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        lowGuess, highGuess = 1, n
        while lowGuess < highGuess:
            midGuess = (lowGuess + highGuess + 1) // 2
            guessResult = guess(midGuess)
            if guessResult == 1:
                lowGuess = midGuess
            elif guessResult == 0:
                return midGuess
            else:
                highGuess = midGuess - 1
        return lowGuess
