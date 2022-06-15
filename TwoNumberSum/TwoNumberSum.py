import numbers
from random import randrange
import sys
from turtle import right


def main():
    arr = [randrange(-10, 10) for i in range(10)]
    targetSum = randrange(1, 5)    
    result = TwoNumberSumHash(arr, targetSum)
    print(arr, f"Target Sum: {targetSum}")
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

# O(n) time complexity, O(n) space complexity
def TwoNumberSumHash(array, targetSum):
    numbers = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in numbers:
            return [num, potentialMatch]
        else:
            numbers[num] = True
    return []

# O(n log(n)) time / O(1) space
def TwoNumberSumAlgo(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum > targetSum:
            right -= 1
        else:
            left += 1
    return []            
            

if __name__ == "__main__":
    main()