'''74. Search a 2D Matrix - Description
Medium

You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
'''


from typing import List

#     0           1             2
#  0 1 2 3    0  1  2  3    0  1  2  3
#[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# top = 0, bottom = 0, mid_row = 0
# l = 0, r = 3, m = 1

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    top = 0
    bottom = len(matrix) - 1
    while top <= bottom:
        mid_row = (top + bottom) // 2
        if target < matrix[mid_row][0]:
            bottom = mid_row - 1
        elif target > matrix[mid_row][-1]:
            top = mid_row + 1
        else:
            l = 0
            r = len(matrix[mid_row]) - 1
            while l <= r:
                mid_col = (l + r) // 2
                if target == matrix[mid_row][mid_col]:
                    return True
                elif target < matrix[mid_row][mid_col]:
                    r = mid_col - 1
                else:
                    l = mid_col + 1
            return False
    return False

"""Why does row = mid // cols and col = mid % cols work?

This mapping works because we simulate the matrix as a flattened 1D array of size m * n 
(where m is the number of rows and n is the number of columns). The relationship between 
the 1D index and 2D row/column indices comes from basic arithmetic.

Breakdown:
- mid: The current 1D index in the simulated array.
- cols: The number of columns in each row.

Row Calculation: row = mid // cols
- Integer division (//) gives the number of complete rows before the element at index mid.
- Example (matrix with 4 columns, cols = 4):
  - Index 0 to 3 belongs to row 0 because:
    - 0 // 4 = 0, 1 // 4 = 0, 2 // 4 = 0, 3 // 4 = 0.
  - Index 4 to 7 belongs to row 1 because:
    - 4 // 4 = 1, 5 // 4 = 1, 6 // 4 = 1, 7 // 4 = 1.

Column Calculation: col = mid % cols
- The remainder of the division (%) gives the column position within the row.
- Example (same 4-column matrix):
  - Index 0 % 4 = 0, index 1 % 4 = 1, index 2 % 4 = 2, index 3 % 4 = 3.
  - Index 4 % 4 = 0, index 5 % 4 = 1, index 6 % 4 = 2, index 7 % 4 = 3.

Example Walkthrough:
Consider the matrix:
matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
Here, cols = 4 (4 columns per row).

1. Suppose mid = 5:
   - Row: 5 // 4 = 1 → 2nd row (0-indexed).
   - Column: 5 % 4 = 1 → 2nd column (0-indexed).
   - Element: matrix[1][1] = 11.

2. Suppose mid = 10:
   - Row: 10 // 4 = 2 → 3rd row (0-indexed).
   - Column: 10 % 4 = 2 → 3rd column (0-indexed).
   - Element: matrix[2][2] = 34.

3. Suppose mid = 3:
   - Row: 3 // 4 = 0 → 1st row (0-indexed).
   - Column: 3 % 4 = 3 → 4th column (0-indexed).
   - Element: matrix[0][3] = 7.

Why This Works:
This mapping relies on the fixed number of columns (cols) to correctly interpret the flattened 1D index. 
The row is determined by the number of complete rows before the index, and the column is the remainder 
within the current row.

If the matrix were jagged, you'd need a different approach to handle variable row lengths.
"""
def search_matrix_flattened(matrix: List[List[int]], target: int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    l = 0
    r = rows * cols - 1
    while l <= r:
        mid = (l + r) // 2
        row = mid // cols
        col = mid % cols
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            r = mid - 1
        else:
            l = mid + 1
    return False
        


if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
    target = 34
    print(search_matrix(matrix, target))
    print(search_matrix_flattened(matrix, target))