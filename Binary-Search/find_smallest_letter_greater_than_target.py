"""
Problem : Find Smallest Letter Greater Than Target
Difficulty : Easy
Link : https://leetcode.com/problems/find-smallest-letter-greater-than-target/

Approach:
- Since the letters array is sorted, use Binary Search.
- Find the first character that is strictly greater than the target.
- If such a character exists, return it.
- If no character is greater than the target, return the first character
  because the letters wrap around.

Complexity
- Time  : O(log n)
- Space : O(1)

"""


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:

        left = 0
        right = len(letters) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        return letters[left] if left < len(letters) else letters[0]


if __name__ == "__main__":

    sol = Solution()

    print(sol.nextGreatestLetter(["c","f","j"], "a"))
    print(sol.nextGreatestLetter(["c","f","j"], "c"))
    print(sol.nextGreatestLetter(["x","x","y","y"], "z"))