# O(log(n)*n^2)
def threeNumberSum(array, targetSum):
    result = []
    array.sort()
    for i in range(len(array)):
        l = i + 1
        r = len(array) - 1
        while l < r:
            current_sum = array[i] + array[l] + array[r]
            if current_sum == targetSum:
                result.append([array[i], array[l], array[r]])
                l += 1
                r -= 1
            elif current_sum < targetSum:
                l += 1
            else:
                r -= 1                
    return result


def main():
    # [-8, -6, 1, 2, 3, 5, 6, 12]
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    print(threeNumberSum(array, 0))
    
if __name__ == "__main__":
    main()