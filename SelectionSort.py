def selectionSortMyOriginal(array):
    for i in range(len(array)):
        smallest = array[i]
        isSorted = True
        for j in range(i + 1, len(array)):  
            if array[j] < smallest:
                isSorted = False
                smallest = array[j]
                smallestIdx = j
        if not isSorted:
            array[i], array[smallestIdx] = array[smallestIdx], array[i]    
    return array

def selectionSortMyImproved(array):
    for i in range(len(array)):
        smallestIdx = i
        for j in range(i + 1, len(array)):  
            if array[j] < array[smallestIdx]:
                smallestIdx = j
        array[i], array[smallestIdx] = array[smallestIdx], array[i]    
    return array


def selectionSortMyImproved2(array):
    for i in range(len(array)):
        smallestIdx = i
        for j in range(i + 1, len(array)):  
            if array[smallestIdx] > array[j]:
                smallestIdx = j
        array[i], array[smallestIdx] = array[smallestIdx], array[i]    
    return array










def main():
    arr = [8, 5, 6, 2, 8, 0]
    print(selectionSortMyImproved(arr))
    
if __name__ == "__main__":
    main()      