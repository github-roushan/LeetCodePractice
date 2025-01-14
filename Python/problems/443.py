from typing import List

def getCharRep(char, count):
    li = [char]
    if count > 1:
        li.extend(list(str(count)))
    return li

class Solution:
    def compress(self, chars: List[str]) -> int:
        prevChar = chars[0]
        fre = 0
        compSize = 0
        for char in chars:
            if char == prevChar:
                fre += 1
            else:
                compChar = getCharRep(prevChar, fre)
                chars[compSize: compSize + len(compChar)] = compChar
                compSize += len(compChar)
                prevChar = char
                fre = 1

        compChar = getCharRep(prevChar, fre)
        chars[compSize: compSize + len(compChar)] = compChar
        compSize += len(compChar)
        return compSize