"""
Problem : Group Anagrams
Difficulty : Medium
Link :- https://leetcode.com/problems/group-anagrams/

Approach:
- Initialize a hashmap to group anagrams
- Iterate through each word in the input list.
  - Sort the word and use it as the hashmap key.
  - If the key already exists, append the word.
  - Otherwise, create a new list with the word.
- Return all grouped anagrams

Complexity
- Time  : O(n * k log k)
- Space : O(n * k)

"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:
            key = ''.join(sorted(word))
            
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        return list(groups.values())

if __name__ == '__main__':
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(sol.groupAnagrams([""]))


