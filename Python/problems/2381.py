from typing import List

# Function to rotate a character by a given number of positions in the alphabet
def rotateChar(ch, rotateBy):
    # Calculate the new character's position using modular arithmetic
    return chr(ord('a') + (ord(ch) - ord('a') + rotateBy) % 26)

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)
        diffs = [0] * (N + 1)  # Array to store the net effect of shifts

        # Process each shift operation
        for start, end, dire in shifts:
            # Convert direction 0 to -1 (indicating left shift)
            if dire == 0:
                dire = -1
            
            # Apply the direction to the diffs array
            diffs[start] += dire
            diffs[end + 1] -= dire

        # Accumulate the net shifts for each character
        for i in range(1, N + 1):
            diffs[i] += diffs[i - 1]

        # Build the resulting string by applying the shifts to each character
        return "".join(rotateChar(el, diffs[i]) for i, el in enumerate(s))
