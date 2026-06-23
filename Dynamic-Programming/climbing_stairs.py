"""
Problem : Climbing Stairs
Difficulty : Easy
Link :- https://leetcode.com/problems/climbing-stairs/

Approach:
- To reach the current stair, we can come from:
    - One step before.
    - Two steps before.
- Therefore:
    - ways(n) = ways(n - 1) + ways(n - 2)
- This follows the Fibonacci pattern.
- Use two variables to store the previous two results.
- Iterate from 3 to n and calculate the number of ways.
- Return the final answer.

Complexity
- Time  : O(n)
- Space : O(1)

"""

class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        prev = 1
        curr = 2

        for _ in range(3, n + 1):

            prev, curr = curr, prev + curr

        return curr


if __name__ == "__main__":

    sol = Solution()

    print(sol.climbStairs(2))
    print(sol.climbStairs(3))
    print(sol.climbStairs(5))