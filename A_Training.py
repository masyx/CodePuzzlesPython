# O(n^2) time | O(1) space
def twoNumberSumBruteForce(array, targetSum):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []

# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    present = {}
    for number in array:
        possibleNumber = targetSum - number
        if possibleNumber in present:
            return [number, possibleNumber]
        present[number] = True

    return []

# O(n log n) time | O(1) space
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        else:
            right -= 1
    return []


# [1,5,3,2] 7
# [1,2,3,5] 0
def main():
    print()
    
    
if __name__ == "__name__":
    main