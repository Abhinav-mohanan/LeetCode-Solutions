"""
Problem : Container With Most Water
Difficulty : Medium
Link :- https://leetcode.com/problems/container-with-most-water/

Approach:
- Use two pointers, one at the beginning of the array and one at the end.
- The container width is the distance between the pointers.
- The container height is determined by the shorter line, 
    because water cannot exceed the shorter boundary.
- Calculate the current area using: 
    width x minimum height.
- Keep track of the maximum area found so far.
- Move the pointer:
    move the left pointer forward if its height is less than right pointer's height
    otherwise, move the right pointer backward.
- Continue until both pointers meet.

Complexity
- Time  : O(n)
- space : O(1)

"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:

            h = min(height[left], height[right])
            w = right - left
            current_area = h * w

            max_water = max(max_water, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
    print(sol.maxArea([1,1]))

