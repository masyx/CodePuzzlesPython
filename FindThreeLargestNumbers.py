def findThreeLargestNumbers(array):
    max = array[0]
    secondMax = -9999
    thirdMax = -9999
    for i in range(1, len(array)):
        if array[i] >= max:
            temp = max
            temp2 = secondMax
            max = array[i]
            secondMax = temp
            thirdMax = temp2
            continue
        if array[i] > secondMax:
            temp = secondMax
            secondMax = array[i]
            thirdMax = temp
            continue
        if array[i] > thirdMax:
            thirdMax = array[i]
            
    return [thirdMax, secondMax, max]


def main():
    arr = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]#[11,5,-2,77,10,4,-55,6]
    print(findThreeLargestNumbers(arr))
    
if __name__ == "__main__":
    main()