

def main():
    inputArray1 = [-3, -2, -1, 5]

    print(sortedSquaredArrayOptimal(inputArray))
    
def sortedSquaredArray(array):
    squaredArray = []
    for i in range(len(array)):
        squaredValue = array[i]**2   
        squaredArray.append(squaredValue)
    
    squaredArray.sort()    
    return squaredArray


def sortedSquaredArray2(array):
    sortedArray = [0 for _ in array]
    
    for idx in range(len(array)):
        sortedArray[idx] = array[idx]**2
        
    sortedArray.sort()
    return sortedArray


def sortedSquaredArrayOptimal(array):
    squaredArray = [0] * len(array)
    left = 0
    right = len(array) - 1
    for i in range(len(array)):
        val1 = abs(array[left])
        val2 = abs(array[right])
        if val1 > val2:
            squaredArray[-i - 1] = val1**2
            left += 1
        else:
            squaredArray[-i - 1] = val2**2
            right -= 1
    
    return squaredArray


def sortedSquaredArrayOptimal(array):
    squaredArray = [0] * len(array)
    left = 0
    right = len(array) - 1
    for i in reversed(range(len(array))):
        val1 = abs(array[left])
        val2 = abs(array[right])
        if val1 > val2:
            squaredArray[i] = val1**2
            left += 1
        else:
            squaredArray[i] = val2**2
            right -= 1
    
    return squaredArray 
        





if __name__ == "__main__":
    main()