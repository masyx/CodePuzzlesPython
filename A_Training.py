#  0 1 2 3 4 5 6
# [4,5,6,7,8,1,2] target = 8
# l=4, r=6, m=5

#  0 1 2 3 4 5 6
# [4,5,6,7,0,1,2] target = 0
# l=4, r=6, m=5

from typing import List


def search(self, nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        if nums[mid] > nums[l]:
            if  target < mid and target >= nums[l] :
                r = mid - 1
            else:
                l = mid + 1
        else:
            if target > nums[mid] and target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return - 1

if __name__ == "__main__":

    