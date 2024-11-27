#  0 1 2 3 4 5 6 7
# [4,5,6,7,8,1,2,3] target = 2
# l=0, r=7, m=3

#  0 1 2 3 4 5 6
# [4,5,6,7,0,1,2] target = 0
# l=4, r=6, m=5

#  0 1 
# [5,4] target = 4
# l=1, r=1, m=0
from typing import List

def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        if nums[l] < nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if target > nums[r] or target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
    return -1


if __name__ == "__main__":
    nums = [4,5,6,7,8,1,2,3]
    target = 2
    print(search(nums, target))
