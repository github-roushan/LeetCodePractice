from typing import List


class Solution:
    @staticmethod
    def makeFancyString(s: str) -> str:
        result: List[str] = []
        prev_char: str | None = None
        run_length = 0

        for ch in s:
            if ch == prev_char:
                run_length += 1
            else:
                prev_char = ch
                run_length = 1

            if run_length < 3:
                result.append(ch)

        return "".join(result)