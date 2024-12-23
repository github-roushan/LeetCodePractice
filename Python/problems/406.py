from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort the list: first by height in descending order, 
        # then by k in ascending order
        people.sort(key=lambda x: (-x[0], x[1]))

        # Reconstruct the queue based on the sorted list
        for i in range(len(people)):
            if i == people[i][1]:
                continue
            people.insert(people[i][1], people.pop(i))

        return people
