class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for el in s:
            if el == "*":
                stack.pop()
            else:
                stack.append(el)
        return "".join(stack)