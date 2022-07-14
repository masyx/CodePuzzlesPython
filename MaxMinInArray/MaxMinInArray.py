def maxminInArray(array):
    maxValue = array[0]
    minValue = array[0]
    for i in range(1, len(array)):
        if array[i] > maxValue:
            maxValue = array[i]
        else:
            minValue = array[i]
            
    return [minValue, maxValue]


def main():
    array = [-1000,-1000,-999, -3, -1, 0, 1, 2, 8, 9, 99, 1000]
    print(maxminInArray(array))
    
    
if __name__ == "__main__":
    main()