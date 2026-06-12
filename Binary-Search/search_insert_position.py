"""
Problem : Search Insert Position
Difficulty : Easy
Link :- https://leetcode.com/problems/search-insert-position/

Approach:
- Use Binary Search to efficiently search the sorted array.
- Find the middle element:
- Compare nums[mid] with target:
    - If equal return mid.
    - If nums[mid] is smaller than target:
        - Search in the right half.
    - Otherwise:
        - Search in the left half.
- If the target is not found:
    - left will point to the correct insertion position.

- When Binary Search finishes:
    - right points to the largest value smaller than the target.
    - left points to the first position where the target can be inserted.
- Therefore, left is the answer.

Complexity
- Time  : O(log n)
- Space : O(1)

"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
            
        return left


if __name__ == "__main__":

    sol = Solution()
    
    print(sol.searchInsert([1,3,5,6], 5))
    print(sol.searchInsert([1,3,5,6], 7))