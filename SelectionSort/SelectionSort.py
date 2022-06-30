def selectionSort(array):
    for i in range(len(array)):
        smallest = array[i]
        for j in range(i + 1, len(array)):
            isSorted = True
            if array[j] < smallest:
                isSorted = False
                smallest = array[j]
                smallestIdx = j
            if not isSorted:
                array[i], array[smallestIdx] = array[smallestIdx], array[i]    
    return array










def main():
    arr = [8, 5, 6, 2, 8, 0]
    print(selectionSort(arr))
    
if __name__ == "__main__":
    main()      