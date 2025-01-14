class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        li = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            li.append(word1[i])
            li.append(word2[j])
            i+=1
            j+=1
        
        return "".join(li) + word1[i:] + word2[j:]