def make_squares(arr):
    squares = [0] * len(arr)
    l, r = 0, len(arr) - 1
    for i in reversed(range(len(arr))):
        if abs(arr[r]) >= abs(arr[l]):
            squares[i] = arr[r] ** 2
            r -= 1
        else:
            squares[i] = arr[l] ** 2
            l += 1
    return squares


def main():
    array = [-2, -1, 0, 2, 3]
    print(make_squares(array))
    
if __name__ == "__main__":
    main()