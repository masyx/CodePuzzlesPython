# O(n) time | O(1) space
def max_sub_array_of_size_k(arr, k):
    l = 0
    max_sum, curr_sum = 0, 0
    for r in range(len(arr)):
        curr_sum += arr[r]
        if r >= k - 1:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= arr[l]
            l += 1
    return max_sum


def main():
    arr = [2, 1, 5, 1, 3, 2]
    arr_2 = [2, 3, 4, 1, 5]
    print(max_sub_array_of_size_k(arr, 3))
    #print(max_sub_array_of_size_k(arr_2, 2))
    
    
if __name__ == '__main__':
    main()