"""
Problem : Maximum Number of Coins You Can Get
Difficulty : Medium
Link :- https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

Approach:
- There are 3 players:
    - Alice always takes the largest pile.
    - You always take the second largest pile.
    - Bob always takes the smallest pile.
- To maximize your coins, we should first sort the piles.
- After sorting:
    - Alice will take the largest available pile.
    - You should take the next largest pile.
    - Bob will take the smallest available pile.
- In each round:
    - Alice takes piles[right].
    - You take piles[right - 1].
    - Bob takes piles[left].
- Add your pile to result.
- Move:
    - right -= 2  (skip alice and bob piles)
- Continue until you have taken n / 3 piles.

Complexity
- Time  : O(n log n)
- Space : O(1)

"""
class Solution:
    def maxCoins(self, piles: list[int]) -> int:

        piles.sort()

        res = 0
        right = len(piles) - 1

        iteration = len(piles) // 3

        for _ in range(iteration):

            res += piles[right - 1]
            
            right -= 2
        
        return res


if __name__ == "__main__":

    sol = Solution()

    print(sol.maxCoins([2,4,1,2,7,8]))
    print(sol.maxCoins([2,4,5]))
    print(sol.maxCoins([9,8,7,6,5,1,2,3,4]))