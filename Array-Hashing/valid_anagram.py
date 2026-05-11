"""
Problem : Valid Anagram
Difficulty : Easy
Link :- https://leetcode.com/problems/valid-anagram/

Approach:
- If the lengths are not equal, they cannot be anagrams.
- Use a hash map to count character frequencies from the first string.
- Iterate through the second string:
  - If the character does not exist or count becomes zero,
    return False.
  - Otherwise, decrease the count.
- If all checks pass, return True.

Complexity
- Time  : O(n)
- Space : O(n)

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        char_map = {}

        for char in s:
            char_map[char] = char_map.get(char, 0) + 1

        for char in t:
            if char not in char_map or char_map[char] == 0:
                return False
            
            char_map[char] -= 1

        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))
    print(sol.isAnagram("rat", "car"))