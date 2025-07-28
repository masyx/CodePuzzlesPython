from typing import List, Optional
from collections import deque

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows = len(matrix)
        columns = len(matrix[0])
        l = 0
        r = (rows * columns) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            row = mid // columns
            column = mid % columns
            curr_num = matrix[row][column]

            if curr_num == target:
                return True
            elif target < curr_num:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
        
# n = 3       
def main():
    matrix =[[1]]
    sol = Solution()
    print(sol.searchMatrix(matrix, 2))



    
    
if __name__ == "__main__":
    main()
        