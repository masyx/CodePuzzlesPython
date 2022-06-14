from random import randrange
import sys


def main():
    arr = [randrange(0, 99) for i in range(50)]    
    result = TwoNumberSum(arr, 10)
    print(result)
    

# O(n^2) time complexity, O(1) space complexity    
def TwoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return [] 


if __name__ == "__main__":
    main()