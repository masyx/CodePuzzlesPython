'''
74. Search a 2D Matrix
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
    
    
if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
    target = 8
    print(search_matrix(matrix, target))