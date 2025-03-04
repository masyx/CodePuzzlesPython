import math
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
        elif nums[mid] >= nums[l]:
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


# 123
def reverse_int(x: int) -> int:
    MIN = -2147483648  # -2^31,
    MAX = 2147483647  #  2^31 - 1

    res = 0
    while x:
        pop = int(math.fmod(x, 10))
        x = int(x / 10)

        if res > MAX // 10 or (res == MAX // 10 and pop > MAX % 10): # edge case number for second condition is 8463847412
            return 0
        if res < MIN // 10 or (res == MIN // 10 and pop < MIN % 10):
            return 0
        res = (res * 10) + pop

    return res


def main():
    nums = [3,0]
    #print(binary_search(nums, 1))
    #print(search_rotated(nums, 0))
    print(reverse_int(-1563847412))

if __name__ == "__main__":
    main()
