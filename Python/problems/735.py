from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            keepAsteroid = True
            while stack and stack[-1] > 0 and ast < 0 and keepAsteroid:
                if stack[-1] > abs(ast):
                    keepAsteroid = False
                elif stack[-1] == abs(ast):
                    stack.pop()
                    keepAsteroid = False
                else:
                    stack.pop()
            if keepAsteroid:
                stack.append(ast)
        return stack