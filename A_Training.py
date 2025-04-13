from typing import List
from collections import defaultdict

class Solution:
    #                    r  
    #                m
    #            l   
    #    i:      0 1 2 3 4 5 6
    # nums:     [3,4,5,1,2]
    # l = 3, r = 4, mid = 3
    #
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        # if array not rotated return first element
        if nums[r] > nums[l]:
            return nums[l]
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            # left subarray is sorted so inflection point is
            # guaranteed to be on the right
            if nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        
        

        
        
        
    
def main():
    nums = [3,4,5,1,2]
    target = 0
    solution = Solution()
    print(solution.findMin(nums))
    
    
     
if __name__ == "__main__":
    main()
        