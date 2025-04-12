from typing import List
from collections import defaultdict

class Solution:
    #               v
    # i:      0 1 2 3 4 5 6
    # nums:  [4,5,6,7,0,1,2]
    # l = 0; r = 6
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # left subarray is sorted
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # right subarray is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
        

        
        
        
    
def main():
    nums = [4,5,6,7,0,1,2]
    target = 0
    solution = Solution()
    print(solution.search(nums, target))
    
    
     
if __name__ == "__main__":
    main()
        