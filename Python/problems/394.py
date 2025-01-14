class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substring = ""
                while stack and stack[-1] != "[":
                    substring = stack.pop() + substring
                
                stack.pop() ## removed [

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k 
                
                stack.append(int(k) * substring)
        return "".join(stack)