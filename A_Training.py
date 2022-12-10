# O(log n) time | O(1) space
def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    for i in range(len(array)):
        l = i + 1
        r = len(array) - 1
        while l < r:
            curr_sum = array[i] + array[l] + array[r]
            if curr_sum == targetSum:
                result.append([array[i], array[l], array[r]])
                l += 1
                r -= 1
            elif curr_sum > targetSum:
                r -= 1
            else:
                l += 1
    return result 


def main():
    nums = [2, 3, 4, 5, 10, 11, 32]
    print(threeNumberSum(nums, 19))
    
    
if __name__ == "__main__":
    main()