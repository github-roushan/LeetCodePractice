from typing import List
from sortedcontainers import SortedList

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisineHeap = defaultdict(lambda : SortedList(key=lambda tp: (-tp[1], tp[0])))
        N = len(foods)
        self.cuisines = cuisines[:]
        self.ratings = ratings[:]
        self.foodIndices = {}
        for i in range(N):
            f, c, r = foods[i], cuisines[i], ratings[i]
            self.foodIndices[f] = i
            self.cuisineHeap[c].add((f, r))

    def changeRating(self, food: str, newRating: int) -> None:
        ind = self.foodIndices[food]
        curRating = self.ratings[ind]
        cuisine = self.cuisines[ind]
        self.cuisineHeap[cuisine].remove((food, curRating))
        self.cuisineHeap[cuisine].add((food, newRating))
        self.ratings[ind] = newRating

    def highestRated(self, cuisine: str) -> str:
        food, rating = self.cuisineHeap[cuisine][0]
        return food

