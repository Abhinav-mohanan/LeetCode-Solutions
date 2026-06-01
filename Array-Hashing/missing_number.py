"""
Problem : Missing Number
Difficulty : Easy
Link :- https://leetcode.com/problems/missing-number/

Approach:
- The array contains numbers from 0 to n.
- Since one number is missing : 
    the actual sum of the array will be less than the expected sum.
- Calculate the expected sum of numbers from 0 to n using the formula:
    - n * (n + 1) // 2
- Calculate the actual sum of all elements in the array.
- The difference between the expected sum and actual sum gives the missing number.
- Return the missing number.


Complexity
- Time  : O(n)
- Space : O(1)

"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        n = len(nums)

        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)

        missing_number = expected_sum - actual_sum

        return missing_number


if __name__ == "__main__":

    solution = Solution()

    print(solution.missingNumber([3, 0, 1]))
    print(solution.missingNumber([0, 1])) 
    print(solution.missingNumber([9,6,4,2,3,5,7,0,1])) 
    