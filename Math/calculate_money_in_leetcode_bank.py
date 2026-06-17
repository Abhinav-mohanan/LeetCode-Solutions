"""
Problem : Calculate Money in Leetcode Bank
Difficulty : Easy
Link :- https://leetcode.com/problems/calculate-money-in-leetcode-bank/

Approach:
- Calculate the number of complete weeks and remaining days.
- Each complete week contributes:
    - First week sum = 28
    - Every next week contributes 7 more than the previous week.
- Use arithmetic progression to calculate the total amount for all complete weeks.
- For the remaining days:
    - Starting value is (weeks + 1).
    - Each day increases by 1.
- Calculate the remaining days sum using arithmetic progression.
- Return the total amount saved.

Complexity
- Time  : O(1)
- Space : O(1)

"""

class Solution:
    def totalMoney(self, n: int) -> int:

        weeks = n // 7
        days = n % 7

        all_weeks_sum = 28 * weeks + (7 * (weeks - 1) * weeks) // 2

        remaining_days_sum = (weeks * days) + (days * (days + 1) // 2)

        total_amount = all_weeks_sum + remaining_days_sum

        return total_amount


if __name__ == "__main__":

    sol = Solution()

    print(sol.totalMoney(4))
    print(sol.totalMoney(10))
    print(sol.totalMoney(20))