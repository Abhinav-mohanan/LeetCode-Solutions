"""
Problem : Binary Search
Difficulty : Easy
Link :- https://leetcode.com/problems/binary-search/

Approach:
- Use two pointers : 
    'left' at the beginning and 'right' at the end of the array.
- While the left <= right 
    - Find the middle element.
    - Compare the value at 'mid' with the target:
    - If 'nums[mid] == target' 
        found the value Return the index 'mid'.
    - If 'nums[mid] < target' 
        target must be in the right half. 
        Move the 'left' pointer to mid + 1.
    - If 'nums[mid] > target' 
        target must be in the left half. 
        Move the 'right' pointer to mid - 1.
- If the loop finishes without finding the target, Return -1.

Complexity
- Time  : O(log n)
- Space : O(1)

"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1


if __name__ == '__main__':
    sol = Solution()
    
    print(sol.search([-1, 0, 3, 5, 9, 12], 9))  
    print(sol.search([-1, 0, 3, 5, 9, 12], 2))