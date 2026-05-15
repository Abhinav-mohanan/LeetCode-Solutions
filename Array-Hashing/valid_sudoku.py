"""
Problem: Valid Sudoku
Difficulty: Medium
Link: https://leetcode.com/problems/valid-sudoku/

Approach:
- Use sets to track numbers in rows, columns,
   and 3x3 boxes.
- Traverse each cell in the board.
- Skip empty cells ('.').
- If a number already exists in the same row,
   column, or box, return False.
- Otherwise, add the number to the corresponding sets.

Complexity:
- Time: O(1)
- Space: O(1)

The board size is fixed (9x9),
so complexity remains constant.

"""
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value == '.':
                    continue

                box_indx = (row // 3) * 3 + (col // 3)

                if (value in rows[row] or value in cols[col] or 
                    value in boxes[box_indx]):
                    return False
                
                rows[row].add(value)
                cols[col].add(value)
                boxes[box_indx].add(value)

        return True

if __name__ == '__main__':
    inp = []
    sol = Solution()
    print(sol.isValidSudoku(inp))