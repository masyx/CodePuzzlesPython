# O(log(n)) time | O(log(n)) space
def binarySearch(arr, target):
    return binarySearchHelper(arr, target, 0, len(arr) - 1)

def binarySearchHelper(arr, target, left, right):
    if left > right:
        return -1
    m = (left + right) // 2

    if arr[m] == target:
        return m
    elif target < arr[m]:
        return binarySearchHelper(arr, target, left, m - 1)
    else:
        return binarySearchHelper(arr, target, m + 1, right)



def main():

    arr = [5, 23, 111]
    print(binarySearch(arr, 120))
    
if __name__ == "__main__":
    main()