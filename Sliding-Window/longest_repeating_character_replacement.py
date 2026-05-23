"""
Problem: Longest Repeating Character Replacement
Difficulty: Medium
Link: https://leetcode.com/problems/longest-repeating-character-replacement/

Approach:
- Use the Sliding Window technique with two pointers.
- Keep a hashmap to count character frequencies
    inside the current window.
- Track the count of the most frequent character
    in the window.
- If the number of characters to replace
    (window size - max frequency) becomes greater than k:
        - Shrink the window from the left side.
- Update the maximum valid window length during traversal.

Complexity:
- Time: O(n)
- Space: O(n)

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}

        left = 0
        max_freq = 0
        longest = 0

        for right in range(len(s)):

            count[s[right]] = count.get(s[right], 0) + 1

            max_freq = max(max_freq, count[s[right]])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest


if __name__ == "__main__":

    sol = Solution()

    print(sol.characterReplacement("ABAB", 2))
    print(sol.characterReplacement("AABABBA", 1))