def main():
    array = [8, 5, 2, 9, 5, 6, 3]
    arr = bubbleSortBest(array)
    print(array)
    print(arr)


def bubbleSortBest(arr):
    isSorted = False
    counter = 0
    while not isSorted:# this is same as 'while isSorted == False:'
        isSorted = True
        for i in range(len(arr) - 1 - counter):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                isSorted = False
        counter += 1
    return arr
                
            
def bubbleSortMy(array):
    swapCounter = 99
    counter = 0
    while swapCounter != 0:
        swapCounter = 0
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapCounter += 1
        counter += 1
    return array

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
    
    
        
    
    
if __name__ == "__main__":
    main()