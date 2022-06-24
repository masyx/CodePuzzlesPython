def main():
    arr = [1, 5, 23, 111]
    target = -120
    print(binarySearch(arr, target))
    
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
        





if __name__ == "__main__":
    main()