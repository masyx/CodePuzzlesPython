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

# Recursive binary search
# O(log(n)) time | O(log(n)) space
def binarySearchRecursive(arr, target):
    return binarySearchHelper(arr, target, 0, len(arr) - 1)
    
def binarySearchHelper(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        return binarySearchHelper(arr, target, mid + 1, right)
    else:
        return binarySearchHelper(arr, target, left, mid - 1)
    
if __name__ == "__main__":
    nums = [2, 4, 6, 10, 10, 10, 11] 
    target = 10
    print(binary_search_lower_bound(nums, target))
    print(binary_search_upper_bound(nums, target))
