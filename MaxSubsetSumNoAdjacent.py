# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    maxSums = []
    for i in range(len(array)):
        if i == 0:
            maxSums.append(array[i])
            continue
        elif i == 1:
            maxSums.append(max(array[0], array[i]))
            continue
        maxSum = max(maxSums[i - 1], maxSums[i - 2] + array[i])
        maxSums.append(maxSum)
    return maxSums[-1]        

# O(n) time | O(1) space    
def maxSubsetSumNoAdjacent2(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    maxSums = [0, 0]
    for i in range(len(array)):
        if i == 0:
            maxSums[0] = array[i]
            continue
        elif i == 1:
            maxSums[1] = max(array[1], array[0])
            continue
        maxSum = max(maxSums[1], maxSums[0] + array[i])
        maxSums[0] = maxSums[1]
        maxSums[1] = maxSum
    return maxSums[1]

# O(n) time | O(1 space)
def maxSubsetSumNoAdjacentSweet(array):
    previous, current = 0, 0
    for number in array:
        previous, current = current, max(current, previous + number)
    return current


def main():
    arr = [75]
    print(maxSubsetSumNoAdjacentSweet(arr))
    
if __name__ == "__main__":
    main()