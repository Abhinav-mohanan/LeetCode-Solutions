"""
Problem : Best Time to Buy and Sell Stock
Difficulty : Easy
Link :- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Approach:
- Use a sliding window with two pointers: 
    'left' for buying and 'right' for selling.
- The window between 'left' and 'right' represents transaction timeline.
- Move the 'right' pointer forward day by day to
    expand window and look for selling prices.
- If the buying price is less than the selling price:
    Calculate the current profit (selling price - buying price).
    Update 'max_profit' if this profit is higher than the previous one.
- If the selling price is lower than buying price:
    This means found a cheaper day to buy
    Slide the 'left' pointer directly to the 'right' pointer - 
        to reset window at this lower price.
- Continue expanding the window until the 'right' pointer reaches the end.

Complexity
- Time  : O(n)
- Space : O(1)

"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        left = 0
        right = 1

        while right < len(prices):

            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            
            right += 1
        
        return max_profit

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,4,3,1]))