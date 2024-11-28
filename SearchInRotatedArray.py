'''33. Search in Rotated Sorted Array

Medium

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown 
pivot index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index 
of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
 

Constraints:
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4
'''


#  0 1 2 3 4 5 6 7
# [5,6,7,8,9,2,3,4] target = 9
# l = 4, r = 7, m = 5

#  0 1 
# [6,5] target = 5
# l = 1, r = 1, m = 0

#  0 1 2 
# [5,1,3] target = 3
# l = 2, r = 2, m = 1

# O(log n) time | O(1) space
def search_in_rotated_array(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        # left subarray is sorted
        if nums[l] <= nums[mid]:
            if target >= nums[l] and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        # right subarray is sorted
        else:
            if target > nums[mid] and target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1




if __name__ == "__main__":
    nums = [3,1]
    print(search_in_rotated_array(nums, 1))