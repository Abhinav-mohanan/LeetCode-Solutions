"""
Problem : Permutation in String
Difficulty : Medium
Link :- https://leetcode.com/problems/permutation-in-string/

Approach:
- We need to check whether s2 contains any substring that is a permutation of s1.
- A permutation means both strings have the same characters with the same frequencies.
- Since the problem contains only lowercase English letters, use two arrays of size 26:
    - One array stores the frequency of characters in s1.
    - Another array stores the frequency of characters in the current window of s2.
- First build the frequency counts for:
    - The entire s1.
    - The first window of s2 having size len(s1).
- Compare both frequency arrays:
    - If they are equal, the first window itself is a valid permutation return True.
- Then start sliding the window through s2:
    - Add the new character entering from the right side.
    - Remove the character leaving from the left side.
    - This keeps the window size fixed at len(s1).
    - After each update:
        - Compare the two frequency arrays.
        - If they are equal, the current window is a permutation of s1 return True.
- If no matching window is found after checking all windows, return False.

Complexity
- Time  : O(n)
- Space : O(1)

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False
        
        s1_counter = [0] * 26
        s2_counter = [0] * 26

        for i in range(len_s1):

            s1_counter[ord(s1[i]) - ord('a')] += 1
            s2_counter[ord(s2[i]) - ord('a')] += 1
        
        if s1_counter == s2_counter:
            return True
        
        for i in range(len_s1, len_s2):

            s2_counter[ord(s2[i]) - ord('a')] += 1
            left_char = s2[i - len_s1]
            s2_counter[ord(left_char) - ord('a')] -= 1

            if s1_counter == s2_counter:
                return True
        
        return False
    

if __name__ == "__main__":

    sol = Solution()

    print(sol.checkInclusion("ab", "eidbaooo"))
    print(sol.checkInclusion("ab", "eidboaoo"))