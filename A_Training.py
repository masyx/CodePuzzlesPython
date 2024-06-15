def binary_search(lst, n):
    if not lst:
        return -1
    lst.sort()
    l = 0
    r = len(lst) - 1
    while l <= r:
        middle = (l + r) // 2
        if lst[middle] == n:
            return middle
        elif lst[middle] < n:
            l = middle + 1
        else:
            r = middle - 1
    return -1


if __name__ == "__main__":
    lst = [3, 10, 4, 1, 99] # [1,3,4,10,99]
    target = 11
    print(binary_search(lst, target))
