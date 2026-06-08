"""
Problem : Best Time to Buy and Sell Stock
Difficulty : Easy
Link :- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Approach:
- Keep track of the lowest price.
- As we traverse the prices:
    - If the current price is lower than the minimum price,
        update the minimum price.
    - Otherwise:
        - Calculate the profit if we sell at the current price.
        - profit = current_price - minimum_price
        - Update the maximum profit if this profit is larger.
- Return the maximum profit found.

Complexity
- Time  : O(n)
- Space : O(1)

"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            
            min_price = min(min_price, price)
            
            current_profit = price - min_price

            max_profit = max(max_profit, current_profit)

        return max_profit

if __name__ == "__main__":

    sol = Solution()

    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,4,3,1]))
