#   0 1 2 3 4 5
# [-1,0,3,5,9,12] target 2
# l = 2, r = 1, mid = 1


#  0
# [5] target 5
# l = 0, r = 01, mid = 1

# O(log n) time | O(1) space
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
    nums = [3, 10, 4, 1, 99] # [1,3,4,10,99]
    target = 11
    print(binary_search(nums, target))


        
# Recursive binary search
# O(log(n)) time | O(log(n)) space
def binarySearchRecursive(arr, target):
    return binarySearchHelper(arr, target, 0, len(arr) - 1)
    
def binarySearchHelper(arr, target, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return -1
    
    mediumIdx = (leftIdx + rightIdx) // 2
    valueAtMediumIdx = arr[mediumIdx]
    
    if target == valueAtMediumIdx:
        return mediumIdx
    elif target > valueAtMediumIdx:
        return binarySearchHelper(arr, target, mediumIdx + 1, rightIdx)
    else:
        return binarySearchHelper(arr, target, leftIdx, mediumIdx - 1)