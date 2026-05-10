"""
Problem : Contains Duplicate
Difficulty : Easy
Link :- https://leetcode.com/problems/contains-duplicate/

Approach: 
- Use a set to track seen numbers.
- Iterate through the input array `nums`.
- Check if the current number is already in the `seen` set.
  - a duplicate is found, so return True.
  - Otherwise, add the number to the set.
- If the loop finishes without finding duplicates, return False

Complexity
- Time  : O(n)
- space : O(n)

"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
            
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,1]))
    print(sol.containsDuplicate([1,2,3,4]))

