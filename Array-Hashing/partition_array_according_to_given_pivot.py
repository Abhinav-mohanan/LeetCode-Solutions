"""
Problem : Partition Array According to Given Pivot
Difficulty : Medium
Link :- https://leetcode.com/problems/partition-array-according-to-given-pivot/

Approach:
- Partitioning an array into three groups while maintaining relative order using linear traversal.
- Create three separate lists:
    - less_than_pivot
    - equal_to_pivot
    - greater_than_pivot
- Traverse the array once:
    - If the current element is smaller than pivot
        add it to less_than_pivot.
    - If it is equal to pivot add it to equal_to_pivot.
    - Otherwise  add it to greater_than_pivot.
- Finally, combine the three lists in the required order.

Complexity
- Time  : O(n)
- Space : O(n)

"""


class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:

        less_than_pivot = []
        equal_to_pivot = []
        greater_than_pivot = []

        for num in nums:

            if num < pivot:
                less_than_pivot.append(num)

            elif num == pivot:
                equal_to_pivot.append(num)

            else:
                greater_than_pivot.append(num)

        return (less_than_pivot + equal_to_pivot + greater_than_pivot)


if __name__ == "__main__":

    solution = Solution()

    print(solution.pivotArray([9, 12, 5, 10, 14, 3, 10], 10))
    print(solution.pivotArray([-3, 4, 3, 2], 2))
