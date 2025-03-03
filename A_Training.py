from typing import List

#  0  1  2  3   4   5
# [0, 4, 8, 10, 22, 29], target 29
# l = 5, r = 5, mid = 4
def binary_search(nums, target):
    l = 0
    r = len(nums) - 1
    
    while l <= r:
       mid = (l + r) // 2
       if nums[mid] == target:
           return mid
       elif nums[mid] > target:
           r = mid - 1
       else:
           l = mid + 1
    return None

def search_rotated(nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
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
    return None
            
                 
                          
def main():
    nums = [3,1]
    print(search_rotated(nums, 1))

if __name__ == "__main__":
    main()
