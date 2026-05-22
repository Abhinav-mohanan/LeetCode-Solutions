"""
Problem: Longest Substring Without Repeating Characters
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Approach:
- Use the Sliding Window technique with two pointers.
- Keep a set to track characters currently inside the window.
- Expand the right pointer to add new characters.
- If a duplicate character is found:
    - Remove characters from the left side
        until the duplicate is removed.
- Update the maximum substring length after
    each valid window expansion.
- Continue until the right pointer reaches
    the end of the string.

Complexity:
- Time: O(n)
- Space: O(n)

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()

        left = 0
        longest = 0

        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            longest = max(longest, right - left + 1)

        return longest


if __name__ == "__main__":

    sol = Solution()

    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbb"))
    print(sol.lengthOfLongestSubstring("pwwkew"))