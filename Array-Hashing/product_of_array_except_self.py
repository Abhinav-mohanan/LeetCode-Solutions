"""
Problem : Product of Array Except Self
Difficulty : Medium
Link :- https://leetcode.com/problems/product-of-array-except-self/

Approach:
- Use the answer array to store prefix products.
- Prefix product means the product of all elements
   before the current index.
- Then traverse from right to left using a suffix product.
- Multiply the suffix product with the stored prefix product.
- The final result will contain the product of all
   elements except the current element


- We need to find the product of all numbers except the current index.
- Instead of using division, we calculate:
    - Product of numbers on the left side
    - Product of numbers on the right side

Step 1:
- Traverse from left to right.
- Store the product of all left-side numbers in the answer array.

Example:
nums = [1, 2, 3, 4]

Left products:
[1, 1, 2, 6]

Explanation:
- For index 0 → no left element → 1
- For index 1 → 1
- For index 2 → 1 * 2 = 2
- For index 3 → 1 * 2 * 3 = 6

Step 2:
- Traverse from right to left.
- Keep multiplying the right-side product into the answer array.

Right products:
[24, 12, 4, 1]

Final answer:
[24, 12, 8, 6]

Complexity:
- Time: O(n)
- Space: O(1) Extra Space
  (excluding the output array)

"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n  = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for j in range(n - 1, -1, -1):
            answer[j] *= suffix
            suffix *= nums[j]
        
        return answer

if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))
    print(sol.productExceptSelf([-1,1,0,-3,3]))
