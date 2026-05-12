"""
Problem: Group Anagrams
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/

Approach:
- Initialize a hashmap to group anagrams.
- For each word:
    - Create a frequency array of size 26 to count characters.
    - Use each character's position (a-z) to update the count.
    - Convert the frequency array into a tuple so it can be used
      as a hashmap key.
- Words with the same character frequency will share the same key,
  meaning they are anagrams.
- Append each word to its corresponding group.
- Return all grouped anagrams.

Complexity:
- Time: O(n * k)
- Space: O(n * k)

Where:
- n = number of words
- k = maximum length of a word

"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:
            char_count  = [0] * 26

            for c in word:
                char_count [ord(c) - ord('a')] += 1
            
            key = tuple(char_count)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        return list(groups.values())

if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

