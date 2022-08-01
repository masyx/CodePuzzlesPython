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


def binarySearchIterative(arr, target):
    l = 0
    r = len(arr) - 1
    
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif target < arr[m]:
            r = m - 1
        else:
            l = m + 1
    return -1

def main():

    arr = [5, 23, 111]
    print(binarySearchIterative(arr, 5))
    
if __name__ == "__main__":
    main()