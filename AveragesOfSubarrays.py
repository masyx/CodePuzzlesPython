# O(n * K) time | O(n/k) space
def find_averages_of_subarrays_BF(K, arr):
    result = []
    for i in range(len(arr) - K + 1):
        Sum = 0.0
        for j in range(i, i + K):
            Sum += arr[j]
        result.append(Sum/K)
    return result

# O(n) time | O(n/k) space
def find_averages_of_subarrays(K, arr):
    result =[]
    l = 0
    Sum = 0.0
    for r in range(len(arr)):
        Sum += arr[r]
        if r >= K - 1:
            result.append(Sum/K)
            Sum -= arr[l]
            l += 1
    return result


def main():
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    print(find_averages_of_subarrays_BF(5, arr))
    print(find_averages_of_subarrays(5, arr))
    
    
if __name__ == '__main__':
    main()