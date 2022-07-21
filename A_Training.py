# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    used = {}
    for num in array:
        possibleNumber = targetSum - num
        if possibleNumber in used:
            return [num, possibleNumber]
        used[num] = True
    return []

# O(n log(n)) time | O(1) space
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]
        elif array[left] + array[right] > targetSum:
            right -= 1
        else:
            left += 1
    return []


def main():
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    print(twoNumberSum(array, 0))