#O(n^2) time | O(n) space
def insertionSort(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            j = i
            while j != 0:
                if array[j] < array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
                j -= 1
    return array


def main():
    array = [2,-3,99,0,1000,-1000,9,8,1,-1]
    print(insertionSort(array))
    
if __name__ == "__main__":
    main()