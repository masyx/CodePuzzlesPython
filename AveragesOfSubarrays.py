# O(n * K) time | O(n/k) space
def find_averages_of_subarrays(K, arr):
    result = []
    for i in range(len(arr) - K + 1):
        sum = 0.0
        for j in range(i, i + K):
            sum += arr[j]
        result.append(sum/K)
    return result


def main():
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    print(find_averages_of_subarrays(5, arr))
    
    
if __name__ == '__main__':
    main()