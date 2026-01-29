from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # [5,1,2,5,4]
    # [5,1,2]     [5,4]
    # [5,1] [2]   [5] [4]
    # [5] [1] recursively went down to single element in an array, start merging by comparing elements in array
    # [1,5] [2]
    # [1,2,5]     [4,5]
    # [1,2,4,5,5]
    
    

    # [5,1,2,5,4]
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        l = self.sortArray(nums[:mid])
        r = self.sortArray(nums[mid:])
        
        def mergeSort(left_arr, right_arr):
            res = []
            l_ptr = 0
            r_ptr = 0
            
            while l_ptr < len(left_arr) and r_ptr < len(right_arr):
                if left_arr[l_ptr] <= right_arr[r_ptr]:
                    res.append(left_arr[l_ptr])
                    l_ptr += 1
                else:
                    res.append(right_arr[r_ptr])
                    r_ptr += 1
                    
            while l_ptr < len(left_arr):
                res.append(left_arr[l_ptr])
                l_ptr += 1
            
            while r_ptr < len(right_arr):
                res.append(right_arr[r_ptr])
                r_ptr += 1
                
            return res
        
        return mergeSort(l, r)
    
     
        
if __name__ == "__main__":
    arr = []
    sol = Solution()
    print(sol.sortArray(arr))
    