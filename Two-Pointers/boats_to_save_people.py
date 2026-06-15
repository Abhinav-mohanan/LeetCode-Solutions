"""
Problem : Boats to Save People
Difficulty : Medium
Link :- https://leetcode.com/problems/boats-to-save-people/

Approach:
- Each boat can carry at most 2 people.
- The total weight in a boat cannot exceed the limit.
- To minimize the number of boats:
    - Sort the people by weight.
- Use two pointers:
    - left  -> lightest person.
    - right -> heaviest person.
- Check if the lightest and heaviest person can share a boat:
    - If condition is true:
        - Put them in the same boat.
        - Move both pointers.
    - Otherwise:
        - The heaviest person must go alone.
        - Move only the right pointer.
- Continue until all people are assigned to boats.


Complexity
- Time  : O(n log n)
- Space : O(1)

"""


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:

        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:

            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            boats += 1

        return boats


if __name__ == "__main__":

    solution = Solution()

    print(solution.numRescueBoats([1, 2], 3))
    print(solution.numRescueBoats([3, 2, 2, 1], 3))