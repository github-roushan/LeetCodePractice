from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 0:
            return 0
        prevChar = flowerbed[0]
        count = 1
        possiblePlantation = 0
        for el in flowerbed:
            if prevChar == el:
                count += 1
            else:
                possiblePlantation += (prevChar == 0) * (count - 1) // 2
                count = 1
                prevChar = el

        possiblePlantation += (prevChar == 0) * (count) // 2
        return possiblePlantation >= n