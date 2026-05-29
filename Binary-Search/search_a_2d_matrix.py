"""
Problem : Search a 2D Matrix
Difficulty : Medium
Link :- https://leetcode.com/problems/search-a-2d-matrix/

Approach:
- The matrix has a special property:
    - Each row is sorted.
    - The first element of a row is greater than the last element of the previous row.
- So treat the entire matrix as one sorted array.
- Apply Binary Search on the virtual array from index 0 to (rows * cols - 1).
- Find the middle index using:
    - mid = (left + right) // 2
- convert the middle index back to row and column:
    - row = mid // cols (integer division tells  which row the element belongs to)
    - col = mid % cols (Modulus tells  the position inside that row)
- Use matrix[row][col] to get the current value.
- If the value equals the target return True.
- If the middle value is smaller than the target, search in the right half.
- Otherwise search in the left half.
- If the search space becomes empty the target does not exist in the matrix.

Complexity
- Time  : O(log(m * n))
- Space : O(1)

"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:

            mid = (left + right) // 2

            row = mid // cols
            col = mid % cols

            current_value = matrix[row][col]

            if current_value == target:
                return True

            if current_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == "__main__":

    solution = Solution()

    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]

    print(solution.searchMatrix(matrix1, 3))
    print(solution.searchMatrix(matrix1, 13))  
