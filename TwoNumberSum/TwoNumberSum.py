from random import randrange
import sys


def main():
    arr = [randrange(0, 99) for i in range(50)]    
    result = TwoNumberSum(arr, 10)
    print(result)
    
    
def TwoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return [] 


if __name__ == "__main__":
    main()