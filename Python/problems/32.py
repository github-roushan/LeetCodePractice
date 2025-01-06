class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        result = 0
        for i,el in enumerate(s):
            if stack and stack[-1][0] == "(" and el == ")":
                stack.pop()
            else:
                stack.append((el, i))
            
            if stack:
                result = max(result, i - stack[-1][1])
            else:
                result = max(result, i+1)
        return result