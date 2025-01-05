class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        
        # Start index of the current sliding window
        startInd = 0 
        # Dictionary to store the most recent index of each character
        curWindowCharacters = {}
        
        for endInd, el in enumerate(s):
            # If the character is already been found then start a new window.
            if curWindowCharacters.get(el, -1) >= startInd:
                startInd = curWindowCharacters[el] + 1
            
            # Calculate the length of the current substring and update the answer
            ans = max(ans, endInd - startInd + 1)
            
            # Update the last seen index of the current character
            curWindowCharacters[el] = endInd
        return ans
