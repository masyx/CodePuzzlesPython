# Given an array of positive integers and a number ‘S’, find the length of the smallest contiguous 
# subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
# Input: [2, 1, 5, 2, 3, 2], S=10
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to ‘10’ is [5, 2, 3].


# The time complexity of the above algorithm will be O(N). The outer for loop runs for all elements, 
# and the inner while loop processes each element only once; 
# therefore, the time complexity of the algorithm will be O(N+N), which is asymptotically equivalent to O(N).
# O(n) time | O(1) space
def smallest_subarray_sum(s, arr):
  l = 0
  _sum = 0
  result = float('inf')
  for r in range(len(arr)):
      _sum += arr[r]
      while _sum >= s:
          result = min(result, r - l + 1)
          _sum -= arr[l]
          l += 1
  
  return 0 if result == float('inf') else result


def main():
    arr = [2, 1, 5, 2, 3, 2]
    print(smallest_subarray_sum(10, arr))
    
    
if __name__ == "__main__":
    main()