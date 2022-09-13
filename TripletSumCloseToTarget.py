""" Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to 
    the target number as possible, return the sum of the triplet. If there are more than one such triplet, 
    return the sum of the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target. """


# O(n^2) time | O(n) space, which is required for sorting
def triplet_sum_close_to_target(arr, target_sum):
    result = - 1
    arr.sort()
    smallest_diff = float('inf')
    for i in range(len(arr) - 2):
        l = i + 1
        r = len(arr) - 1
        while l < r:
            current_sum = arr[i] + arr[l] + arr[r]
            if current_sum == target_sum:
                return current_sum
            
            current_diff = target_sum - current_sum
            if abs(current_diff) < smallest_diff:
                smallest_diff = abs(current_diff)
                result = current_sum
                
            if current_diff > 0:
                l += 1    # we need a triplet with a bigger sum
            else:
                r -= 1    # we need a triplet with a smaller sum
    return result


def main():
    # [1,2,3,4,5] 10
    arr = [-2, 0, 1, 2]
    print(triplet_sum_close_to_target(arr, 2))
    
    
if __name__ == "__main__":
    main()