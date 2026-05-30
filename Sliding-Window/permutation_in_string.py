"""
Problem : Permutation in String
Difficulty : Medium
Link :- https://leetcode.com/problems/permutation-in-string/

Approach:
- We need to check whether any substring of s2 is a permutation of s1.
- A permutation means both strings contain the same characters with the same frequencies.
- Create a frequency count for all characters in s1.
- The right pointer moves:
    - Add the current character to the window frequency count.
    - If the window size becomes larger than len(s1):
        - Decrease the char count
        - If the char count is '0' Remove the leftmost character from the window.
        - Move the left pointer forward.
- This keeps the window size fixed at len(s1).
- After every update:
    - Compare the window frequency count with the frequency count of s1.
    - If both counts are equal the current window is a permutation of s1 return True.
- If we finish traversing s2 without finding a match return False.

Complexity
- Time  : O(n * k) [ k is number of distinct characters '26' ]
- Space : O(1)

"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_counter = Counter(s1)
        s2_counter = Counter()
        left = 0

        for right in range(len(s2)):

            s2_counter[s2[right]] += 1

            if (right - left) + 1 > len(s1):
                
                left_char = s2[left]
                s2_counter[left_char] -= 1

                if s2_counter[left_char] == 0:
                    del s2_counter[left_char]

                left += 1
            
            if s1_counter == s2_counter:
                return True
        
        return False

if __name__ == "__main__":
    
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))
    print(sol.checkInclusion("ab", "eidboaoo"))