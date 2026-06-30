"""
Problem : Find if Digit Game Can Be Won
Difficulty : Easy
Link : https://leetcode.com/problems/find-if-digit-game-can-be-won/

Approach:
- Traverse the array once.
- Separate the sum of single-digit numbers (< 10) and double-digit numbers (>= 10).
- Alice wins if these two sums are different.
- If both sums are equal, no matter which group Alice chooses, the remaining sums are equal,
  so she cannot win.
- Return whether the sums are different.

Complexity
- Time  : O(n)
- Space : O(1)

"""

from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:

        single_digit_sum = 0
        double_digit_sum = 0

        for num in nums:

            if num < 10:
                single_digit_sum += num

            else:
                double_digit_sum += num

        return single_digit_sum != double_digit_sum


if __name__ == "__main__":

    sol = Solution()

    print(sol.canAliceWin([1, 2, 3, 4, 10]))       
    print(sol.canAliceWin([1, 2, 3, 4, 5, 14])) 