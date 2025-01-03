from typing import List


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        N = len(word)
        sizeofWord = N - numFriends + 1
        return max(word[i:i+sizeofWord] for i in range(N))