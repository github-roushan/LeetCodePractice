class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = list(filter(lambda word: word != "", s.split(" ")))
        return " ".join(reversed(wordList))
