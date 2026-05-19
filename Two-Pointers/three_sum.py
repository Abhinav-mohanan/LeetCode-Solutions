"""
Problem : 3Sum
Difficulty : Medium
Link :- https://leetcode.com/problems/3sum/

Approach:
- Sort the array, And iterate through the array
    'i' representing the first element of the triplet.
- If the current number 'nums[i]' is greater than 0, 
    'break' because no three positive numbers can sum up to 0.
- If the current number is the same as the previous one ('nums[i] == nums[i-1]'), 
    skip it to avoid duplicate triplets.
- Set up two pointers for the remaining part of the array: 
    'left' at 'i + 1' and 'right' at the end of the array.
- Calculate the total:
  - If 'total == 0', we found a valid triplet, Append it to results. 
        Move both pointers and skip any identical consecutive values 
            for 'left' and 'right' to avoid duplicate triplets.
  - If 'total' is small. Move the 'left' pointer forward.
  - If 'total' is large. Move the 'right' pointer backward.

Complexity
- Time  : O(n²)
- space : O(n)

"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()
        res = []

        for i in range(len(nums)):
            
            if nums[i] > 0 :
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                
                    left += 1
                    right -= 1

                elif total > 0:
                    right -= 1
                
                else:
                    left += 1
        
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))
    print(sol.threeSum([0,0,0,0]))
