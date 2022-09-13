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


def triplet_sum_close_to_target(arr, target_sum):
  # TODO: Write your code here
  return -1


def main():
    arr = [-2, 0, 1, 2]
    print(triplet_sum_close_to_target(arr, 2))
    
    
if __name__ == "__main__":
    main()