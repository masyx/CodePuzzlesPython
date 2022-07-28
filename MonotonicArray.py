#O(n) time | O(1) space
def isMonotonic(array) -> bool:
    monotonic = True
    increasing = False
    if len(array) <= 1:
        return monotonic
    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            continue
        elif array[i] > array[i - 1]:
            increasing = True
            break
        else:
            increasing = False
            break
    
    if increasing:
        for i in range(1, len(array)):
            if array[i] >= array[i - 1]:
                continue
            else:
                monotonic = False
                break
    else:
        for i in range(1, len(array)):
            if array[i] <= array[i - 1]:
                continue
            else:
                monotonic = False
                break
    return monotonic


def main():
    nums = [1,1,2,2,3]
    print(isMonotonic(nums))
    
    
if __name__ == '__main__':
    main()