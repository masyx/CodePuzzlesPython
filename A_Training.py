
#   0 1 2 3 4 5
# [-1,0,3,5,9,12] target 2
# l = 2, r = 1, mid = 1


#  0
# [5] target 5
# l = 0, r = 01, mid = 1

def binary_search(nums, target):
    nums.sort()
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        curr_num = nums[mid]
        if curr_num == target:
            return mid
        elif curr_num > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1
            
if __name__ == "__main__":
    numbers = [-1,0,3,5,9,12]
    print(binary_search(numbers, 9))