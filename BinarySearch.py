def main():
    arr = [1, 5, 23, 111]
    target = -120
    print(binarySearch(arr, target))


#O(log(n)) time | O(1) space  
def binarySearch(arr, target):
    leftIdx = 0
    rightIdx = len(arr) - 1
    
    while leftIdx <= rightIdx:
       middleIdx = (leftIdx + rightIdx) // 2
       medianValue = arr[middleIdx]
       
       if medianValue == target:
           return middleIdx
       elif target > medianValue:
           leftIdx = middleIdx + 1
       else:
           rightIdx = middleIdx - 1
    
    return -1


        
# Recursive binary search
# O(log(n)) time | O(log(n)) space
def binarySearchRecursive(arr, target):
    binarySearchHelper(arr, target, 0, len(arr) - 1)
    
def binarySearchHelper(arr, target, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return -1
    
    mediumIdx = (leftIdx + rightIdx) // 2
    valueAtMediumIdx = arr[mediumIdx]
    
    if target == valueAtMediumIdx:
        return mediumIdx
    elif target > valueAtMediumIdx:
        binarySearchHelper(arr, target, mediumIdx + 1, rightIdx)
    else:
        binarySearchHelper(arr, target, leftIdx, mediumIdx - 1)




if __name__ == "__main__":
    main()