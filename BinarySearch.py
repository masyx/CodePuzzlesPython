def binary_search(lst, target):
    if not lst:
        return -1
    lst.sort()
    l = 0
    r = len(lst) - 1
    while l <= r:
        middle = (l + r) // 2
        if lst[middle] == target:
            return middle
        elif lst[middle] < target:
            l = middle + 1
        else:
            r = middle - 1
    return -1


if __name__ == "__main__":
    lst = [3, 10, 4, 1, 99] # [1,3,4,10,99]
    target = 11
    print(binary_search(lst, target))


        
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