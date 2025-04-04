
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1       
    
    #  c  0   1  2  3
    # r    
    # 0 [[1,  3, 5, 7],
    # 1  [10,11,16,20],
    # 2  [23,30,34,60]]
    # 10 -> (r * 4) + c = 1 * 4 + 0 = 4; r = (4 - 0)/ 4
    # 34 -> 2 * 4 + 2 = 10 
    # l = 0, r = 11
    # ind = (r * len(matrix[0])) + c; r = (ind - c) / len(matrix[0])
    # r      0              1             2
    # c 0  1  2  3     4  5  6  7     8  9 10 11
    # [[1, 3, 5, 7], [10,11,16,20], [23,30,34,60]]
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        l = 0
        r = columns * rows - 1
        
        while l <= r:
            mid = (l + r) // 2
            column = mid % columns
            row = mid // columns
            
            curr_number = matrix[row][column]
            if target == curr_number:
                return True
            elif target > curr_number:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
            
        
    
    
    
def main():
    arr = [1,4,6]
    target = 6
    solution = Solution()
    print(solution.search(arr, target))
    
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    #matrix = [[1,1]]
    target = 34
    print(solution.searchMatrix(matrix, target))
    
     
if __name__ == "__main__":
    main()
        