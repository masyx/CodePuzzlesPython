def sortedSquaredArray(array):
    result = [0] * len(array)
    l = 0
    r = len(array) - 1
    for i in reversed(range(len(array))):
        val_1 = abs(array[l])
        val_2 = abs(array[r])
        if val_1 > val_2:
            result[i] = val_1**2
            l += 1
        else:
            result[i] = val_2**2
            r -= 1
    return result

def main():
    # [25]
    arr = [-5, 2, 3, 5, 6, 8, 9]
    print(sortedSquaredArray(arr))
    
if __name__ == "__main__":
    main()