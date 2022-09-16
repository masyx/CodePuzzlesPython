""" Given an array arr of unsorted numbers and a target sum, count all triplets in it such that 
    arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. 
    Write a function to return the count of such triplets.

Example 1:
Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

Example 2:
Input: [-1, 4, 2, 1, 3] , target=5  (sorted array = [-1, 1, 2, 3, 4])
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3] """

# O(n^3) time | O(n) space for sorting
def triplet_with_smaller_sum_my(arr, target):
    count = 0
    arr.sort()
    for i in range(len(arr)):
        for l in range(i + 1, len(arr)):
            r = len(arr) - 1
            while l < r:
                current_sum = arr[l] + arr[r] + arr[i]
                if current_sum < target:
                    count += 1
                    r -= 1
                elif current_sum >= target:
                    r -= 1
    return count

"""Sorting the array will take O(N * logN). The searchPair() will take O(N). So, overall searchTriplets() 
    will take O(N * logN + N^2), which is asymptotically equivalent to O(N^2). """
# O(n^2) time | O(n) space for sorting
def triplet_with_smaller_sum_my_2(arr, target):
    count = 0
    arr.sort()
    for i in range(len(arr)):
        l = i + 1
        r = len(arr) - 1
        while l < r:
            current_sum = arr[l] + arr[r] + arr[i]
            if current_sum < target:
                count += r - l
                l += 1
            elif current_sum >= target:
                r -= 1
    return count


def triplet_with_smaller_sum(arr, target):
  arr.sort()
  count = 0
  for i in range(len(arr)-2):
    count += search_pair(arr, target - arr[i], i)
  return count


def search_pair(arr, target_sum, first):
  count = 0
  left, right = first + 1, len(arr) - 1
  while (left < right):
    if arr[left] + arr[right] < target_sum:  # found the triplet
      # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
      # left and right to get a sum less than the target sum
      count += right - left
      left += 1
    else:
      right -= 1  # we need a pair with a smaller sum
  return count


def main():
    arr = [-1, 4, 2, 1, 3]
    print(triplet_with_smaller_sum(arr, 5))
    
    
if __name__ == "__main__":
    main()