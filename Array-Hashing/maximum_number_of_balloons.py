"""
Problem : Maximum Number of Balloons
Difficulty : Easy
Link :- https://leetcode.com/problems/maximum-number-of-balloons/

Approach:
- Count the frequency of each character in the input string.
- To form the word "balloon", we need:
    - b : 1
    - a : 1
    - l : 2
    - o : 2
    - n : 1
- Calculate how many complete "balloon" words can be formed:
    - count('b') // 1
    - count('a') // 1
    - count('l') // 2
    - count('o') // 2
    - count('n') // 1
- The minimum of these values is the answer.
- Return the minimum count.

Complexity
- Time  : O(n)
- Space : O(1)

"""

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count = Counter(text)

        return min(
            count['b'],
            count['a'],
            count['l'] // 2,
            count['o'] // 2,
            count['n']
        )


if __name__ == "__main__":

    sol = Solution()

    print(sol.maxNumberOfBalloons("nlaebolko"))
    print(sol.maxNumberOfBalloons("loonbalxballpoon"))
    print(sol.maxNumberOfBalloons("leetcode"))