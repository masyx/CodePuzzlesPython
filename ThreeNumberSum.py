# medium

# O(n^2) time | O(n) space, the max amount of triplets with numbers in it is bounded by n
def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                result.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum > targetSum:
                right -= 1
            else:
                left += 1
    return result    


def main():
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    print(threeNumberSum(array, 9))
    
    
if __name__ == "__main__":
    main()