from typing import List

#  0 1 2 3 4 5 6 7
# [5,6,7,8,9,1,2,3]
# l = 0, r = 7, mid = 3
def search_array(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[l]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
    

if __name__ == "__main__":
    nums = [5,6,7,8,9,1,2,3]
    target = 1
    print(search_array(nums, target))
