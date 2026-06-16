"""
Problem : Process String with Special Operations I
Difficulty : Medium
Link :- https://leetcode.com/problems/process-string-with-special-operations-i/

Approach:
- Process the string from left to right.
- Maintain a result string that gets updated after each character.
- For each character:
    - If it is a lowercase letter:
        - Append it to the result.
    - If it is '*':
        - Remove the last character from the result if it exists.
    - If it is '#':
        - Duplicate the current result and append it to itself.
    - If it is '%':
        - Reverse the current result.
- After processing all characters, return the final result.

Complexity
Time  : O(2^n)
Space : O(2^n)

"""


class Solution:
    def processStr(self, s: str) -> str:

        result = []

        for char in s:

            if char.isalpha():

                result.append(char)

            elif char == "*":

                if result:
                    result.pop()

            elif char == "#":

                result.extend(result)

            elif char == "%":

                result.reverse()

        return "".join(result)


if __name__ == "__main__":

    solution = Solution()

    print(solution.processStr("a#b%*"))
    print(solution.processStr("z*#"))