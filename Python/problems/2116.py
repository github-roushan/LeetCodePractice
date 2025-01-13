class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False

        openB = [] ## open and locked
        unlocked = [] ## unlocked, can be anything

        for i,el in enumerate(s):
            if locked[i] == "0":
                unlocked.append(i)
            elif el == "(":
                openB.append(i)
            elif el == ")":
                if openB:
                    openB.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while openB and unlocked and openB[-1] < unlocked[-1]:
            openB.pop()
            unlocked.pop()
        
        return len(openB) == 0
