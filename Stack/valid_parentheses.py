"""
Problem: Valid Parentheses
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Approach:
- Use a stack to keep track of opening brackets.
- Traverse each character in the string.
- If the character is an opening bracket,
    push it onto the stack.
- If the character is a closing bracket:
    - Check whether the stack is empty.
    - Pop the top element from the stack
        and verify it matches the correct opening bracket.
- At the end, the stack should be empty for the string to be valid.

Complexity:
- Time: O(n)
- Space: O(n)

"""

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:

            if char not in bracket_map:
                stack.append(char)

            else:

                if not stack:
                    return False

                top = stack.pop()

                if top != bracket_map[char]:
                    return False

        return len(stack) == 0


if __name__ == "__main__":

    sol = Solution()

    print(sol.isValid("()"))
    print(sol.isValid("()[]{}"))
    print(sol.isValid("(]"))