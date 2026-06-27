"""
Problem : House Robber
Difficulty : Medium
Link :- https://leetcode.com/problems/house-robber/

Approach:
- At each house, we have two choices:
    - Rob the current house.
    - Skip the current house.
- Maintain two variables:
    - prev1 : Maximum money that can be robbed up to the previous house.
    - prev2 : Maximum money that can be robbed up to two houses before.
- For each house:
    - Rob current house:
        prev2 + current_money
    - Skip current house:
        prev1
    - Store the maximum of both choices.
- Return the maximum money that can be robbed.

Complexity
- Time  : O(n)
- Space : O(1)

"""

class Solution:
    def rob(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        prev1 = prev2 = 0

        for money in nums:

            prev1, prev2 = max(prev1, prev2 + money), prev1

        return prev1


if __name__ == "__main__":

    sol = Solution()

    print(sol.rob([1, 2, 3, 1]))
    print(sol.rob([2, 7, 9, 3, 1]))