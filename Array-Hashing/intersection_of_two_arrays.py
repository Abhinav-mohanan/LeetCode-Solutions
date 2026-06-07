"""
Problem : Intersection of Two Arrays
Difficulty : Easy
Link :- https://leetcode.com/problems/intersection-of-two-arrays/

Approach:
- We need to find all unique elements that appear in both arrays.
- To reduce extra space, create a set from the smaller array.
- Traverse the larger array:
    - If the current element exists in the set 'seen' ,
      add it to the result set.
- Use a result set because the answer should contain only unique elements.
- Convert the result set to a list and return it.

Complexity
- Time  : O(n + m)
- Space : O(min(n, m))

  n = length of nums1
  m = length of nums2

"""


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        smaller_set = set(nums1)
        result = set()

        for num in nums2:

            if num in smaller_set:
                result.add(num)

        return list(result)


if __name__ == "__main__":

    solution = Solution()

    print(solution.intersection([1, 2, 2, 1], [2, 2]))
    print(solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
