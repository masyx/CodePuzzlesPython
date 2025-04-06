
from typing import List, Optional
import math

class Solution:
    def binarySearch(self, nums, target):    
        def binary_search_recursive(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return binary_search_recursive(mid + 1, r)
            else:
                return binary_search_recursive(l, mid - 1)
                
        return binary_search_recursive(0, len(nums) - 1)

def main():
    nums = [0,1,2,3,4,5,6,7,8,9,10]
    
    target = 9
    solution = Solution()
    print(solution.binarySearch(nums, target))
    
     
if __name__ == "__main__":
    main()
        