"""
Problem : Fibonacci Number
Difficulty : Easy
Link :- https://leetcode.com/problems/fibonacci-number/

Approach:
- The Fibonacci sequence follows the recurrence:
    - fib(n) = fib(n - 1) + fib(n - 2)
- Handle the base cases:
    - fib(0) = 0
    - fib(1) = 1
- Use two variables to store the previous two Fibonacci numbers.
- Iterate from 2 to n:
    - Compute the current Fibonacci number.
    - Update the previous two values.
- Return the nth Fibonacci number.

Complexity
- Time  : O(n)
- Space : O(1)

"""

class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n

        prev1 = 0
        prev2 = 1

        for _ in range(2, n + 1):

            prev1, prev2 = prev2, prev1 + prev2

        return prev2


if __name__ == "__main__":

    sol = Solution()

    print(sol.fib(2))
    print(sol.fib(3))
    print(sol.fib(4))