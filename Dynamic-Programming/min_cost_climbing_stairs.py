"""
Problem : Min Cost Climbing Stairs
Difficulty : Easy
Link :- https://leetcode.com/problems/min-cost-climbing-stairs/

Approach:
- To reach the current stair, we can come from:
    - One stair before.
    - Two stairs before.
- Therefore:
    - min_cost(i) = cost[i] + min(min_cost(i - 1), min_cost(i - 2))
- Use two variables to store the minimum cost of the previous two stairs.
- Iterate through the cost array starting from the third stair.
- Update the minimum cost for each stair.
- The top is beyond the last stair, so return the minimum cost of the last two stairs.

Complexity
- Time  : O(n)
- Space : O(1)

"""

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        first = cost[0]
        second = cost[1]

        for i in range(2, len(cost)):

            current = cost[i] + min(first, second)

            first = second
            second = current

        return min(first, second)


if __name__ == "__main__":

    sol = Solution()

    print(sol.minCostClimbingStairs([10, 15, 20]))
    print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))