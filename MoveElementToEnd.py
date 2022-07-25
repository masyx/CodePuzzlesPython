# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    r = len(array) - 1
    l = 0
    while l < r:
        if array[l] == toMove:
            while array[r] == toMove:
                r -= 1
                if l >= r:
                    break
            array[l], array[r] = array[r], array[l]
            r -= 1
        l += 1           
    return array

# O(n) time | O(1) space
def moveElementToEndAlgo(array, to_move):
    l = 0
    r = len(array) - 1
    while l < r:
        while l < r and array[r] == to_move:
            r -= 1
        if array[l] == array[r]:
            array[l], array[r] = array[r], array[l]
        l += 1
    return array
            


def main():
    arr = [2, 1, 2, 2, 2, 3, 4, 2]
    to_move = 2
    print(moveElementToEnd(arr, to_move))
    
if __name__ == "__main__":
    main()