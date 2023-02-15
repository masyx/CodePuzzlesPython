# O(n) time | O(1) space
def get_num_of_rotations_bf(array):
    for i in range(len(array)):
        if array[i] < array[i - 1]:
            return i
    return

# O(log (n)) time | O(1) space 
def get_rotate_num(arr):
    l = 0
    r = len(arr) - 1
    while r > l:
        current = (l + r) // 2
        if arr[current] > arr[current + 1]:
            return current + 1
        elif arr[current] > arr[l]:
            l = current
        else:
            r = current
    return 0


def main():
    arr1 = [1, 2, 3, 4, 5, 6]  # 0
    arr2 = [2, 3, 4, 5, 6, 7, 1]  # 6
    arr3 = [6, 1, 2, 3, 4, 5]  # 1
    arr4 = [4, 5, 6, 1, 2, 3]  # 3
    arr5 = [10, 50, -10, 0]
    print(get_num_of_rotations_bf(arr1))
    print(get_rotate_num(arr1))

    print(get_num_of_rotations_bf(arr2))
    print(get_rotate_num(arr2))

    print(get_num_of_rotations_bf(arr3))
    print(get_rotate_num(arr3))

    print(get_num_of_rotations_bf(arr4))
    print(get_rotate_num(arr4))
    
    print(get_num_of_rotations_bf(arr5))
    print(get_rotate_num(arr5))


if __name__ == "__main__":
    main()
