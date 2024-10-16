def TwoNumberSumSort(array, targetSum):
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
    nums = [3, 10, 4, 1, 99] 
    target = 11
    print(TwoNumberSumSort(nums, target))