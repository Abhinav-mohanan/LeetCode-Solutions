"""
Problem : Two Sum II - Input Array Is Sorted
Difficulty : Medium
Link :- https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Approach:
- Initialize a 'left' pointer at the beginning and
    a 'right' pointer at the end of the array.
- Calculate the sum of the elements at these two pointers 
    ('total = numbers[left] + numbers[right]')
- Check the calculated sum against the target:
    - If 'total == target', we found the answer. 
        Return the 1-based indices: '[left + 1, right + 1]'.
    - If the sum is small, move the 'left' pointer forward.
    - If the sum is large. move the 'right' pointer backward.
- Repeat the process until the target pair is found.

Complexity
- Time  : O(n)
- space : O(1)

"""
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            
            if total < target:
                left += 1
            else:
                right -= 1
    
if __name__ == "__main__":
    sol = Solution()

    print(sol.twoSum([2, 7, 11, 15], 9))
    print(sol.twoSum([2, 3, 4], 6))

