
from typing import List, Optional
import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        left, right = 0, rows * columns - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // columns
            column = mid % columns
            if matrix[row][column] == target:
                return True
            elif target > matrix[row][column]:
                left = mid + 1
            else:
                right = mid - 1
        return False

        

def main():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    matrix = [[2]]

    solution = Solution()
    res = solution.searchMatrix(matrix, 2)
    print(res)
    
     
if __name__ == "__main__":
    main()
        