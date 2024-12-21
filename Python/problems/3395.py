from collections import Counter
from typing import List

MOD = 10**9 + 7
LIM = 1000 + 1

f = [1]*LIM
for i in range(1, LIM):
    f[i] = f[i-1] * i % MOD

def C(n, r):
    if r > n or r < 0 or n <0:
        return 0
    num = f[n]
    den = f[r] * f[n-r]
    den = pow(den, MOD-2, MOD)
    num = num * den % MOD
    return num

class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        fullCounter = Counter(nums)
        leftCounter = Counter()
        rightCounter = Counter(nums)
        numLen = len(nums)
        total = 0

        leftSingleSum, leftPairSum = 0, 0
        rightSingleSum, rightPairSum = 0, 0
        for fre in rightCounter.values():
            rightPairSum += fre * rightSingleSum
            rightSingleSum += fre

        for ind, el in enumerate(nums):
            ## adjust right values
            rightPairSum -= rightSingleSum - rightCounter[el]
            rightSingleSum -= 1
            rightCounter[el] -= 1

            l = leftCounter[el]
            r = rightCounter[el]
            leftSize = ind
            rightSize = numLen - ind - 1

            # m, m, m, m, m
            total += C(l,2) * C(r,2) % MOD
            total %= MOD

            # a, m, m, m, m
            total += (leftSize - l) * l * C(r, 2) % MOD
            total %= MOD

            # m, m, m, m, b
            total += C(l, 2) * r * (rightSize - r) % MOD
            total %= MOD

            # a, m, m, m, b
            total += (leftSize - l) * l * r * (rightSize - r) % MOD
            total %= MOD

            # a, b, m, m, m
            total += C(leftSize - l, 2) * C(r, 2) % MOD
            total %= MOD

            # m, m, m, a, b
            total += C(l, 2) * C(rightSize - r, 2) % MOD
            total %= MOD

            # a, m, m, b, c
            for a, afre in leftCounter.items():
                if a == el:
                    continue
                maExcSingleSum = rightSingleSum - (rightCounter[a] + rightCounter[el])
                maExcPairSum = rightPairSum - maExcSingleSum * (rightCounter[a] + rightCounter[el]) - rightCounter[a] * rightCounter[el]
                # maExcTripletSum = rightTripletSum - maExcPairSum * (rightCounter[a] + rightCounter[el]) - rightCounter[a] * rightCounter[el] * maExcSingleSum

                total += afre * l * maExcPairSum % MOD

            # a, b, m, m, c
            for c, cfre in rightCounter.items():    
                if c == el:
                    continue
                mcExcSingleSum = leftSingleSum - (leftCounter[c] + leftCounter[el])
                mcExcPairSum = leftPairSum - mcExcSingleSum * (leftCounter[c] + leftCounter[el]) - leftCounter[c] * leftCounter[el]
                # mcExcTripletSum = leftTripletSum - mcExcPairSum * (leftCounter[c] + leftCounter[el]) - leftCounter[c] * leftCounter[el] * mcExcSingleSum

                total += r * cfre * mcExcPairSum % MOD
            
            # adjust left values
            leftPairSum += leftSingleSum - leftCounter[el]
            leftSingleSum += 1
            leftCounter[el] += 1

        return total 
