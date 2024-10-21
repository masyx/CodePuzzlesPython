#   0 1 2 3 4 5
# [-1,0,3,5,9,12] target 2
# l = 2, r = 1, mid = 1


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

#i  0  1  2  3  4   5
# [-1, 3, 4, 4, 6, 10] target = 11, answer = 1
# l = 4, r = 6, mid = 5
'''
Upper Bound: Find the first element that is greater than the given value.
Goal is to continue moving right until you find the first element greater than target.

If l == len(array), it means all elements in the array are less than or equal to the given value.
This means the upper bound is beyond the end of the array, and the element would go at the end to maintain the sorted order.
'''
def binary_search_upper_bound(nums, target):
    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid
    if l > 0 and nums[l - 1] == target:
        return l - 1
    else:
        return -1


#i 0  1  2  3   4   5    6
# [2, 4, 6, 10, 10, 10, 11]  target = 2
# l = 0, r = 0, mid = 0
'''The lower bound in binary search is the smallest index where nums[i] is greater 
   than or equal to (>=) the target.'''
def binary_search_lower_bound(nums, target):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    return l if l < len(nums) and nums[l] == target else -1
    
if __name__ == "__main__":
    nums = [2, 4, 6, 10, 10, 10, 11] 
    target = 10
    print(binary_search_lower_bound(nums, target))
    print(binary_search_upper_bound(nums, target))


        
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