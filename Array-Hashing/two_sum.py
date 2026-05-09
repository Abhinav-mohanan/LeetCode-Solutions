"""
Problem : Two Sum
Difficulty : Easy
Link :- https://leetcode.com/problems/two-sum/

Approach:
- Use a hash map to store previously seen numbers and their indices.
- For each number, calculate the complement (target - current number).
- If the complement already exists in the map, return the indices.
- Otherwise, store the current number and its index.

Complexity
- Time  : O(n)
- space : O(n)

"""

from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:

        prev_map = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[num] = i
        return []

if __name__ == "__main__":
    sol = Solution()
    print(sol.two_sum([2, 7, 11, 15], 9))

