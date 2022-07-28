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

#O(n) time | O(1) space
def isMonotonic2(array):
    if len(array) <= 2:
        return True
    
    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue
        if breaksDirection(direction, array[i - 1], array[i]):
            return False
    return True

def breaksDirection(direction, previousInt, currentInt):
    difference = currentInt - previousInt
    if direction < 0:
        isBreaking = difference > 0
        return isBreaking
    return difference < 0

def main():
    nums = [1, 1, 1, 2, 4, 4, 5]
    print(isMonotonic2(nums))
    
    
if __name__ == '__main__':
    main()