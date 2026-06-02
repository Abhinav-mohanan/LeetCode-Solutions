"""
Problem : Ransom Note
Difficulty : Easy
Link :- https://leetcode.com/problems/ransom-note/

Approach:
- We need to check whether every character in ransomNote can be formed using
    the characters available in magazine.
- Count the frequency of each character present in magazine.
- Traverse each character in ransomNote.
- For every character:
    - Check if it exists in the magazine count.
    - If the character is not available or its count becomes 0,
        we cannot construct the ransom note.
    - Return False.
- Otherwise, use one occurrence of that character by decreasing its count.
- If all characters in ransomNote are successfully matched,
    return True.

Complexity
- Time  : O(n + m)
- Space : O(k)

  n = length of ransomNote
  m = length of magazine
  k = number of distinct characters

"""


from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        counter = Counter(magazine)

        for char in ransomNote:

            if counter[char] <= 0:
                return False
            
            counter[char] -= 1
        
        return True

